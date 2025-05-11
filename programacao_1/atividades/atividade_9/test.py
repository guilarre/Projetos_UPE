from tabulate import tabulate
from datetime import datetime
import os
from pathlib import Path

# Funções


# Função pra carregar em forma de lista de dicionários
def carregar_contatos():
    contatos = []

    p = Path(__file__).with_name('agenda_contatos')
    try:
        p.open('x')
    except:
        pass

    with p.open('r') as file:
        linhas = file.readlines()
        for linha in linhas:
            # Decodificando as linhas em código binário
            byte_array = int(linha, 2).to_bytes(
                len(linha) // 8, byteorder='big')
            linha = byte_array.decode('utf-8')

            nome = linha.split(',')[0]
            telefone = linha.split(',')[1]
            aniversario = linha.split(',')[2]

            contatos.append(
                {'Nome': nome, 'Telefone': telefone, 'Aniversário': aniversario})

    return contatos


def listar_todos(contatos):
    if contatos == []:
        print("\nVocê não possui contatos registrados.")
    else:
        print('\n')
        print(tabulate(contatos, headers='keys'))
        print('\n')


def listar_contatos_letra(contatos):
    if contatos == []:
        print("\nVocê não possui contatos registrados.")
    else:
        contatos_letra = []
        letra = input("\nDigite uma letra que deseja pesquisar: ").lower()

        for contato in contatos:
            if contato['Nome'][0].lower() == letra:
                contatos_letra.append(contato)

        if contatos_letra == []:
            print("\nNão há contatos com essa letra.")
        else:
            print('\n')
            print(tabulate(contatos_letra, headers='keys'))
            print('\n')


def pesquisar_nome(contatos):
    if contatos == []:
        print("\nVocê não possui contatos registrados.")
    else:
        contatos_nome = []
        nome = input("\nDigite um nome para pesquisar: ").lower()
        for contato in contatos:
            if str(contato['Nome']).lower() == nome:
                contatos_nome.append(contato)

        if contatos_nome == []:
            print("\nVocê não possui contatos com esse nome.")
        else:
            print('\n')
            print(tabulate(contatos_nome, headers='keys'))
            print('\n')


def inserir_contato(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato (00)00000-0000: ")
    aniversario = input("Digite o aniversário do contato xx/xx/xxxx: ")
    contatos.append({'Nome': nome, 'Telefone': telefone,
                    'Aniversário': aniversario})

    print("\nContato salvo com sucesso!")
    return contatos


def remover_contato(contatos):
    if contatos == []:
        print("\nVocê não possui contatos registrados.")
        return contatos
    else:
        nome = input(
            "\nDigite o nome do contato que você deseja remover: ").lower()

        for contato in contatos:
            if str(contato['Nome']).lower() == nome:
                print(f"\nO contato que você deseja remover é:")
                print(f"Nome: {contato['Nome']}\nTelefone: {
                    contato['Telefone']}\nAniversário: {contato['Aniversário']}\n")
                confirmacao = input(
                    "Você confirma a remoção desse contato? Digite S para sim ou N para não: ").lower()
                if confirmacao == 's':
                    contatos.remove(contato)
                    return contatos
                else:
                    print("Contato não foi removido.")
                    return contatos


# Salvar lista de dicionários em números binários
def salvar_contatos(contatos):
    p = Path(__file__).with_name('agenda_contatos')
    with p.open('w') as file:
        for contato in contatos:
            line = str(contato.values())[
                13:-2].replace("'", "").replace(" ", "")
            byte_array = bytearray(line, 'utf-8')
            binary_str = ''.join(format(x, '08b') for x in byte_array)
            file.write(binary_str)
            file.write('\n')


def aniversariantes_mes(contatos):
    if contatos == []:
        print("\nVocê não possui contatos registrados.")
    else:
        aniversariantes_mes = []
        for contato in contatos:
            mes = contato['Aniversário'].split('/')[1]
            if '0' in mes:
                mes = mes.replace('0', '')
            if int(mes) == datetime.now().month:
                aniversariantes_mes.append(contato)

        if aniversariantes_mes == []:
            print("\nNão há aniversariantes este mês!")
        else:
            print('\n')
            print(tabulate(aniversariantes_mes, headers='keys'))
            print('\n')


# Mensagens

msg_bem_vindo = '''
###################

Agenda de contatos

###################
'''

msg_menu = '''
Digite a opção desejada:

[1] = Listar todos os contatos
[2] = Listar os contatos cujo nome inicia com uma dada letra
[3] = Pesquisar um contato pelo nome
[4] = Inserir contato
[5] = Remover contato
[6] = Imprimir os aniversariantes do mês

[S] = Sair

=> '''


# Menus


def main():
    os.system('cls')
    print(msg_bem_vindo)

    contatos = carregar_contatos()

    while True:
        opcao = input(msg_menu)

        if opcao == '1':
            listar_todos(contatos)

        elif opcao == '2':
            listar_contatos_letra(contatos)

        elif opcao == '3':
            pesquisar_nome(contatos)

        elif opcao == '4':
            contatos = inserir_contato(contatos)

        elif opcao == '5':
            contatos = remover_contato(contatos)

        elif opcao == '6':
            aniversariantes_mes(contatos)

        elif opcao == 's' or opcao == 'S':
            salvar_contatos(contatos)
            print("\nVocê saiu da agenda")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
