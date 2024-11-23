# 1. Escreva um programa que leia um número inteiro e verifique se ele é positivo, negativo ou igual a
# zero.

num = int(input("Digite um número inteiro: "))

if num > 0:
    print("O número digitado é positivo.")
elif num < 0:
    print("O número digitado é negativo.")
else:
    print("O número digitado é igual a zero.")

# 2. Crie um programa que receba a idade de uma pessoa e exiba se ela é maior de idade ou menor de
# idade.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade")

# 3. Desenvolva um programa que leia dois números inteiros e mostre qual deles é o maior, ou se são
# iguais.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}.")
elif num1 < num2:
    print(f"{num1} é menor que {num2}.")
else:
    print(f"Os números {num1} e {num2} são iguais.")

# 4. Faça um programa que verifique se um número é par ou ímpar.

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print("O número digitado é par.")
else:
    print("O número digitado é ímpar.")

# 5. Elabore um programa que leia três notas de um aluno e calcule a média. Em seguida, exiba se o
# aluno está aprovado (média maior ou igual a 7) ou reprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("O aluno está aprovado.")
else:
    print("O aluno está reprovado.")

# 6. Crie um programa que receba o nome de duas pessoas e exiba qual delas possui o maior número
# de caracteres em seu nome.

pessoa1 = input("Digite o nome de uma pessoa: ")
pessoa2 = input("Digite o nome de outra pessoa: ")

if len(pessoa1) > len(pessoa2):
    print(f"O nome '{pessoa1}' é maior que '{pessoa2}'.")
elif len(pessoa1) < len(pessoa2):
    print(f"O nome '{pessoa1}' é menor que '{pessoa2}'.")
else:
    print(
        f"O nome '{pessoa1}' tem o mesmo número de caracteres que '{pessoa2}'."
    )

# 7. Desenvolva um programa que leia um caractere e verifique se ele é uma vogal ou uma consoante.

char = input("Digite uma letra: ").lower()
vogais = ['a', 'e', 'i', 'o', 'u']

if char in vogais:
    print("A letra digitada é uma vogal.")
else:
    print("A letra digitada é uma consoante.")

# 8. Faça um programa que receba três números e os imprima em ordem crescente.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite mais um número: "))

list = [num1, num2, num3]
list.sort()

for item in list:
    print(item)

# 9. Elabore um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa, dado o peso e
# a altura. Em seguida, exiba se a pessoa está abaixo do peso, com peso normal, com sobrepeso,
# obesa ou muito obesa.

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / altura**2

if imc < 18.5:
    imc_result = "peso baixo"
elif 18.5 <= imc < 25:
    imc_result = "peso normal"
elif 25 <= imc < 30:
    imc_result = "sobrepeso"
elif 30 <= imc < 35:
    imc_result = "obesidade grau I"
elif 35 <= imc < 40:
    imc_result = "obesidade grau II"
else:
    imc_result = "obesidade grau III"

print(
    f"""Você possui o peso {peso} e altura {altura}. O seu imc é {
        imc:.2f} e você está com {imc_result}."""
)

# 10. Escreva um programa que receba um número de mês (1 a 12) e exiba o nome do mês
# correspondente.

numero_mes = int(input("Digite o número do mês: "))
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
numero_mes = numero_mes - 1

print(f"O número digitado corresponde ao mês: {meses[numero_mes]}.")

# 11. Desenvolva um programa que leia o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.500,00, o aumento deve ser de 10%. Caso contrário, o aumento é de
# 15%.

salario = float(input("Digite o salário do funcionário: "))

if salario <= 1500:
    aumento = 1.15
else:
    aumento = 1.1

salario_novo = salario * aumento
print(f"O salário novo do funcionário, com o aumento, é: {salario_novo:.2f}.")

# 12. Receba um número inteiro do usuário e verifique se ele é divisível por 3 e por 5 ao mesmo tempo,
# exibindo uma mensagem apropriada.

num = int(input("Digite um número inteiro: "))

if num % 3 == 0 and num % 5 == 0:
    print("O número é divisível por 3 e 5 ao mesmo tempo.")
else:
    print("O número NÃO é divisível por 3 e 5 ao mesmo tempo.")

# 13. Peça ao usuário que insira o dia da semana (por extenso) e, em seguida, exiba uma mensagem
# informando se é um dia útil ou um fim de semana.

dia = input("Digite o dia da semana por extenso: ").lower()

dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
fim_de_semana = ['Sábado', 'Domingo']

if dia in dias_da_semana:
    print("É um dia da semana.")
else:
    print("É um dia do fim de semana.")

# 14. Elabore um programa que leia um número inteiro de 1 a 5 e exiba a mensagem "Muito bom",
# "Bom", "Regular", "Insuficiente" ou "Muito insuficiente", de acordo com o valor lido.

num = int(input("Digite um número de 1 a 5: "))
msgs = ['Muito bom', 'Bom', 'Regular', "Insuficiente", "Muito insuficiente"]
num = num - 1

print(msgs[num])

# 15. Peça ao usuário que digite um número entre 1 e 7 e exiba o dia da semana correspondente (1 -
# Domingo, 2 - Segunda-feira, etc.).

num = int(input("Digite um número de 1 a 7: "))
dias_da_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira',
                  'Quinta-feira', 'Sexta-feira', 'Sábado']
num_index = num - 1

print(num, "-", dias_da_semana[num_index])

# 16. Receba um número decimal do usuário e arredonde-o para o inteiro mais próximo usando a
# estrutura de controle try/except para tratar possíveis exceções.

try:
    dec = (float(input("Digite um número decimal: ")))
    dec = round(dec)
except ValueError:
    print("ERRO: Digite o número decimal em apenas dígitos.")

# 17. Peça ao usuário que insira a sua idade e verifique se ele é um bebê (0 a 1 ano), criança (1 a 12
# anos), adolescente (13 a 18 anos) ou adulto (mais de 18 anos).

idade = int(input("Digite a sua idade em dígitos: "))

if 0 < idade <= 1:
    print("Você é um bebê.")
if 2 < idade <= 12:
    print("Você é uma criança.")
if 13 < idade <= 17:
    print("Você é um adolescente.")
if idade > 17:
    print("Você é um adulto.")

# 18. Solicite ao usuário dois números inteiros e, com base na operação escolhida pelo usuário (1 - para
# soma, 2 - para subtração, 3 - para multiplicação ou 4 - para divisão), exiba o resultado da operação.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
operacao = int(input("""
Escolha uma operação:

[1] => Soma
[2] => Subtração
[3] => Multiplicação
[4] => Divisão

=> """))

if operacao == 1:
    print(num1 + num2)
if operacao == 2:
    print(num1 - num2)
if operacao == 3:
    print(num1 * num2)
if operacao == 4:
    print(num1 / num2)

# 19. Desenvolva um programa que leia o nome e a idade de uma pessoa. Utilize o bloco try/except para
# garantir que a idade digitada seja um valor inteiro válido.

nome = input("Digite o seu nome: ")
try:
    idade = int(input("Digite a sua idade: "))
except:
    print("ERRO: Digite uma idade válida (somente dígitos).")

# 20. Crie um programa que leia um valor em metros e o converta para centímetros, milímetros e
# quilômetros. Utilize o bloco try/except para lidar com possíveis exceções que possam vir a
# acontecer durante os cálculos.

try:
    distancia = float(input("Digite uma distância em metros: "))
except:
    print("Digite o valor da distância apenas em dígitos, usando um ponto em vez de vírgula para o ponto decimal.")

print(f"A distância em centímetros é: {
      distancia * 100}, em milímetros: {distancia * 1000} e em quilômetros: {distancia / 1000}.")
