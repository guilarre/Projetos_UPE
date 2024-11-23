from datetime import datetime

# 1. Implemente o código do slide de número 6.

num = input("Insira um número: ")

print("Você inseriu:", num)
print("Tipo de dado de num:", type(num))

# 2. Implemente o código do slide de número 11.

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = int(num1) + int(num2)
print(resultado)

# 3. Implemente o código do slide de número 14.

print("Programiz é " + "incrível.")

# 4. Solicite ao usuário seu nome e imprima uma mensagem de boas-vindas na tela.

nome = input("Insira seu nome: ")
print(f"Olá, {nome}, seja bem-vindo.")

# 5. Peça ao usuário que digite sua idade em texto (por exemplo, "18") e converta-a em um número
# inteiro.

idade = int(input("Insira sua idade: "))

# 6. Receba um número inteiro do usuário e converta-o em um número decimal (float).

inteiro = float(input("Insira um número inteiro: "))

# 7. Peça ao usuário para digitar dois números inteiros e exiba a soma deles.

numero1 = input("Digite um número inteiro: ")
numero2 = input("Digite outro número inteiro: ")
resultado = int(num1) + int(num2)

print("A soma desses números é:", resultado)

# 8. Receba um número decimal do usuário e calcule o seu quadrado.

numero_dec = float(input("Insira um número decimal: "))
quadrado_dec = numero_dec**2
print(f"O quadrado deste número é: {quadrado_dec}.")

# 9. Peça ao usuário que insira o seu ano de nascimento e, em seguida, exiba a sua idade.

ano_nascimento = int(input("Insira o seu ano de nascimento: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

print("Sua idade é:", idade)

# 10. Peça ao usuário que digite seu primeiro nome e seu sobrenome separadamente. Em seguida,
# concatene-os em uma única string e exiba o nome completo.

primeiro_nome = input("Insira seu primeiro nome: ")
sobrenome = input("Insira seu sobrenome: ")

print("Seu nome completo é: " + primeiro_nome + " " + sobrenome)

# 11. Solicite ao usuário uma sequência de números separados por espaço e exiba quantos números
# foram digitados.

numeros = input("Digite uma sequência de números separados por espaço: ")
numeros_strip = numeros.replace(" ", "")
print("Você digitou", len(numeros_strip), "números.")

# 12. Receba o nome de um animal digitado pelo usuário e exiba uma mensagem informando qual
# animal foi digitado.

animal = input("Digite o nome de um animal: ")
print(f"O animal digitado foi: {animal}.")

# 13. Peça ao usuário que digite o seu nome e o seu sobrenome. Em seguida, exiba o nome completo
# invertido (sobrenome, nome).

primeiro_nome2 = input("Insira seu primeiro nome: ")
sobrenome2 = input("Insira seu sobrenome: ")

print(sobrenome2, primeiro_nome2)

# 14. Receba uma string digitada pelo usuário e imprima o seu tamanho (número de caracteres).

frase = input("Escreva uma frase: ")
print(f"Sua frase contém {len(frase)} caracteres.")

# 15. Solicite ao usuário um número inteiro e exiba se ele é par ou ímpar.

numero3 = int(input("Digite um número inteiro: "))

if numero3 % 2 == 0:
    print("O número digitado é par.")
else:
    print("O número digitado é ímpar.")

# 16. Receba um número inteiro digitado pelo usuário e verifique se ele é positivo ou negativo.

numero4 = int(input("Digite um número inteiro: "))

if numero4 > 0:
    print("O número digitado é positivo.")
elif numero4 == 0:
    print("O número digitado é neutro.")
else:
    print("O número digitado é negativo.")

# 17. Peça ao usuário que insira dois números e exiba o maior deles.

primeiro_num = int(input("Digite um número: "))
segundo_num = int(input("Digite outro número: "))

if primeiro_num > segundo_num:
    print(f"O número {primeiro_num} é o maior.")
elif primeiro_num == segundo_num:
    print(f"Os números digitados são iguais.")
else:
    print(f"O número {segundo_num} é o maior.")

# 18. Receba a altura e o peso de uma pessoa digitados pelo usuário. Em seguida, calcule o seu índice de
# massa corporal (IMC) utilizando a fórmula: IMC = peso / (altura * altura) e exiba o resultado.

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / altura**2

if imc < 25:
    imc_result = "peso ideal"
elif 25 < imc < 30:
    imc_result = "sobrepeso"
else:
    imc_result = "obesidade"

print(
    f"Você possui o peso {peso} e altura {altura}. O seu imc é {imc} e você está em {imc_result}."
)

# 19. Peça ao usuário que digite o seu nome e verifique se ele contém mais de 5 caracteres utilizando a
# função.

nome2 = input("Digite seu nome: ")

if len(nome2) > 5:
    print("Seu nome contém mais de 5 caracteres.")
else:
    print("Seu nome contém 5 caracteres ou menos.")


# 20. Solicite ao usuário que insira o seu estado civil e exiba uma mensagem apropriada (por exemplo:
# "Você é casado(a)", "Você é solteiro(a)", etc.).

estado_civil = input("Digite o seu estado civil: ")
print(f"Você é {estado_civil}.")

# 21. Receba a base e a altura de um retângulo digitados pelo usuário. Em seguida, calcule a sua área e
# exiba o resultado.

b = float(input("Digite o tamanho da base do retângulo: "))
h = float(input("Digite o tamanho da altura do retângulo: "))
a = b * h

print(f"A área do retângulo é: {a}.")

# 22. Peça ao usuário que digite a sua cidade e verifique se ela começa com a letra "S" (ou outra letra de
# sua escolha).

cidade = input("Digite o nome da sua cidade: ")

if cidade[0] == "S" or cidade[0] == "s":
    print("O nome da sua cidade começa com a letra 'S'.")
else:
    print("O nome da sua cidade não começa com a letra 'S'.")

# 23. Solicite ao usuário que insira dois números decimais e calcule o resto da divisão entre eles.

numero_1 = float(input("Digite um número decimal: "))
numero_2 = float(input("Digite outro número decimal: "))

resto = numero_1 % numero_2
print(f"O resto da divisão entre esses números é: {resto}")

# 24. Solicite ao usuário um número decimal e converta-o em um número inteiro.

num_convertido = int(float(input("Digite um número decimal: ")))
print(f"O número convertido para inteiro é: {num_convertido}.")

# 25. Receba uma string contendo um número inteiro e some 10 a esse número, convertendo-o
# novamente para uma string antes de exibi-lo.

string = input("Digite um número inteiro: ")
numero_convertido = int(string)
num_novo = numero_convertido + 10
string_novamente = str(num_novo)

print(f"O número novo é: {string_novamente}")

# 26. Solicite ao usuário que digite uma data no formato "dd/mm/aaaa" e extraia o dia, o mês e o ano
# separadamente, convertendo-os em números inteiros.

data = input("Digite uma data no formato 'dd/mm/aaaa': ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

print(f"Dia: {dia}, mês: {mes}, ano: {ano}.")

# 27. Receba o nome de uma cidade do usuário e concatene-o com o nome do estado para formar uma
# mensagem completa, como "Você mora em [cidade], [estado].".

cidade_usuario = input("Digite o nome da sua cidade: ")
estado_usuario = input("Digite o nome do seu estado: ")

print("Você mora em " + cidade_usuario + ", " + estado_usuario + ".")

# 28. Solicite ao usuário que insira seu ano de nascimento e concatene-o com uma mensagem de
# boas-vindas, como "Bem-vindo ao nosso programa, nascido em [ano de nascimento]!".

ano_de_nascimento = input("Insira o seu ano de nascimento: ")
print("Bem-vindo ao nosso programa, nascido em " + ano_de_nascimento + "!")

# 29. Receba um número inteiro e uma string do usuário. Em seguida, concatene-os em uma única
# string, separando-os com um espaço.

inteiro2 = input("Digite um número: ")
frase2 = input("Digite uma frase: ")

print(inteiro2, frase2)

# 30. Receba o nome de um produto digitado pelo usuário e concatene-o com o preço do produto,
# adicionando o símbolo de moeda da sua escolha.

produto = input("Digite o nome de um produto: ")
preco = input("Digite o preço do produto: ")
print(produto + " R$" + preco)

# 31. Receba um número inteiro do usuário e concatene-o com uma mensagem, informando o dobro
# desse número.

numero_int = int(input("Digite um numero inteiro: "))
numero_x2 = numero_int * 2
print("O dobro desse número é: " + str(numero_x2))

# 32. Receba uma string contendo um endereço de e-mail e concatene-a com uma mensagem de
# agradecimento personalizada.

email = input("Digite seu email: ")
msg = "Obrigado por entrar em contato, "
print(msg + email + ".")

# 33. Receba dois números inteiros do usuário e exiba a soma, a diferença, o produto e o quociente
# (divisão inteira) entre eles.

primeiro_numero = int(input("Digite um número inteiro: "))
segundo_numero = int(input("Digite outro número inteiro: "))

print(
    f"A soma dos números é: {primeiro_numero + segundo_numero}, a diferença é: {primeiro_numero - segundo_numero}, o produto é: {primeiro_numero * segundo_numero} e o quociente (da divisão inteira) é: {primeiro_numero // segundo_numero}."
)

# 34. Peça ao usuário para digitar a base e a altura de um triângulo. Em seguida, calcule e exiba a área do
# triângulo.

b2 = float(input("Digite o tamanho da base do triângulo: "))
h2 = float(input("Digite o tamanho da altura do triângulo: "))
a2 = (b2 * h2) / 2

print(f"A área do triângulo é: {a2}.")

# 35. Receba o raio de uma circunferência digitado pelo usuário e calcule o seu perímetro (2 * π * raio).

r = float(input("Digite o raio da circunferência: "))
print(f"O perímetro da circunferência é: {2 * 3.14 * r}.")

# 36. Receba a base e a altura de um retângulo digitados pelo usuário. Em seguida, calcule e exiba o
# perímetro do retângulo.

b3 = float(input("Digite o tamanho da base do retângulo: "))
h3 = float(input("Digite o tamanho da altura do retângulo: "))
print(f"O perímetro do retângulo é: {2 * (b3 + h3)}.")

# 37. Solicite ao usuário que insira três números decimais. Em seguida, calcule e exiba a média
# aritmética desses números.

dec1 = float(input("Digite um número decimal: "))
dec2 = float(input("Digite outro número decimal: "))
dec3 = float(input("Digite mais um número decimal: "))

print(f"A média aritmética desses números é: {(dec1 + dec2 + dec3) / 3}.")

# 38. Peça ao usuário para digitar a sua idade e, em seguida, informe quantos meses e quantos dias ele já
# viveu (considerando um ano com 365 dias).

idade2 = int(input("Digite sua idade: "))
print(
    f"Você já viveu pelo menos {idade2 * 12} meses e {idade2 * 365} dias nesses {idade2} anos."
)

# 39. Receba um valor em reais e a cotação do dólar digitados pelo usuário. Em seguida, converta o valor
# para dólares e exiba o resultado.

valor = float(input("Insira um valor em reais: "))
dolar = float(input("Insira o valor da cotação atual do real em dólares: "))
print(f"O valor convertido para dólares é: {valor * dolar}.")

# 40. Solicite ao usuário para digitar um número decimal e arredonde-o para o inteiro mais próximo.

num_dec = float(input("Digite um número decimal: "))
print(f"O inteiro mais próximo é: {round(num_dec)}.")

# 41. Receba três números inteiros digitados pelo usuário e exiba o resultado da operação (n1 + n2) * n3.

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = int(input("Digite mais um número inteiro: "))

print((n1 + n2) * n3)

# 42. Peça ao usuário que digite uma temperatura em graus Celsius e a converta para Fahrenheit usando
# a fórmula: Fahrenheit = (Celsius * 9/5) + 32.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"A temperatura em Fahrenheit é: {fahrenheit} ºF.")
