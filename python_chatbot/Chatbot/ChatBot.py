import random
import json
import pickle
import numpy as np
import os

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

# Recebe a função para reduzir a palavra a sua forma canonica
lematizador = WordNetLemmatizer()

intents_path = os.path.join(os.path.dirname(__file__), '../intents/intents.json')
palavras_path = os.path.join(os.path.dirname(__file__),'../chatbot_training/palavras.pkl')
classes_path = os.path.join(os.path.dirname(__file__),'../chatbot_training/classes.pkl')
modelo_path = os.path.join(os.path.dirname(__file__), '../chatbot_training/Modelo_ChatBot.h5')
# Carregar o dicionario para a variavel intents
intents = json.loads(open(intents_path).read())

palavras = pickle.load(open(palavras_path, 'rb'))

classes = pickle.load(open(classes_path, 'rb'))

modelo = load_model(modelo_path)

# tokeniza e lematiza a frase recebida


def filtrar_frase(frase):
    palavras_frase = nltk.word_tokenize(frase)
    palavras_frase = [lematizador.lemmatize(
        palavra) for palavra in palavras_frase]
    return palavras_frase

# Pega a frase, filtrando-a, e cria uma bag baseado nas comparações das palavras dessa frase com as palavras do modelo


def bag_of_words(frase):
    palavras_frase = filtrar_frase(frase)
    bag = [0] * len(palavras)

    for p in palavras_frase:
        for i, palavra in enumerate(palavras):
            # print(palavra)
            # print(p)
            if palavra.lower() == p.lower():
                bag[i] = 1

            # print(bag)
    return np.array(bag)


def prever_classe(frase):
    bow = bag_of_words(frase)
    # print(bow)
    res = modelo.predict(np.array([bow]))[0]
    # print(res)
    ERROR_THRESHOLD = 0.25

    resultados = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    # print(resultados)

    resultados.sort(key=lambda x: x[1], reverse=True)
    # print(resultados)
    lista_retorno = []
    for r in resultados:
        lista_retorno.append(
            {'intent': classes[r[0]], 'probabilidade': str(r[1])})
    # print(lista_retorno)
    return lista_retorno


def resposta(lista_intents, json_intents):
    tag = lista_intents[0]['intent']
    lista_de_intents = json_intents['intents']
    for i in lista_de_intents:
        if i['tag'] == tag:
            resultado = random.choice(i['reponses'])
            break
    return resultado


print('ChatBot LIGADO!')

def chatbot_answer(mensagem):
    ints = prever_classe(mensagem)
    return resposta(ints, intents)
    
