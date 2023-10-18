import json

def cerregar_pets():
    try:
        with open('pets.json','r') as arquivo:
            pets = json.load(arquivo)
    except FileExistsError:
        pets = []
    return pets

def salva_pets(pets):
    with open('pets.json','w') as arquivo:
        json.dump(pets, arquivo, indent=4)

def inserir_pets():
    tipo = input("Tipo de Pet: ")
    nome = input("Nome: ")

    while True:
        idade_input = input("Idade: ")
        try:
            idade = int(idade_input)
            break
        except ValueError:
            print("Idade deve ser um numero inteiro valido. Tente novamente. ")

    novo_pet = {
        "tipo": tipo,
        "nome": nome,
        "idade": idade
    }

    pets = cerregar_pets()
    pets.append(novo_pet)
    salva_pets(pets)
    print("Pet salvo com sucesso!")

def excluir_pets():
    nome = input("Nome do pet que deseja excluir: ")
    pets = cerregar_pets()

    novos_pets = [pet for pet in pets if pet['nome']!=nome]

    if len(pets) == len(novos_pets):
        print("Pet não encontrado. ")
    else:
        salva_pets(novos_pets)
        print("Pet ecluido com sucesso! ")

def listar_pets():
    pets = cerregar_pets()

    if len(pets) == 0:
        print("Nenhum pet encontrado. ")
    else:
        for i, pet in enumerate(pets, 1):
            print(f"{i}: Tipo:{pet['tipo']}, Nome:{pet['nome']}, Idade:{pet['idade']} ")

while True:
    print("\nOpções: ")
    print("1- Inserir Pet")
    print("2- Excluir Pet")
    print("3- Listar Todos Pets")
    print("4- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        inserir_pets()
    elif opcao == '2':
        excluir_pets()
    elif opcao == '3':
        listar_pets()
    elif opcao == '4':
        break
    else:
        print("Opção invaldia. Tente novamente.")