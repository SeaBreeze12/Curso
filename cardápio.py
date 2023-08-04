#fazer o cardápio com as opções
#criar um carrinho e um total
#fazer um código onde, para cada valor chave no menu, printar a chave e o valor


Cardápio = {"frango assado": 3.50,
            "bife": 4.00,
            "batata": 3.00,
            "arroz": 2.00,
            "feijão": 2.00,
            "salada": 3.25,
            "macarrão": 3.75}

pedido = []
total = 0

for comida, value in Cardápio.items():
   print(f"{comida:10}: ${value:.2f}")

while True:
    comida = input("Selecione sua comida (q para sair): ")
    if comida == "q":
        break
    elif Cardápio.get(comida) is not None:
        pedido.append(comida)

for comida in pedido:
    total += Cardápio.get(comida)
    print(comida, end=" ")
print()
print(f"O total é: R${total:.2f}")
