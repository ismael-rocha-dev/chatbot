# bot.py

import os  # para lidar com diferentes sistemas operacionais
import discord  # funções e classes para criar o bot
from dotenv import load_dotenv  # para lidar com variáveis de ambiente
import sys # para lidar com paths absolutos, nesse caso adicionar o caminho do ChatBot.py

chatbot_path = os.path.join(os.path.dirname(__file__), './python_chatbot/Chatbot')#pega o caminho do programa que responde as perguntas
sys.path.append(chatbot_path)#adiciona a pasta do chatbot à variável path para  poder importar a função que responde as perguntas
from ChatBot import chatbot_answer #importa o programa do chatbot que responde perguntas

load_dotenv()  # lê um arquivo .env e carrega as variáveis de ambiente dele
TOKEN = os.getenv('DISCORD_TOKEN')  # pega o token de uma variável de ambiente
GUILD = os.getenv('DISCORD_GUILD')  # pega o nome do servidor discord

intents = discord.Intents.default()
intents.members = True


# cria um objeto da classe discord.Client
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} se conectou ao discord')


@client.event
async def on_member_join(member):
    print('alguem entrou')
    await member.create_dm()
    await member.dm_channel.send(f'Olá {member.name} bem vindo ao servidor, meu nome é {client.user} e eu faço parte do grupo de extensão RAITec')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    await message.channel.send(chatbot_answer(message.content.lower()))

client.run(TOKEN)  # roda o cliente com o token de acesso
