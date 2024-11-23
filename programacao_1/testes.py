# 9. Faça um programa para gerenciar uma agenda de contatos. Para cada contato armazene o nome, o
# telefone e o aniversário (dia e mês). O programa deve permitir:
# a. Inserir contato;
# b. Remover contato;
# c. Pesquisar um contato pelo nome;
# d. Listar todos os contatos;
# e. Listar os contatos cujo nome inicia com uma dada letra;
# f. Imprimir os aniversariantes do mês.

# Sempre que o programa for encerrado, os contatos devem ser armazenados em um arquivo binário.

# Quando o programa iniciar, os contatos devem ser inicializados com os dados contidos neste
# arquivo binário.

with open('./teste.txt', 'wb') as file:
    texto = bytearray("oi isso é um teste.", encoding='utf-8')
    file.write(texto)
