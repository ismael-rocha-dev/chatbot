# Introdução

Este programa é um bot para discord que conversa e responde perguntas básicas sobre o projeto RAITec. Feito utilizando redes neurais.

# Setup
Este programa se comunica com a API do discord para bots. Para utilizá-lo, é necessário primeiro criar um bot com a sua conta do discord pelo link: https://discord/developers/applications

### Após criar o bot do discord e adicionar ele em um servidor, siga esses passos:

## Configurações iniciais
- [ ] Clone este repositório 
- [ ] Crie um ambiente virtual para instalar as dependências desse projeto:
    - [ ] Abra a linha de comando na pasta do seu projeto, digite ```python -m venv venv```. Isso criará a pasta ```venv``` no seu projeto, ela é o seu ambiente virtual.
    - [ ] Ative o seu ambiente com o comando ```./venv/Scripts/activate```. Se tudo der certo você deve ver o nome ```(venv)``` no seu terminal.
- [ ] Instale todas as dependências do projeto com o comando: ```pip install -r requirements.txt```
- [ ] Crie um arquivo ```.env``` e escreva nele ```TOKEN=<O seu TOKEN>```. Copie o seu token do discord e    coloque ele no lugar de ```<O seu TOKEN>``` 

## Treinamento do Chatbot
Para utilizar o bot, primeiro é necessário treinar o bot com algumas perguntas e respostas prontas. Essas perguntas e respostas se encontram em ```./python_chatbot/Intents.py```. Esse arquivo contém um vetor de padrões que o Bot deve reconhecer, esses padrões seguem a estrutura:

- ```tag```: é nome do conjunto pergunta/resposta. Você pode colocar qualquer nome, contanto que não já exista uma tag com o mesmo nome.
- ```patterns```: são as frases que queremos que o chatbot identifique e ache uma resposta condizente.
- ```responses```: são as respostas que queremos que o chatbot envie quando um usuário realiza uma pergunta semelhante a uma frase dos ```patterns```

Modifique os intents se quiser mudar o comportamento do chatbot.

- [ ] navegue para a pasta ```python_chatbot``` com o comando ```cd python_chatbot``` e execute o comando ```python ./chatbot_train.py```. Isso gerará outros arquivos necessários para o funcionamento do chatbot (```Sempre que mudar os intents é necessário rodar este comando novamente```).

## Discord
Agora o bot está pronto para rodar, execute o arquivo ```bot.py``` e então o seu programa deverá se comunicar com a API do discord e estar pronto para responder perguntas no servidor em que tiver sido adicionado.

para se comunicar com o bot, digite em quaquer canal de texto o comando ```-chat``` seguido de uma frase que o bot ira responder.





