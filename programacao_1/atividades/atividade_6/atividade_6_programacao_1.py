# 1. Faça um programa que exiba os números de 1 a 10 em ordem crescente.

for i in range(1, 11):
    print(i)

# 2. Crie um programa que exiba os números de 10 a 1 em ordem decrescente.

for i in reversed(range(1, 11)):
    print(i)

# 3. Elabore um programa que calcule a soma dos números de 1 a 100.

soma = 0
for i in range(1, 101):
    soma += i

print(soma)

# 4. Desenvolva um programa que exiba todos os números pares de 1 a 50.

for i in range(2, 51, 2):
    print(i)

# 5. Faça um programa que calcule o produto dos números de 1 a 5.

lista = []
produto = 1

for i in range(1, 6):
    lista.append(i)

for item in lista:
    produto = produto * item

print(produto)

# 6. Crie um programa que exiba a tabuada do 7.

for i in range(1, 11):
    print(7 * i)

# 7. Elabore um programa que calcule a média de 5 notas digitadas pelo usuário.

notas = []
soma = 0

for i in range(5):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    soma += nota

media = soma / len(notas)
print(media)

# 8. Desenvolva um programa que exiba todos os múltiplos de 3 no intervalo de 1 a 50.

lista = []
for i in range(1, 51):
    lista.append(i)

multiplos_3 = []
for item in lista:
    if item % 3 == 0:
        multiplos_3.append(item)

print(multiplos_3)

# 9. Crie um programa que leia 10 números do usuário e exiba o maior e o menor valor digitado.

lista_numeros = []

for i in range(10):
    numero_digitado = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero_digitado)

print(f"O menor número é: {min(lista_numeros)}")
print(f"O maior número é: {max(lista_numeros)}")

# 10. Faça um programa que exiba os números ímpares de 1 a 100.

lista_impares = []
for i in range(1, 101):
    if i % 2 != 0:
        lista_impares.append(i)

print(lista_impares)

# 11. Crie um programa que leia 5 notas de alunos e exiba quantos deles foram aprovados (nota maior
# ou igual a 7).

lista_aprovados = []
for i in range(5):
    nota = float(input(f"Digite uma nota do {i+1}º aluno: "))
    if nota >= 7:
        lista_aprovados.append(nota)

print(f"Foram aprovados {len(lista_aprovados)} alunos.")

# 12. Faça um programa que exiba a soma dos dígitos de um número inteiro fornecido pelo usuário.

numero = input("Digite um número inteiro: ")
soma = 0
for digito in numero:
    soma += int(digito)
print(soma)

# 13. Elabore um programa que leia um número inteiro e exiba todos os seus divisores.

lista_divisores = []
numero = int(input("Digite um número inteiro: "))
for i in range(1, numero + 1):
    if numero % i == 0:
        lista_divisores.append(i)

print(f"O número {numero} é divisível por: {str(lista_divisores)[1:-1]}.")

# 14. Desenvolva um programa que calcule a média da altura de 5 pessoas.

soma = 0
for i in range(5):
    soma += float(input(f"Digite a altura da {i+1}ª pessoa: "))

print(f"A média das alturas digitadas é: {soma/5}.")

# 15. Faça um programa que exiba os números de 1 a 100, substituindo os múltiplos de 3 pela palavra
# "Fizz" e os múltiplos de 5 pela palavra "Buzz". Para os números que são múltiplos de ambos,
# utilize a palavra "FizzBuzz".

lista_numeros = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, 'Fizz')
    elif i % 3 == 0:
        print(i, 'Buzz')
    elif i % 5 == 0:
        print(i, 'FizzBuzz')
    else:
        print(i)

# 16. Elabore um programa que leia um número inteiro e exiba a soma dos dígitos pares desse número.

numero = input("Digite um número inteiro: ")
soma = 0
for digito in numero:
    if int(digito) % 2 == 0:
        soma += int(digito)
print(f"A soma dos dígitos pares desse número é: {soma}.")

# 17. Faça um programa que leia um número inteiro e exiba o número invertido. Por exemplo, se o
# número lido for 123, o programa deve exibir 321.

numero = input("Digite um número inteiro: ")
print(numero[::-1])
