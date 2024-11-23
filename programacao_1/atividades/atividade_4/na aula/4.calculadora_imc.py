nome = input("Digite o seu nome: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso/altura**2

if imc > 25:
    imc_result = "peso ideal"
elif 25 < imc < 30:
    imc_result = "sobrepeso"
else:
    imc_result = "obesidade"
    
print(f"{nome}, você possui o peso {peso} e altura {altura}. O seu imc é {imc} e você está em {imc_result}.")