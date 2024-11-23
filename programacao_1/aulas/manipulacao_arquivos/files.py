# arquivo = open("aulas/manipulacao_arquivos/meu_arquivo.txt",
#                'a', encoding='utf-8')

# name = "Guilherme"
# arquivo.write(f"Olá, {name}\n")
# arquivo.close()

################################

# arquivo = open("aulas/manipulacao_arquivos/meu_arquivo.txt",
#                'r', encoding='utf-8')

# print(arquivo.read())
# arquivo.close()

################################

# Usa-se o with ... as ... pro arquivo ser fechado automaticamente:

with open("aulas/manipulacao_arquivos/meu_arquivo.txt", 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
