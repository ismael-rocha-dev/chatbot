def intents():
    intents = [
        
            {"tag": "Loop",
             "patterns": [""],
             "reponses": ["Desculpe, não entendi.", "Repita, por favor.", "Tendi não, pode RaiRepetir?"]
             },
        
            {"tag": "Saudar",
             "patterns": ["Olá", "Oi", "Bom dia", "Boa tarde", "Boa noite", "Eai", "Como você está", "Opa"],
             "reponses": ["Olá, como você vai?", "Oi, tudo bem?", "Bom dia, boa tarde, boa noite!",
                          "Você precisa de ajuda?"]
             },
    
            {"tag": "Despedir",
             "patterns": ["Até mais", "Adeus", "Até logo", "Falou", "Foi bom te conhecer", "Tchau"],
             "reponses": ["Até mais, volte sempre!", "Ahhh, sentirei sua falta...", "Prazer em conhecê-lo!", "Tchau Tchau!",
                          "Au revoir!"]
             },
        
            {"tag": "Nome",
             "patterns": ["Qual seu nome", "Como você se chama", "Quem é você"],
             "reponses": ["Meu nome é RAIBot, qual é o seu?", "Voce pode me chamar de RAIBot",
                          "Meu nome é Uberverlandio! Brincadeira, é RAIBot kkkkk."]
             },
        
            {"tag": "Idade",
             "patterns": ["Quantos anos você tem", "Qual sua idade", "Quando você nasceu"],
             "reponses": ["Depende do referencial... estou sendo concebido desde outubro de 2021.",
                          "Não tenho certeza... só sei que vi a rainha Elizabeth nascer!"]
             },
        
            {"tag": "Origem",
             "patterns": ["De onde você veio", "Como você foi criado"],
             "reponses": ["Fui criado pelo grupo de Robótica, Automação, Inteligência Artificial e Tecnologia (RAITec)!"]
             },
        
            {"tag": "Silvestre",
             "patterns": ["Silvestre", "Você conhece o Silvestre", "Qual sua opnião sobre o Silvestre", "Quem é Silvestre"],
             "reponses": ["Conheço não, pergunte ao Levir.", "Hmmm, lamento, meus criadores me proibiram de falar "
                                                             "desse assunto.", "Victor Silvestre é um dos membros do "
                                                                               "GDAE."]
             },
        
            {"tag": "RAITec",
             "patterns": ["O que é o RAITec", "Quais os projetos do RAITec", "Quem são os membors do RAITec"],
             "reponses": ["Resumidamente, o RAITec é top. Você pode conhecer mais sobre ele clicando nesse link: (SITE)"],
             },
    ]
    return intents