

import csv
import json

alunos = {}

with open('notas.csv','r') as arquivo:
    arquivo_aluno = csv.reader(arquivo, delimiter=';')

    next(arquivo, None)

    for linha in arquivo_aluno:
        rm, nome, nota1, nota2, nota3, nota4 = linha
        rm = rm.strip()
        nome = nome.strip()
        notas = [float(nota1), float(nota2), float(nota3), float(nota4)]

        alunos[rm] = {
            "nome": nome,
            "notas": notas
        }

with open('alunos.json', 'w') as arquivo_json:
    json.dump(alunos, arquivo_json, indent=4)