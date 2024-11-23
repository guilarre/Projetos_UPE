idade = None
maiores_18 = []
contador_todas_idades = 0

while idade != 0:
    idade = int(input("Digite uma idade: (se desejar parar, digite 0.)"))
    if 0 < idade < 120:
        pass
    else:
        print("Você deve apenas inserir idades positivas e num intervalo plausível (entre 1 e 120 anos).")
        erro = True
        break

    if idade >= 18:
        maiores_18.append(idade)

    contador_todas_idades += 1

print(f"Foram digitadas {contador_todas_idades} idades no total.")

# erro quando dividir por 0, correção:
if not erro == True:
    print(f"A média das idades de 18 anos ou mais é: {
          sum(maiores_18) / len(maiores_18)}.")
    print(f"A diferença entre a maior e a menor idade do grupo de 18 anos ou mais é: {
          max(maiores_18) - min(maiores_18)}")
