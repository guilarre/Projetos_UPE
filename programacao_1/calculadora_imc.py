peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / altura**2

if imc < 18.5:
    imc_result = "baixo peso"
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
    f"Você possui o peso {peso} e altura {altura}. O seu imc é {
        imc:.2f} e você está em {imc_result}."
)
