import json
import datetime as dt

caminho = "data_json.json"

registro = list()

with open("data_json.json", "r") as openfile:
    registro = json.load(openfile)

Nome = input("Digite seu nome: ")
Idade = input("Digite sua idade: ")

log = dt.datetime.now().strftime('%d/%m/%Y as %H:%M')
Comentario = input("Faça um comentário: ")


registro.append(dict(Nome = Nome, Idade = Idade, log = log, Comentario = Comentario))

with open("data_json.json", "w") as trans:
    json.dump(registro, trans, indent= "\t")