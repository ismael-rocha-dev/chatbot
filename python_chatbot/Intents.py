def intents():
    intents = [
        
            {"tag": "Loop",
             "patterns": [""],
             "reponses": ["Desculpe, nao entendi", "Repita, por favor"]
             },
       
            {"tag": "Saudar",
             "patterns": ["Olá", "Oi", "Bom dia", "Boa tarde", "Boa noite", "Eai", "Como você está", "Opa"],
             "reponses": ["Ola, como voce vai?", "Oi, tudo bem?", "Bom dia, boa tarde, boa noite!",
                          "Voce precisa de ajuda?"]
             },
       
            {"tag": "Despedir",
             "patterns": ["Ate mais", "Adeus", "Ate logo", "Falou", "Foi bom te conhecer", "Tchau"],
             "reponses": ["Ate mais, volte sempre!", "Ahhh, sentirei sua falta...", "Prazer em conhece-lo!", "Tchau Tchau!",
                          "Au revoir!"]
             },
        
            {"tag": "Nome",
             "patterns": ["Qual seu nome", "Como você se chama", "Quem é você"],
             "reponses": ["Meu nome eh (NOME), qual eh o seu?", "Voce pode me chamar de (NOME)",
                          "Meu nome é Uberverlandio! Brincadeira, eh (NOME) kkkk."]
             },
        
            {"tag": "Idade",
             "patterns": ["Quantos anos você tem", "Qual sua idade", "Quando você nasceu"],
             "reponses": ["Depende do referencial... estou sendo concebido desde outubro de 2021.",
                          "Nao tenho certeza... se sei que vi a rainha Elizabeth nascer!"]
             },
        
            {"tag": "Origem",
             "patterns": ["De onde você veio", "Como você foi criado"],
             "reponses": ["Fui criado pelo grupo de Robotica, Automacao, Inteligencia Artificial e Tecnologia (RAITec)!"]
             }
    ]
    return intents