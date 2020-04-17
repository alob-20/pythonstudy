print('Calculadora')
print()

while True:
    num_1 = float(input('Digite um valor: '))
    num_2 = float(input('Digite outro valor: '))
    operacao = input('Digite a operação desejada: ')

    if operacao == '+': print(num_1 + num_2)
    elif operacao == '-': print(num_1 - num_2)
    elif operacao == '/': print(num_1 / num_2)
    elif operacao == '*': print(num_1 * num_2)

    sair = input('Deseja finalizar? ')
    lista = ['Sim', 'sim', 'S', 's']
    if sair in lista:
        break

    print()



