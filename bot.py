# bot.py

import os  # para lidar com diferentes sistemas operacionais
import discord  # funções e classes para criar o bot
from dotenv import load_dotenv  # para lidar com variáveis de ambiente
import sys # para lidar com paths absolutos, nesse caso adicionar o caminho do ChatBot.py
from discord.ext import commands

chatbot_path = os.path.join(os.path.dirname(__file__), './python_chatbot')#pega o caminho do programa que responde as perguntas
sys.path.append(chatbot_path)#adiciona a pasta do chatbot à variável path para  poder importar a função que responde as perguntas
from chatbot import chatbot_answer #importa o programa do chatbot que responde perguntas

load_dotenv()  # lê um arquivo .env e carrega as variáveis de ambiente dele
TOKEN = os.getenv('TOKEN')  # pega o token de uma variável de ambiente

intents = discord.Intents.default()
intents.members = True


# cria um objeto da classe discord.Client
client = discord.Client(intents=intents) #cria um cliente para lidar com eventos em um servidor
bot = commands.Bot(command_prefix='-') #cria um "bot" para fazer coisas quando um comando é passado


#--------------- Comandos para o BOT -----------
@bot.command(name='chat')
async def default_command(context, *args):
    frase = ' '.join(args)
    await context.send('{}, {}'.format(context.author.name, chatbot_answer(frase)))


bot.run(TOKEN)  # roda o bot com o token de acesso
#client.run(TOKEN) # roda um cliente com o token de acesso