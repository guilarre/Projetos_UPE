from pathlib import Path

# 1. Escreva um programa que:
# a. Crie/abra um arquivo texto de nome “arq.txt”.
# b. Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com
# o caractere "0".
# c. Feche o arquivo.

p = Path(__file__).with_name('arq.txt')
with p.open('a') as file:
    while True:
        char = input(
            "Digite um caractere qualquer (se desejar parar, digite 0): ")
        if char == '0':
            break
        file.write(char)

# Agora, abra e leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres
# armazenados.

p = Path(__file__).with_name('arq.txt')
with p.open('r') as file:
    caracteres = file.read()
    for caractere in caracteres:
        print(caractere)  # DÚVIDA: é pra separar por linha?

# 2. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas esse
# arquivo possui.

p = input("Digite o caminho de um arquivo .txt: ")
with open(p, 'r') as file:
    linhas = file.readlines()
    print(f"O arquivo escolhido contém {len(linhas)} linhas.")

# 3. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são
# vogais.

vogais = ['a', 'e', 'i', 'o', 'u']
qtd_vogais = 0

p = input("Digite o caminho de um arquivo .txt: ")
with open(p, 'r') as file:
    texto = file.read()

for letra in texto:
    if letra in vogais:
        qtd_vogais += 1

print(f"O texto contém {qtd_vogais} vogais.")

# 4. Faça um programa que receba do usuário um arquivo texto e um caractere. Mostre na tela quantas
# vezes aquele caractere ocorre dentro do arquivo.

p = input("Digite o caminho de um arquivo .txt: ")
caractere = input("Digite um caractere qualquer: ")
qtd_carac = 0

with open(p, 'r') as file:
    texto = file.read()

for letra in texto:
    if letra == caractere:
        qtd_carac += 1

print(f"O caractere escolhido aparece {qtd_carac} vezes no texto.")

# 5. Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo,
# mas com todas as letras minúsculas convertidas para maiúsculas. Os nomes dos arquivos serão
# fornecidos, via teclado, pelo usuário. A função que converte maiúscula para minúscula é a
# toupper(). Ela é aplicada em cada caractere da string.

p = input("Digite o caminho de um arquivo .txt: ")

print("\nIrei transformar esse texto para que todas as letras fiquem maiúsculas.\n")

new_name = input(
    "Digite o nome do novo arquivo (incluindo a extensão .txt ao final): ")

with open(p, 'r') as file:
    texto_original = file.read()

texto_novo = texto_original.upper()

new_path = "\\".join((str(Path(p).parent), new_name))

with open(new_path, 'w') as new_file:
    new_file.write(texto_novo)

# 6. Faça um programa no qual o usuário informa o nome do arquivo e uma palavra, e retorne o número
# de vezes que aquela palavra aparece no arquivo.

p = input("Digite o caminho de um arquivo .txt: ")
palavra_pesquisada = input("Digite uma palavra qualquer qualquer: ")
qtd_palavra = 0

with open(p, 'r') as file:
    texto = file.read()

for palavra in texto.split():
    if palavra.lower() == palavra_pesquisada:
        qtd_palavra += 1

print(f"A palavra que você digitou aparece {qtd_palavra} vezes no texto.")

# 7. Faça um programa que permita que o usuário entre com diversos nomes e telefone para cadastro, e
# crie um arquivo com essas informações, uma por linha. O usuário finaliza a entrada com "0" para o
# telefone.

contatos = []

while True:
    nome = input("Digite o nome de um contato (se desejar sair, digite 0): ")
    if nome == '0':
        break
    telefone = input(f"Digite o telefone de {nome}: ")

    contato = (nome, telefone)
    contatos.append(contato)

p = Path(__file__).with_name('agenda_contatos.txt')
with p.open('a') as file:
    for contato in contatos:
        file.write(str(contato)[1:-1].replace("'", "").replace(" ", ""))
        file.write("\n")

# 8. Faça um programa que leia um arquivo contendo o nome e o preço de diversos produtos
# (separados por linha), e calcule o total da compra.

precos = []

p = input("Digite o nome do arquivo contendo os produtos que serão comprados: ")
with open(p, 'r') as file:
    linhas = file.readlines()
    for item in linhas:
        precos.append(int(item.split(',')[1]))

print(f"O valor total da compra é de {sum(precos)}.")

# 9. Faça um programa para gerenciar uma agenda de contatos. Para cada contato armazene o nome, o
# telefone e o aniversário (dia e mês). O programa deve permitir:
# a. Inserir contato;
# b. Remover contato;
# c. Pesquisar um contato pelo nome;
# d. Listar todos os contatos;
# e. Listar os contatos cujo nome inicia com uma dada letra;
# f. Imprimir os aniversariantes do mês.

# Sempre que o programa for encerrado, os contatos devem ser armazenados em um arquivo binário.

# Quando o programa iniciar, os contatos devem ser inicializados com os dados contidos neste
# arquivo binário.
