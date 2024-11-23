altura = float(input("Digite quanto você tem de altura: "))
peso = float(input("Digite quanto você tem de peso: "))

if altura < 1.2 and peso < 60:
    print("A sua classificação é: A.")
elif 1.2 <= altura <= 1.7 and peso < 60:
    print("A sua classificação é: B.")
elif altura > 1.7 and peso < 60:
    print("A sua classificação é: C.")
elif altura < 1.2 and 60 <= peso <= 90:
    print("A sua classificação é: D.")
elif 1.2 <= altura <= 1.7 and 60 <= peso <= 90:
    print("A sua classificação é: E.")
elif altura > 1.7 and 60 <= peso <= 90:
    print("A sua classificação é: F.")
elif altura < 1.2 and peso > 90:
    print("A sua classificação é: G.")
elif 1.2 <= altura <= 1.7 and peso > 90:
    print("A sua classificação é: H.")
elif altura > 1.7 and peso > 90:
    print("A sua classificação é: I.")
