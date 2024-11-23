lista_carros = []

while True:
    nome_carro = input(
        "Digite o nome do carro que deseja cadastrar (se desejar parar, digite 0): ")
    if nome_carro == '0':
        break

    preco = float(input("Digite o preço do carro: "))
    ano = int(input("Digite o ano de fabricação do carro: "))
    estado = input(
        'Digite o estado de conservação do carro ("novo", "seminovo", "conservado" ou "mau estado"): ')

    lista_carros.append(
        {'nome_carro': nome_carro, 'preco': preco, 'ano': ano, 'estado': estado})


file = open('./estoque_carros.txt', 'a')
for carro in lista_carros:
    file.write(str(carro))
    file.write("\n")
file.close()
