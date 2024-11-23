# def criarFrases(frase, vezes):
#     for i in range(vezes):
#         print(frase)


# frase = input("Qual frase você deseja criar? ")
# vezes = int(input("Quantas vezes devo repeti-la? "))
# criarFrases(frase, vezes)

####################################################

# def soma(num1: float, num2: float): # especificar o tipo nos parâmetros pra acessar métodos
#     resultado = num1 + num2
#     return resultado
#     print("outro código")  # não executa pq tá depois do return


# soma(5, 4)
# result = soma(num2=6, num1=6)
# print(result)

####################################################

# def find_square(num):
#     result = num * num
#     return result


# square = find_square(3)

# print('Square:', square)

####################################################

# Função para calcular IMC

def calcularIMC(peso, altura):
    imc = peso / altura ** 2

    if imc < 18.5:
        imc_result = "baixo peso"
        return imc, imc_result
    elif 18.5 <= imc < 25:
        imc_result = "peso normal"
        return imc, imc_result
    elif 25 <= imc < 30:
        imc_result = "sobrepeso"
        return imc, imc_result
    else:
        imc_result = "obesidade"
        return imc, imc_result


peso = float(input("Digite o seu peso (em kg, por ex. 60): "))
altura = float(input("Digite a sua altura (em metros, por ex.: 1.65): "))
imc, imc_result = calcularIMC(peso, altura)

print(
    f"Você possui o peso {peso} e altura {altura}. O seu imc é {
        imc:.2f} e você está em {imc_result}."
)
