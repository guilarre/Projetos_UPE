preco_antigo = float(input("Digite o preço antigo do produto: "))

if preco_antigo <= 50:
    aumento = 1.05
elif 50 < preco_antigo <= 100:
    aumento = 1.1
elif preco_antigo > 100:
    aumento = 1.15

preco_novo = preco_antigo * aumento
print(f"O preço novo é: {preco_novo}.")

if preco_novo <= 80:
    print("O preço novo é barato!")
elif 80 < preco_novo <= 120:
    print("O preço novo é normal!")
elif 120 < preco_novo <= 200:
    print("O preço novo é caro!")
elif preco_novo > 200:
    print("O preço novo é muito caro!")
