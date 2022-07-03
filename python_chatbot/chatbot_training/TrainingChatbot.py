import os
from posixpath import dirname
import random

import json

import pickle

import numpy as np

import nltk
# Essa função serve para reduzir a palavra a sua forma canonica.
from nltk.stem.wordnet import WordNetLemmatizer

nltk.download('punkt', quiet=True)                            # Necessário para se instalar "punkt"
nltk.download('wordnet', quiet=True)                          # Necessário para se instalar "wordnet"
nltk.download('omw-1.4')

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout  # """Bug""" resolvido instalando-se NVidia COPA (problema de GPU?)
from tensorflow.keras.optimizers import SGD

# Recebe a função para reduzir a palavra a sua forma canonica
lematizador = WordNetLemmatizer()

main_dir = os.path.dirname(__file__)
intents_path = os.path.join(main_dir, '../intents/intents.json')
# Carregar o dicionario para a variavel intents
intents = json.loads(
    open(intents_path).read())

palavras = []
palavras_lematizadas = []
classes = []
documentos = []
# Caracteres que não serão levados em conta pela "leitura" das entradas
ignore_letters = ['?', '!', '.', ',', '~', '^']

# Percorre as categorias dos intents
for intent in intents['intents']:
    # Percorre os padrões de cada tag
    for pattern in intent['patterns']:
        # Separa as palavras em cada frase desses padrões
        listaPalavras = nltk.word_tokenize(pattern)
        # O vetor "palavras" é preenchido com essas palavras
        palavras.extend(listaPalavras)
        # O vetor documentos (matriz), é prenchido com essas palavras e suas respectivas "tags"
        documentos.append((listaPalavras, intent['tag']))
        # Estratégia para preencher o vetor classes com as "tags" sem repetição
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# print(documentos) # Teste

# Percorre o vetor com as palavras separadas, colocando-as
for palavra in palavras:
    # em outro vetor após desconsiderar alguns caracteres da ignore_letters
    if palavra not in ignore_letters:
        # e lematiza-las, ou seja, colaca-las na sua forma canôica (não funciona para todas)
        palavras_lematizadas.append(lematizador.lemmatize(palavra))

# Organiza e elimina as duplicatas no vetor
palavras_lematizadas = sorted(set(palavras_lematizadas))

# print(palavras_lematizadas) # Teste

# Organiza e elimina as duplicatas no vetor
classes = sorted(set(classes))

# Criação de dois arquivos "pkl"(?) com as palavras separadas
pickle.dump(palavras_lematizadas, open('palavras.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb')
            )                       # e as tags

# Bag of words: Transformar as palavras em dados numéricos (binários)

treinamento = []

# Declaração de um vetor com o tamanho da quantidade de tags preenchido com 0s
output_vazio = [0] * len(classes)

# print(output_vazio) # Teste

# Percorre a matriz documentos (indice 0: Palavras separadas) (indice 1: tags)
for documento in documentos:
    # A cada iteração, cria-se uma sacola vazia
    bag = []
    # "palavras_padroes" recebe as palavras separadas do documento
    palavras_padroes = documento[0]

    # print(documento) # Teste
    # print(palavras_padroes) # Teste

    # Percorre "palavras_padroes", colocando todas em caixa baixa
    palavras_padroes = [lematizador.lemmatize(
        palavra.lower()) for palavra in palavras_padroes]

    # print(palavras_padroes) # Teste

    # Percorre as palavras lematizadas anteriormente e verifica se
    for palavra in palavras_lematizadas:
        # existem paralelos na "palavras_padroes" acrescentando 1 caso sim e 0 caso não
        # print(palavras_padroes) # Teste             # (Laço duplo, palavras repetidas ???)
        # print(palavra) # Teste                      # (Maiscula != Miniscula ???)

        if palavra.lower() in palavras_padroes:
            bag.append(1)
        else:
            bag.append(0)

    # A cada iteração nos documentos, copia-se a lista de zeros para uma outra lista (linha de saída)
    output_linha = list(output_vazio)

    # print(output_linha) # Teste

    # No indice da presente "tag" do documento, atribui-se 1, com o restante sendo 0
    output_linha[classes.index(documento[1])] = 1
    # Finalmente, acrescenta-se tudo ao vetor treinamento (a sacola e a linha de saída)
    treinamento.append([bag, output_linha])

# print(treinamento) # Teste

random.shuffle(treinamento)                           # Embaralhar os dados

# print(treinamento) # Teste

# Transformando o vetor treinamento para um vetor numpy (???)
treinamento = np.array(treinamento)

# print(treinamento) # Teste

# Objeto para treino dos dados da sacola
treinar_x = list(treinamento[:, 0])
# Objeto para treino dos dados da linha de saída
treinar_y = list(treinamento[:, 1])


# Simples modelo sequencial(???)
modelo = Sequential()
modelo.add(Dense(128, input_shape=(len(treinar_x[0]),),                                   # Acrescentando camadas: 1ª Input Layer (camada densa com 128 neurônios e com uma shape de entrada que depende dos tamanhos dos dados de treinamento para x)
                 activation='relu'))                                                      # Função de Ativação: Unidade Linear Retificada (RELU: Rectified linear unity)
# Acrescentando camadas: Evitar Overfitting (???) / Parâmetros (???)
modelo.add(Dropout(0.5))
# Acrescentando camadas: camada densa com 69 neurônios e mesma função de ativação
modelo.add(Dense(69, activation='relu'))
modelo.add(Dropout(0.5))
# Acrescentando camadas: camada densa com (Tamanho das classes) neurônios e função de ativação "softmax": resume/escala os resultados na camada de saída (porcentagem da probabilidade das saidas)
modelo.add(Dense(len(treinar_y[0]), activation='softmax'))

# Stochastic gradient descent (Definindo um otimizador (taxa de aprendizagem, decaimento, momento, nesterov(???)))
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

# Compilação do modelo: (função de perda, otimizador, métrica)
modelo.compile(loss='categorical_crossentropy',
               optimizer=sgd, metrics=['accuracy'])

# Dados que devem ser treinados, quantas vezes alimentarão a rede neural, tamanho do lote, comando para obter uma quantidade média de informações
hist = modelo.fit(np.array(treinar_x), np.array(
    treinar_y), epochs=200, batch_size=5, verbose=1)
# Salvando o modelo
modelo.save('Modelo_ChatBot.h5', hist)

print('Treino Realizado!')

