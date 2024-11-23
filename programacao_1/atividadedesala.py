# 1. Defina uma variável chamada "alunos". Adicione a ela 5 itens.
# Cada item representa o nome de cada aluno.

# Faça uma estrutura de repetição que percorre sobre a lista. Procure um aluno específico na lista.
# Se for encontrado, interrompa a estrutura de repetição.

alunos = ["guilherme", "hugo", "márcio", "elias", "lucas"]
search_str = input("Digite qual aluno deseja procurar: ").lower()

# indice = 0

# for aluno in alunos:
#     indice += 1
#     if aluno == search_str:
#         print(f"Encontrado: {aluno.title()} no índice {indice}.")
#         break
#     else:
#         continue

for indice, aluno in enumerate(alunos):
    if aluno == search_str:
        print(f"Encontrado: {aluno.title()} no índice {indice}.")
        break
    else:
        continue


# 24/10
# Crie um programa que simule um jogo de adivinhação. O programa deve gerar um número aleatório entre 1 e 100, e o usuário deve tentar adivinhar esse número. O programa deve dar dicas ao usuário, indicando se o palpite é maior ou menor que o número gerado. O jogo continua até que o usuário adivinhe o número correto.
# Twist: sem geração de num aleatório, colega do lado digita o número a ser adivinhado e vc dá um número p programa dar dicas.

numero_definido = int(
    input("Digite um número de 1 a 100 para o seu colega adivinhar: "))
numero_tentativa = 0
while numero_tentativa != numero_definido:
    numero_tentativa = int(input("Tente adivinhar o número escolhido: "))
    if numero_tentativa > numero_definido:
        print("O número é menor que esse.")
    elif numero_tentativa < numero_definido:
        print("O número é maior que esse.")
print("Parabéns, você acertou o número!")
