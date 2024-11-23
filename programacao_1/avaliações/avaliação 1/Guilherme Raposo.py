## Programação 1 - Atividade 1
## Aluno: Guilherme Raposo Gonçalves de Melo Larré

# Questão 3

def questao_3():
    total = 142
    representantes = 18
    fracao = 0.04

    lotes_para_cada_representante = round(total * fracao)
    lotes_restantes_para_prefeitura = total - (lotes_para_cada_representante * representantes)

    print(f"\nCada pessoa receberá {lotes_para_cada_representante} lotes.")
    print(f"Restarão {lotes_restantes_para_prefeitura} lotes.")


# Questão 4

def questao_4():
    valor_total = float(input("\nOlá, insira o valor total da compra: "))

    desconto_10 = valor_total * 0.9
    parcela_3x = valor_total / 3
    comissao_compra_a_vista = desconto_10 * 0.05
    comissao_compra_parcelada = valor_total * 0.05

    print(f"""    
a. O total a pagar com desconto de 10% é: R${desconto_10:.2f};
b. O valor de cada parcela, no parcelamento de 3x sem juros é: R${parcela_3x:.2f};
c. A comissão do vendedor, no caso de a venda ser à vista é (5% sobre o valor com desconto): R${comissao_compra_a_vista:.2f};
d. A comissão do vendedor, no caso de a venda ser parcelada (5% sobre o valor total) é: R${comissao_compra_parcelada:.2f}.

Obrigado por usar nosso sistema.""")

#########################################################################################

msg_menu = """
## Escolha qual resposta deseja visualizar:
[3] => Resposta para a questão 3
[4] => Resposta para a questão 4

=> """

while True:
    escolha = input(msg_menu)
    
    if escolha == "3":
        questao_3()
        continue
    if escolha == "4":
        questao_4()
        continue