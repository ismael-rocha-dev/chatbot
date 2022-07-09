def intents():
    intents = [
        
            {"tag": "Loop",
             "patterns": [""],
             "responses": ["Desculpe, não entendi.", "Não sei muito sobre esse assunto, mas podemos falar sobre o raitec, o que acha?", 
             "Interessante, mas ainda não tenho conhecimento sobre isso", "Não sei... Mudando de assunto, você gosta de tecnologia?"]
             },
        
            {"tag": "Saudar",
             "patterns": ["Olá", "Oi", "Bom dia", "Boa tarde", "Boa noite", "Eai", "Como você está", "eai", "salve", "ola", "oi","ei","fala"],
             "responses": ["Olá, como você vai?", "Oi, tudo bem?", "Oi","Você precisa de ajuda?","Olá, eu sou o Chatbot, é assim que todos me chamam.",
             "Olá!","Oi!"]
             },
    
            {"tag": "Despedir",
             "patterns": ["Até mais", "Adeus", "Até logo", "Falou", "Foi bom te conhecer", "Tchau"],
             "responses": ["Até mais, volte sempre!", "Ahhh, sentirei sua falta...", "Prazer em conhecê-lo!", "Tchau Tchau!",
                          "Au revoir!"]
             },
        
            {"tag": "Nome",
             "patterns": ["Qual seu nome", "Como você se chama", "Quem é você","quem e voce", "o que é voce"],
             "responses": ["Meu nome é Chatbot, qual é o seu?", "Você pode me chamar de Chatbot, é meio redundante haha, mas todos me chamam assim!",
                          "Eu sou um Chatbot, fui programado para responder perguntas, então pode me chamar de Chatbot mesmo", "Meu nome é Chatbot, eu sou um robô e gosto de conversar!",
                          "Alguns me chamam de Chatbot, outros de RaiBot, em homenagem ao RAITEC"]
             },
        
            {"tag": "Idade",
             "patterns": ["Quantos anos você tem", "Qual sua idade", "Quando você nasceu"],
             "responses": ["Estou sendo concebido desde outubro de 2021.",
                          "Não tenho certeza... só sei que vi a rainha Elizabeth nascer!"]
             },
        
            {"tag": "Origem",
             "patterns": ["De onde você veio", "Como você foi criado"],
             "responses": ["Fui criado pelo grupo de Robótica, Automação, Inteligência Artificial e Tecnologia (RAITec)!"]
             },
        
            {"tag": "Silvestre",
             "patterns": ["Silvestre", "Você conhece o Silvestre", "Qual sua opnião sobre o Silvestre", "Quem é Silvestre"],
             "responses": ["Conheço não, pergunte ao Levir.", "Hmmm, lamento, meus criadores me proibiram de falar nesse assunto.",
             "Victor Silvestre é um dos membros do PET, salvo o engano."]
             },
        
            {"tag": "RAITec",
             "patterns": ["O que é o RAITec", "Quais os projetos do RAITec", "Quem são os membros do RAITec"],
             "responses": ["Resumidamente, o RAITec é top. Você pode conhecer mais sobre ele clicando nesse link: (SITE)", 
             "O Raitec é um projeto de extensão da Universidade Federal do Ceará criado em 2018.", "O RAITec é constituído por pessoas que tem sede de aprendizado e amam tecnologia."
             "Esse projeto é muito bom, eles desenvolvem apps, sites, circuitos eletrônicos e muito mais. Sempre com o intuito de ensinar e aprender!"],
             },
    ]
    return intents