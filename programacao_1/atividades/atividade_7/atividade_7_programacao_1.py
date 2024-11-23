# 1. Enumere as diferenças entre os comandos "for" e "while".

resposta = "O 'for' itera sobre um objeto iterável (como uma lista, por exemplo), ou seja, o número de vezes que o código é repetido vai depender do tamanho do objeto e não é necessário implementar uma condição de parada. Já o 'while' repete o código indefinidamente. Para limitar o número de vezes que o código é repetido, devemos implementar um contador ou uma condição qualquer de parada."
print(resposta)

# 2. Descreva em quais circunstâncias os comandos "for" e "while" devem ser empregados.

resposta = "O 'for' deve ser empregado quando temos um objeto a ser iterado. É útil especialmente para realizarmos operações ou análises com objetos muito grandes (listas, dicionários, tabelas ou arquivos diversos), pois o código será repetido até que o objeto chegue ao fim. Já o 'while' deve ser usado quando não há um objeto específico a ser iterado e temos a necessidade de repetir o código indefinidamente até que uma condição de parada seja atingida. Por exemplo, para a seleção de opção em um menu principal, onde o usuário digita a opção desejada, é levado ao procedimento desejado, e depois retorna para o menu principal, repetindo esse ciclo até que deseje sair do programa."
print(resposta)

# 3. Escreva um programa que exiba os números de 1 a 10 em ordem crescente utilizando o while.

num = 1
while num <= 10:
    print(num)
    num += 1

# 4. Crie um programa que exiba os números de 10 a 1 em ordem decrescente utilizando o while.

num = 10
while num >= 1:
    print(num)
    num -= 1

# 5. Elabore um programa que calcule a soma dos números de 1 a 100 utilizando o while.

soma = 0
num = 1
while num <= 100:
    soma += num
    num += 1
print(soma)

# 6. Faça um programa que calcule o produto dos números de 1 a 5 utilizando o while.

produto = 1
num = 1
while num <= 5:
    produto *= num
    num += 1
print(produto)

# 7. Crie um programa que exiba a tabuada do 9 utilizando o while.

num = 1
while num <= 10:
    print(9 * num)
    num += 1

# 8. Crie um programa que leia uma sequência de números inteiros do usuário e exiba o maior e o
# menor valor digitado. O programa deve parar de ler quando o usuário digitar o número 0
# utilizando o while.

numero = int(input("Digite um número inteiro (digite 0 se desejar parar): "))
menor_num = None
maior_num = 0

while numero != 0:
    if menor_num == None:
        menor_num = numero
    elif numero < menor_num:
        menor_num = numero
    if numero > maior_num:
        maior_num = numero
    numero = int(
        input("Digite um número inteiro (digite 0 se desejar parar): "))

print(f"O maior número digitado foi {maior_num} e o menor foi {menor_num}.")

# 9. Crie um programa que leia uma sequência de números inteiros do usuário e exiba a média dos
# números digitados. O programa deve parar de ler quando o usuário digitar o número -1 utilizando
# o while.

lista_numeros = []
numero = int(input("Digite um número inteiro (digite -1 se desejar parar): "))
while numero != -1:
    lista_numeros.append(numero)
    numero = int(
        input("Digite um número inteiro (digite -1 se desejar parar): "))

print(f"A média entre os números digitados é: {
      sum(lista_numeros) / len(lista_numeros)}.")

# 10. Faça um programa que leia um número inteiro e exiba a soma dos seus dígitos elevados ao cubo
# utilizando o while.

soma_digitos = 0
num = input("Digite um número inteiro: ")
for digito in num:
    cubo = int(digito) ** 3
    soma_digitos += cubo

print(soma_digitos)

# 11. Faça um programa que exiba os números ímpares de 1 a 100 utilizando o while.

num = 1
lista_impares = []
while num <= 100:
    if num % 2 != 0:
        lista_impares.append(num)
    num += 1

print(lista_impares)

# 12. Desenvolva um programa que exiba todos os múltiplos de 3 no intervalo de 1 a 50 utilizando o
# while.

num = 1
lista_multiplos_3 = []
while num != 50:
    if num % 3 == 0:
        lista_multiplos_3.append(num)
    num += 1

print(lista_multiplos_3)

# 13. Crie um programa que leia 5 notas de alunos e exiba quantos deles foram aprovados (nota maior
# ou igual a 7) utilizando o while.

count = 0
count_aprovados = 0
while count != 5:
    numero = int(input("Digite a nota: "))
    if numero >= 7:
        count_aprovados += 1
    count += 1

print(f"Foram aprovados {
      count_aprovados} alunos com nota igual ou maior que 7.")

# 14. Elabore um programa que leia uma sequência de números inteiros do usuário e determine
# quantos números pares foram digitados antes do primeiro número ímpar. O programa deve parar
# de ler quando o usuário digitar o número 0 utilizando o while.

lista_numeros = []
numero = int(input("Digite um número inteiro (digite 0 se desejar parar): "))

while numero != 0:
    lista_numeros.append(numero)
    numero = int(
        input("Digite um número inteiro (digite 0 se desejar parar): "))

count_pares = 0
for num in lista_numeros:
    if num % 2 == 0:
        count_pares += 1
    else:
        break

print("Foram digitados", count_pares, "números pares antes do primeiro ímpar.")

# 15. Crie um programa que leia uma sequência de números inteiros do usuário e exiba quantos
# números pares e quantos números ímpares foram digitados. O programa deve parar de ler quando
# o usuário digitar o número 0 utilizando o while.

count_pares = 0
count_impares = 0

numero = int(input("Digite um número inteiro (digite 0 se desejar parar): "))
while numero != 0:
    if numero % 2 == 0:
        count_pares += 1
    else:
        count_impares += 1
    numero = int(
        input("Digite um número inteiro (digite 0 se desejar parar): "))

print(f"Você digitou {count_pares} números pares e {
      count_impares} números ímpares.")

# 16. Faça um programa que leia uma sequência de números inteiros do usuário e exiba quantos
# números são divisíveis por 2, quantos são divisíveis por 3 e quantos são divisíveis por 5. O
# programa deve parar de ler quando o usuário digitar o número 0 utilizando o while.

count_2 = 0
count_3 = 0
count_5 = 0

numero = int(input("Digite um número inteiro (digite 0 se desejar parar): "))
while numero != 0:
    if numero % 2 == 0:
        count_2 += 1
        print(f"{numero} é divisível por 2")

    # condições seguintes sem usar elif pra caso seja divisível por mais de um primo
    if numero % 3 == 0:
        count_3 += 1
        print(f"{numero} é divisível por 3")
    if numero % 5 == 0:
        count_5 += 1
        print(f"{numero} é divisível por 5")
    numero = int(
        input("Digite um número inteiro (digite 0 se desejar parar): "))

print(f"Você digitou {count_2} números divisíveis por 2, {
      count_3} números divisíveis por 3 e {count_5} números divisíveis por 5.")

# 17. Desenvolva um programa que leia uma sequência de números inteiros do usuário e exiba a média
# dos números divisíveis por 3. O programa deve parar de ler quando o usuário digitar o número 0
# utilizando o while.

divisiveis_por_3 = []
numero = int(input("Digite um número inteiro (digite 0 se desejar parar): "))
while numero != 0:
    if numero % 3 == 0:
        divisiveis_por_3.append(numero)
    numero = int(
        input("Digite um número inteiro (digite 0 se desejar parar): "))

media = sum(divisiveis_por_3) / len(divisiveis_por_3)
print(media)

# 18. Faça um programa que leia uma sequência de números inteiros do usuário e exiba quantos
# números possuem mais de três dígitos. O programa deve parar de ler quando o usuário digitar o
# número 0 utilizando o while.

numeros_maiores_de_tres = []
numero = input("Digite um número inteiro (digite 0 se desejar parar): ")
while numero != '0':
    numeros_maiores_de_tres.append(numero)
    numero = input("Digite um número inteiro (digite 0 se desejar parar): ")

count = 0
for num in numeros_maiores_de_tres:
    if len(num) > 3:
        count += 1
print(count)

# 19. Desenvolva um programa que leia uma sequência de números inteiros do usuário e exiba a média
# dos números que estão entre 50 e 100. O programa deve parar de ler quando o usuário digitar o
# número 0 utilizando o while.

numeros_para_media = []
numero = int(input("Digite um número inteiro (digite 0 se desejar parar): "))
while numero != 0:
    if 50 <= numero <= 100:
        numeros_para_media.append(numero)
    numero = int(
        input("Digite um número inteiro (digite 0 se desejar parar): "))

print(f"A média dos números entre 50 e 100 que foram digitados é: {
      sum(numeros_para_media) / len(numeros_para_media)}.")

# 20. Elabore um programa que leia uma sequência de números inteiros do usuário e exiba o menor
# valor digitado que seja positivo e ímpar. O programa deve parar de ler quando o usuário digitar o
# número 0 utilizando o while.

numero = int(input("Digite um número inteiro (digite 0 se desejar parar): "))
if numero > 0:
    menor_impar_pos = numero
elif numero == 0:
    print("Você fechou o programa.")

while numero != 0:
    numero = int(
        input("Digite um número inteiro (digite 0 se desejar parar): "))
    if numero < menor_impar_pos and numero % 2 != 0:
        menor_impar_pos = numero

print(f"O menor número positivo e ímpar digitado foi: {menor_impar_pos}")

# 21. Faça um programa que leia uma sequência de números inteiros do usuário e exiba quantos
# números são pares e quantos números são ímpares entre o primeiro e o último número digitado.
# O programa deve parar de ler quando o usuário digitar o número 0 utilizando o while.

numeros_pares = 0
numeros_impares = 0
numero = int(input("Digite um número inteiro (digite 0 se desejar parar): "))
while numero != 0:
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
    numero = int(
        input("Digite um número inteiro (digite 0 se desejar parar): "))

print(f"Você digitou {numeros_pares} números pares e {
      numeros_impares} números ímpares.")
