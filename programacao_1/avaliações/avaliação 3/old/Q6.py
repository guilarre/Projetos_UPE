import os.path

# Funções


def procurar_carro():
    pesquisa = input(
        f'\nDigite o preço máximo do carro que você deseja, ou o estado de conservação dele ("novo", "seminovo", "conservado" ou "mal estado"): ')

    file = open('./estoque_carros.txt', 'r', encoding='utf-8')
    file_lines = file.readlines()
    try:
        # float
        resultado = []
        for line in file_lines:
            line_dict = eval(line)
            if float(line_dict['preco']) <= float(pesquisa):
                resultado.append(line_dict)
        if resultado == []:
            print("\nCarro não encontrado!")
        else:
            print("\nCarros encontrados:\n")
            for carro in resultado:
                print(f"Modelo: {carro['nome_carro']}, Preço: {carro['preco']}, Ano: {
                      carro['ano']}, Estado: {carro['estado']};")

    except ValueError:
        # string
        resultado = []
        for line in file_lines:
            line_dict = eval(line)
            if line_dict['estado'] == pesquisa:
                resultado.append(line_dict)
        if resultado == []:
            print("\nCarro não encontrado!")
        else:
            print("\nCarros encontrados:\n")
            for carro in resultado:
                print(f"Modelo: {carro['nome_carro']}, Preço: {carro['preco']}, Ano: {
                      carro['ano']}, Estado: {carro['estado']};")

    file.close()


def cadastrar_carro(lista_carros):
    while True:
        nome_carro = input(
            "\nDigite o nome do carro que deseja cadastrar (se desejar parar, digite 0): ")
        if nome_carro == '0':
            break

        preco = float(input("Digite o preço do carro: "))
        ano = int(input("Digite o ano de fabricação do carro: "))
        estado = input(
            'Digite o estado de conservação do carro ("novo", "seminovo", "conservado" ou "mau estado"): ')

        lista_carros.append(
            {'nome_carro': nome_carro, 'preco': preco, 'ano': ano, 'estado': estado})
        print("\nCarro cadastrado!")

    file = open('./estoque_carros.txt', 'a', encoding='utf-8')
    if not os.path.exists('./estoque_carros.txt'):
        file.write('\n')
    for carro in lista_carros:
        file.write(str(carro))
        file.write('\n')
    file.close()
    print("\nCarro(s) registrado(s) com sucesso!")


# Mensagens

msg_bem_vindo = '''
##############################################

Bem-vindo à concessionária Paraíba Cars LTDA!'''

msg_menu = '''
##############################################

Digite a opção que você deseja ('p', 'c' ou 's'):

[p] = Procurar carro
[c] = Cadastrar carro
[s] = Sair do sistema

> '''

msg_procurar = '''
##############################################

Vamos pesquisar um carro para você!\n
'''

msg_cadastrar = '''
##############################################

Vamos cadastrar um carro!\n
'''

# Menus


def main():
    lista_carros = []
    print(msg_bem_vindo)

    while True:
        opcao = input(msg_menu)
        if opcao == 'p':
            procurar_carro()
        elif opcao == 'c':
            cadastrar_carro(lista_carros)
        elif opcao == 's':
            print("\nObrigado por usar o nosso sistema!")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n\n")


main()
