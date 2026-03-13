sa='sim'
while sa != 'sair':
    n1=float(input('Digite um valor: '))
    o=input('Escolha um operador: ')
    n2=float(input('Digite outro valor: '))
    if o =='+':
        print(f'A soma é:{n1+n2}')
    elif o == '-':
        print(f'A subtração é: {n1-n2} ')
    elif o == '*':
        print(f'A multiplicação é: {n1*n2}')
    elif o == '/':
        print(f'A divisão é: {n1/n2}')
    else:
        print('Operação invalida')

    sa=input("Deseja sair da calculadora? digite 'sim' para sair ")