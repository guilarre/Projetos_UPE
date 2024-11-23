print("## Vamos pesquisar um carro para você!")
pesquisa = input(
    f'Digite o valor máximo do carro que você deseja, ou o estado de conservação dele ("novo", "seminovo", "conservado" ou "mal estado"): ')

file = open('./estoque_carros.txt', 'r')
file_lines = file.readlines()


def procurar_carro(pesquisa):
    try:
        # float
        for line in file_lines:
            line_dict = eval(line)
            if float(line_dict['preco']) <= float(pesquisa):
                print(line)

    except ValueError:
        # string
        for line in file_lines:
            line_dict = eval(line)
            if line_dict['estado'] == pesquisa:
                print(line)


procurar_carro(pesquisa)

file.close()
