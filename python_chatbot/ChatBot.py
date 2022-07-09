import random
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

import Intents                                     # Inclui o dicionário

intents = Intents.intents()

lematizador = WordNetLemmatizer()                  # Recebe a função para reduzir a palavra a sua forma canonica

palavras = pickle.load(open('./python_chatbot/palavras.pkl', 'rb'))

classes = pickle.load(open('./python_chatbot/classes.pkl', 'rb'))

modelo = load_model('./python_chatbot/Modelo_ChatBot.h5')

# tokeniza e lematiza a frase recebida

def filtrar_frase(frase):
    palavras_frase = nltk.word_tokenize(frase)
    palavras_frase = [lematizador.lemmatize(palavra) for palavra in palavras_frase]
    return palavras_frase

# Pega a frase, filtrando-a, e cria uma bag baseado nas comparações das palavras dessa frase com as palavras do modelo
def bag_of_words(frase):
    palavras_frase = filtrar_frase(frase)
    bag = [0] * len(palavras)

    for p in palavras_frase:
        for i, palavra in enumerate(palavras):
            if palavra.lower() == p.lower():
                bag[i] = 1

    return np.array(bag)

def prever_classe(frase):
    bow = bag_of_words(frase)
    res = modelo.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25

    resultados = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    resultados.sort(key=lambda x: x[1], reverse=True)
    lista_retorno = []
    for r in resultados:
        lista_retorno.append({'intent': classes[r[0]], 'probabilidade': str(r[1])})
    return lista_retorno


def responder(lista_intents, intents):
    tag_mais_provavel = lista_intents[0]['intent']
    for intent in intents:
        if intent['tag'] == tag_mais_provavel:
            resposta = random.choice(intent['responses'])
            break
    return resposta

print('ChatBot LIGADO!')


def chatbot_answer(mensagem):
    classes = prever_classe(mensagem)
    resposta = responder(classes, intents)
    return resposta


