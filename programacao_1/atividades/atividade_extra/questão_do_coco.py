cliente = int(
    input(
        """
Escolha o tipo de cliente:

[1] = Cliente normal
[2] = Cliente especial

=> """
    )
)

qtd_coco = int(input("\nDigite a quantidade de cocos a serem vendidos: "))

if cliente == 2:
    modificador = 0.8
else:
    modificador = 1

if qtd_coco > 10:
    valor_coco = 2
else:
    valor_coco = 2.5

valor_final = qtd_coco * valor_coco * modificador
print(f"\nO cliente deve pagar: R${valor_final:.2f}")
