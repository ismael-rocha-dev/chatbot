import random

import pickle

import numpy as np

import nltk
from nltk.stem.wordnet import WordNetLemmatizer                 # Essa função serve para reduzir a palavra a sua forma canonica.

# nltk.download('punkt', quiet=True)                            # Necessário para se instalar "punkt"
# nltk.download('wordnet', quiet=True)                          # Necessário para se instalar "wordnet"

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout  # """Bug""" resolvido instalando-se NVidia COPA (problema de GPU?)
from tensorflow.keras.optimizers import SGD


import Intents

intents = Intents.intents()                        # Inclui o dicionário

lematizador = WordNetLemmatizer()                  # Recebe a função para reduzir a palavra a sua forma canonica

palavras = []
palavras_lematizadas = []
classes = []
documentos = []
ignore_letters = ['?', '!', '.', ',', '´', '~', '^', '`']  # Caracteres que não serão levados em conta pela "leitura" das entradas


for intent in intents:                          # Percorre as categorias dos intents
    for pattern in intent['patterns']:                     # Percorre os padrões de cada tag
        # print(pattern) # Teste
        listaPalavras = nltk.word_tokenize(pattern)        # Separa as palavras em cada frase desses padrões
        palavras.extend(listaPalavras)                     # O vetor "palavras" é preenchido com essas palavras
        documentos.append((listaPalavras, intent['tag']))  # O vetor documentos (matriz), é prenchido com essas palavras e suas respectivas "tags"
        if intent['tag'] not in classes:                   # Estratégia para preencher o vetor classes com as "tags" sem repetição
            classes.append(intent['tag'])
        

#print(documentos) # Teste

for palavra in palavras:                                              # Percorre o vetor com as palavras separadas, colocando-as
    if palavra not in ignore_letters:                                 # em outro vetor após desconsiderar alguns caracteres da ignore_letters
        palavras_lematizadas.append(lematizador.lemmatize(palavra))   # e lematiza-las, ou seja, colaca-las na sua forma canôica (não funciona para todas)

palavras_lematizadas = sorted(set(palavras_lematizadas))              # Organiza e elimina as duplicatas no vetor

# print(palavras_lematizadas) # Teste

classes = sorted(set(classes))                                        # Organiza e elimina as duplicatas no vetor

pickle.dump(palavras_lematizadas, open('palavras.pkl', 'wb'))         # Criação de dois arquivos "pkl"(?) com as palavras separadas
pickle.dump(classes, open('classes.pkl', 'wb'))                       # e as tags

# Bag of words: Transformar as palavras em dados numéricos (binários)

treinamento = []

output_vazio = [0] * len(classes)                                    # Declaração de um vetor com o tamanho da quantidade de tags preenchido com 0s

# print(output_vazio) # Teste

for documento in documentos:                                         # Percorre a matriz documentos (indice 0: Palavras separadas) (indice 1: tags)
    bag = []                                                         # A cada iteração, cria-se uma sacola vazia
    palavras_padroes = documento[0]                                  # "palavras_padroes" recebe as palavras separadas do documento

    # print(documento) # Teste
    # print(palavras_padroes) # Teste

                                     # Percorre "palavras_padroes", colocando todas em caixa baixa
    palavras_padroes = [lematizador.lemmatize(palavra.lower()) for palavra in palavras_padroes]

        # print(palavras_padroes) # Teste

    for palavra in palavras_lematizadas:              # Percorre as palavras lematizadas anteriormente e verifica se
                                                      # existem paralelos na "palavras_padroes" acrescentando 1 caso sim e 0 caso não
        # print(palavras_padroes) # Teste             # (Laço duplo, palavras repetidas ???)
        # print(palavra) # Teste                      # (Maiscula != Miniscula ???)

        if palavra.lower() in palavras_padroes:
            bag.append(1)
        else:
            bag.append(0)

    output_linha = list(output_vazio)                 # A cada iteração nos documentos, copia-se a lista de zeros para uma outra lista (linha de saída)

    # print(output_linha) # Teste

    output_linha[classes.index(documento[1])] = 1     # No indice da presente "tag" do documento, atribui-se 1, com o restante sendo 0
    treinamento.append([bag, output_linha])           # Finalmente, acrescenta-se tudo ao vetor treinamento (a sacola e a linha de saída)

# print(treinamento) # Teste

random.shuffle(treinamento)                           # Embaralhar os dados

# print(treinamento) # Teste

treinamento = np.array(treinamento)                   # Transformando o vetor treinamento para um vetor numpy (???)

# print(treinamento) # Teste


treinar_x = list(treinamento[:, 0])                   # Objeto para treino dos dados da sacola
treinar_y = list(treinamento[:, 1])                   # Objeto para treino dos dados da linha de saída

# print(treinar_x) # Teste
# print(treinar_y) # Teste
# print(treinar_x[0]) # Teste

modelo = Sequential()                                                                     # Simples modelo sequencial(???)
modelo.add(Dense(128, input_shape=(len(treinar_x[0]),),                                   # Acrescentando camadas: 1ª Input Layer (camada densa com 128 neurônios e com uma shape de entrada que depende dos tamanhos dos dados de treinamento para x)
                 activation='relu'))                                                      # Função de Ativação: Unidade Linear Retificada (RELU: Rectified linear unity)
modelo.add(Dropout(0.5))                                                                  # Acrescentando camadas: Evitar Overfitting (???) / Parâmetros (???)
modelo.add(Dense(69, activation='relu'))                                                  # Acrescentando camadas: camada densa com 69 neurônios e mesma função de ativação
modelo.add(Dropout(0.5))
modelo.add(Dense(len(treinar_y[0]), activation='softmax'))                                # Acrescentando camadas: camada densa com (Tamanho das classes) neurônios e função de ativação "softmax": resume/escala os resultados na camada de saída (porcentagem da probabilidade das saidas)

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)                               # Stochastic gradient descent (Definindo um otimizador (taxa de aprendizagem, decaimento, momento, nesterov(???)))

modelo.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])      # Compilação do modelo: (função de perda, otimizador, métrica)

hist = modelo.fit(np.array(treinar_x), np.array(treinar_y), epochs=200, batch_size=5, verbose=1) # Dados que devem ser treinados, quantas vezes alimentarão a rede neural, tamanho do lote, comando para obter uma quantidade média de informações
modelo.save('Modelo_ChatBot.h5', hist)                                                       # Salvando o modelo

print('Treino Realizado!')

