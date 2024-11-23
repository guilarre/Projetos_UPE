import random
from datetime import datetime

# 1. Escreva uma função chamada "soma" que receba dois parâmetros (a e b) e retorne a soma deles.


def somar(a, b):
    soma = a + b
    return soma


num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
resultado = somar(num1, num2)
print(f"A soma dos números é: {resultado}.")

# 2. Crie uma função chamada "isPar" que receba um número inteiro como parâmetro e retorne "True"
# se o número for par ou "False" caso contrário.


def isPar(num):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um número: "))
result = isPar(num)
print(result)

# 3. Elabore uma função chamada "media" que receba três notas como parâmetros e retorne a média
# aritmética delas.


def calcularMedia(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite outra nota: "))
nota3 = float(input("Digite mais uma nota: "))
media = calcularMedia(nota1, nota2, nota3)
print(f"A média das notas é: {media:.2f}.")

# 4. Elabore uma função chamada "imc" que receba o peso (em kg) e a altura (em metros) de uma
# pessoa e retorne o índice de massa corporal (IMC) dela.


def calcularIMC(peso, altura):
    imc = peso / altura ** 2
    return imc


peso = float(input("Digite o seu peso (em kg, por ex. 60): "))
altura = float(input("Digite a sua altura (em metros, por ex.: 1.65): "))
imc = calcularIMC(peso, altura)

print(f"O seu imc é {imc:.2f}.")

# 5. Elabore uma função chamada "calcularDesconto" que receba o valor de um produto e o
# percentual de desconto como parâmetros e retorne o valor com o desconto aplicado.


def calcularDesconto(valor, desconto):
    valor_final = valor * (1-(desconto/100))
    return valor_final


valor = float(input("Digite o valor do produto: "))
desconto = float(input(
    f"Digite o desconto do produto (por ex., se for 20% de desconto, digite: 20%): ")[:-1])
valor_final = calcularDesconto(valor, desconto)
print(f"O valor do produto com o desconto aplicado é: R${valor_final:.2f}.")


# 6. Elabore uma função chamada "calcularImpostoRenda" que receba o salário bruto de uma pessoa
# como parâmetro e retorne o valor do imposto de renda a ser pago, considerando as seguintes
# faixas de renda:

# a. Até R$ 1.903,98: isento
# b. De R$ 1.903,99 até R$ 2.826,65: alíquota de 7,5%
# c. De R$ 2 .826,66 até R$ 3.751,05: alíquota de 15%
# d. De R$ 3.751,06 até R$ 4.664,68: alíquota de 22,5%
# e. Acima de R$ 4.664,68: alíquota de 27,5%

def calcularImpostoRenda(salario):
    a = 0
    b = 0.075
    c = 0.15
    d = 0.225
    e = 0.275

    dict_faixas = {a: 'A', b: 'B', c: 'C', d: 'D', e: 'E'}

    if salario <= 1903.98:
        return a, dict_faixas[a]
    elif 1903.99 <= salario < 2826.65:
        return salario * b, dict_faixas[b]
    elif 2826.66 <= salario < 3751.05:
        return salario * c, dict_faixas[c]
    elif 3751.06 <= salario < 4664.68:
        return salario * d, dict_faixas[d]
    else:
        return salario * e, dict_faixas[e]


salario = float(input("Digite o valor do salário bruto: "))
imposto, faixa = calcularImpostoRenda(salario)
print(f"Você está na faixa {faixa}, portanto, você precisa pagar R${
      imposto:.2f} de imposto para o seu salário.")


# 7. Faça uma função chamada "calcularMediaArredondada" que receba uma lista de números como
# parâmetro e retorne a média aritmética desses números, arredondada para o inteiro mais
# próximo.

def calcularMediaArredondada(num_list):
    try:
        media = sum(num_list) / len(num_list)
        return round(media)
    except ZeroDivisionError:
        return "erro"


num_list = []
while True:
    try:
        num = float(
            input(f"Digite um número (digite qualquer letra se desejar parar): "))
        num_list.append(num)
    except ValueError:
        break

media_arredondada = calcularMediaArredondada(num_list)

if media_arredondada == "erro":
    print("Digite ao menos um valor.")
else:
    print(f"A média aritmética dos números digitados é: {media_arredondada}.")


# 8. Desenvolva uma função chamada "contarDigitosParesImpares" que receba um número inteiro
# como parâmetro e retorne a quantidade de dígitos pares e a quantidade de dígitos ímpares
# presentes nesse número.

def contarDigitosParesImpares(num):
    count_evens = 0
    count_odds = 0
    for digit in num:
        if int(digit) % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1
    return count_evens, count_odds


num = input("Digite um número inteiro: ")
count_evens, count_odds = contarDigitosParesImpares(num)
print(f"O número digitado contém {count_evens} dígitos pares e {
      count_odds} dígitos ímpares.")

# 9. Crie uma função chamada "calcularMediaAlunos" que receba uma lista de alunos, onde cada aluno
# é representado por um objeto com os atributos "nome" e "nota". A função deve calcular e
# retornar a média das notas de todos os alunos.


def calcularMediaAlunos(lista_alunos):
    notas_alunos = []

    for aluno in lista_alunos:
        notas_alunos.append(aluno['Nota'])

    media_alunos = sum(notas_alunos) / len(notas_alunos)
    return media_alunos


lista_alunos = []

while True:
    nome = input(f"Digite o nome do aluno (se desejar parar, digite 0): ")
    if nome == '0':
        break

    nota = float(input(f"Digite sua nota (se desejar parar, digite 0): "))
    if nota == 0:
        break

    lista_alunos.append({"Nome": nome, "Nota": nota})

media_alunos = calcularMediaAlunos(lista_alunos)
print(f"A média das notas de todos os alunos é: {media_alunos}.")


# 10. Crie uma função chamada "calcularIdade" que receba o ano de "nascimento" de uma pessoa como
# parâmetro e retorne a idade atual.


def calcularIdade(ano_nascimento):
    ano_atual = datetime.now().year
    idade_atual = ano_atual - ano_nascimento
    return idade_atual


ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_atual = calcularIdade(ano_nascimento)
print(f"A idade atual da pessoa de ano de nascimento {
      ano_nascimento} é {idade_atual}.")

# 11. Crie uma função chamada "gerarTabuada" que receba um "número" como parâmetro e exiba a
# tabuada desse número de 1 a 10 no console.


def gerarTabuada(num):
    tabuada = []
    for i in range(1, 11):
        tabuada.append(num * i)
    print(tabuada)


num = int(input("Digite um número: "))
gerarTabuada(num)

# 12. Escreva uma função chamada "advinheNumero" que gera aleatoriamente um número inteiro entre
# 1 e 100. Em seguida, permita que o usuário insira tentativas para adivinhar o número. A função
# deve dar dicas ao usuário se o número correto é maior ou menor do que a tentativa. Quando o
# usuário acertar, exiba uma mensagem de parabéns e informe a quantidade de tentativas
# utilizadas.


def adivinheNumero():
    numero_definido = random.randint(1, 100)
    numero_tentativa = 0
    count_tentativas = 0
    while numero_tentativa != numero_definido:
        numero_tentativa = int(input("Tente adivinhar o número escolhido: "))
        if numero_tentativa > numero_definido:
            print("O número é menor que esse.")
        elif numero_tentativa < numero_definido:
            print("O número é maior que esse.")
        count_tentativas += 1
    print(f"Parabéns, você acertou o número! Foram feitas {
          count_tentativas} tentativas até você acertar.")


adivinheNumero()

# 13. Crie uma função chamada "verificarPropriedade" que receba um objeto e uma string como
# parâmetros, e retorne true se o objeto possuir a propriedade com o nome especificado na string, e
# false caso contrário.


def verificarPropriedade(dict, string):
    result = None

    for key, value in dict.items():
        print(key, value)
        if key == string or value == string:
            result = True
            break
        else:
            result = False

    return result


dict = {}
print("####### Vamos criar um dicionário! #######")

while True:
    chave = input("Digite o nome da chave (digite 0, se desejar parar): ")
    if chave == '0':
        break

    valor = input("Digite o nome do valor (digite 0, se desejar parar): ")
    if chave == '0':
        break

    dict[chave] = valor

while True:
    print("####### Vamos verificar se o dicionário criado possui uma chave ou valor específico! #######")

    string = input(
        "Digite o nome de uma chave ou valor que você deseja consultar (digite 0, se desejar parar): ")
    if string == '0':
        break

    resultado = verificarPropriedade(dict, string)

    if resultado == True:
        print("O dicionário POSSUI a chave ou valor consultado.")
    if resultado == False:
        print("O dicionário NÃO possui a chave ou valor consultado.")

# 14. Faça uma função chamada "calcularPrecoProduto" que receba o "valor de custo" de um produto, a
# "margem de lucro" desejada (em percentual) e o "valor do frete" como parâmetros. A função deve
# calcular e retornar o preço de venda do produto, considerando que o preço de venda é igual ao
# custo acrescido da margem de lucro e do valor do frete.


def calcularPrecoProduto(custo, lucro, frete):
    preco_venda = custo * lucro + frete
    return preco_venda


custo = float(input("Digite o valor de custo do produto: "))
lucro = float(
    input("Digite a margem de lucro desejada (em porcentagem, por ex., 20%): ")[:-1])
lucro = 1 + (lucro / 100)
print(lucro)
frete = float(input("Digite o valor do frete: "))

preco_venda = calcularPrecoProduto(custo, lucro, frete)
print(f"O preço final de venda é: {preco_venda}.")

# 15. Escreva uma função que aceite uma string como parâmetro e encontre a palavra mais longa dentro
# da string. String de exemplo: 'Tutorial de desenvolvimento da web'. Resultado esperado:
# 'Desenvolvimento'.


def maiorPalavra(string):
    maior_palavra = ''
    for palavra in string.split():
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
    return maior_palavra


string = input("Digite uma frase: ")
print(maiorPalavra(string))

# 16. Escreva uma função que pegue uma lista de strings e as imprima, uma por linha, em um quadro
# retangular. Por exemplo, a lista ["Hello", "World", "in", "a", "frame"] é impressa como:

# *********
# * Hello *
# * World *
# * in *
# * a *
# * frame *
# *********


def frameIt(frase):
    palavras = frase.split()
    maior_palavra = ''
    for palavra in palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
    largura = len(maior_palavra)

    print('*'*(largura + 4))
    for palavra in palavras:
        print('*', palavra.center(largura), '*')
    print('*'*(largura + 4))


frase = input("Digite uma frase: ")
frameIt(frase)

# 17. Crie uma função que receba um array de strings e retorne um novo array contendo apenas as
# strings que têm mais de 5 caracteres.


def stringMaisDe5(palavras):
    mais_de_5 = []
    for palavra in palavras:
        if len(palavra) > 5:
            mais_de_5.append(palavra)
    return mais_de_5


frase = input("Digite uma frase: ")
palavras = frase.split()
mais_de_5 = stringMaisDe5(palavras)

if mais_de_5 == []:
    print("Não há palavras com mais de 5 caracteres.")
else:
    print(f"As palavras com mais de 5 caracteres são: {mais_de_5}.")

# 18. Crie uma função que recebe um array de objetos com informações sobre livros (título, autor, ano,
# etc.) e retorne um novo array apenas com os livros escritos por determinado autor.


def livrosPorAutor(books):
    print("\n### Pesquisa por autor ###\n")
    search_str = input("Digite o nome do autor que deseja pesquisar: ")
    search_result = []

    for book in books:
        if book["Autor"] == search_str:
            search_result.append(book)

    return search_result


books = []
count_livros = 1

print("\n### Vamos criar uma biblioteca! ###\n")
while True:
    print(f"Livro {count_livros}:\n")

    titulo = input("Digite o título do livro (Digite 0 se desejar parar): ")
    if titulo == '0':
        break

    autor = input("Digite o autor do livro (Digite 0 se desejar parar): ")
    if autor == '0':
        break

    genero = input("Digite o gênero do livro (Digite 0 se desejar parar): ")
    if genero == '0':
        break

    ano = input("Digite o ano do livro (Digite 0 se desejar parar): ")
    if ano == '0':
        break

    books.append({"Título": titulo, "Autor": autor,
                 "Gênero": genero, "Ano": ano})
    count_livros += 1


search_str = livrosPorAutor(books)
print(search_str)

# 19. Crie uma função que recebe um array de objetos representando pessoas (com nome, idade, etc.) e
# retorne o nome da pessoa mais velha.


def maisVelho(lista_pessoas):
    maior_idade = 0
    mais_velho = None
    for pessoa in lista_pessoas:
        if pessoa["Idade"] > maior_idade:
            mais_velho = pessoa
            maior_idade = pessoa["Idade"]

    return mais_velho["Nome"]


lista_pessoas = [
    {
        "Nome": "Carlos",
        "Idade": 30,
        "Profissão": "Professor de História"
    },
    {
        "Nome": "Angela",
        "Idade": 67,
        "Profissão": "Aposentada"
    },
    {
        "Nome": "Guilherme",
        "Idade": 28,
        "Profissão": "Professor de Inglês"
    },
    {
        "Nome": "Julia",
        "Idade": 38,
        "Profissão": "Professora de Inglês"
    }
]

print(maisVelho(lista_pessoas))

# 20. Escreva uma função que recebe um array de objetos com informações sobre carros (com marca,
# modelo, ano, etc.) e retorne um novo array apenas com os carros fabricados após um certo ano
# específico.


def carroAposAno(lista_carros):
    print("## Vamos mostrar os carros a partir de um ano escolhido ##")
    ano = int(input("Escolha o ano: "))
    search_result = []
    for carro in lista_carros:
        if carro["Ano"] >= ano:
            search_result.append(carro)
    return search_result


lista_carros = [
    {
        "Marca": "Volkswagen",
        "Modelo": "Gol",
        "Ano": 2018,
    },
    {
        "Marca": "Volkswagen",
        "Modelo": "Polo",
        "Ano": 2010,
    },
    {
        "Marca": "Volkswagen",
        "Modelo": "Fusca",
        "Ano": 1976,
    },
    {
        "Marca": "Volkswagen",
        "Modelo": "Passat",
        "Ano": 2024,
    },
]

resultado = carroAposAno(lista_carros)
for carro in resultado:
    print(carro)

# 21. Crie uma função chamada "inverterString" que recebe uma string como argumento e retorna a
# string invertida. Por exemplo, para a entrada "hello", a função deve retornar "olleh".


def inverterString(string):
    reversed_string = string[::-1]
    return reversed_string


string = input("Digite uma palavra ou frase: ")
print(f"A palavra ou frase invertida é: {inverterString(string)}.")
