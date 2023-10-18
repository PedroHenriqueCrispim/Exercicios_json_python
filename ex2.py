import json

pessoas = {}

with open('foods.csv','r') as arquivo:
    next(arquivo, None) #pula linha

    for linha in arquivo:
        partes = linha.strip().split(';')
        id, nome, comida = partes
        id = id.strip()
        nome = nome.strip()
        comida = comida.strip()

        pessoas[id] = {
            "nome": nome,
            "food": comida
        }

with open('pessoas.json','w') as arquivo_json:
    json.dump(pessoas,arquivo_json, indent=4)
