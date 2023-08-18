import json

teste = list()

with open("json.json", "r") as trans:
     teste = json.load(trans)

print(teste)

nome = input("Digite um nome: ")
idade = input("Digite sua idade ")

teste.append(dict(nome = nome, idade = idade))

with open("json.json", "w") as trans:
     json.dump(teste, trans, indent="/t")