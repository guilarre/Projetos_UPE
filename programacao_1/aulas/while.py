# O bloco 'while' possui 'else'

# counter = 0
# while counter < 3:
#     print("Inside loop")
#     counter += 1
# else:
#     print("Inside else")


# Se parado por um 'break', não executa o 'else'

counter = 0
while counter < 3:
    if counter == 1:
        break

    print("Inside loop")
    counter += 1
else:
    print("Inside else")
