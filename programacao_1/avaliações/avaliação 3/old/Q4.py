print("## Vamos pesquisar um carro para você!")
pesquisa = input(
    f'Digite o valor máximo do carro que você deseja, ou o estado de conservação dele ("novo", "seminovo", "conservado" ou "mal estado"): ')

file = open('./estoque_carros.txt', 'r')
file_lines = file.readlines()


def procurar_carro(pesquisa):
    try:
        # float
        resultado = []
        for line in file_lines:
            line_dict = eval(line)
            if float(line_dict['preco']) <= float(pesquisa):
                resultado.append(line_dict)
        if resultado == []:
            print("Carro não encontrado!")
        else:
            for carro in resultado:
                print(carro)

    except ValueError:
        # string
        resultado = []
        for line in file_lines:
            line_dict = eval(line)
            if line_dict['estado'] == pesquisa:
                resultado.append(line_dict)
        if resultado == []:
            print("Carro não encontrado!")
        else:
            for carro in resultado:
                print(carro)


procurar_carro(pesquisa)

file.close()
