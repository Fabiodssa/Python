while True:
    n1 = input('Digite um número: ')
    o = input('Digite o operador (+-/*): ')
    n2 = input('Digite outro número: ')

    numeros_validos = None

    try:
        n1_f = float(n1)
        n2_f = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if o not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(o) > 1:
        print('Digite apenas um operador.')
        continue

    if o =='+':
        print(f'A soma é:{n1_f+n2_f}')
    elif o == '-':
        print(f'A subtração é: {n1_f-n2_f} ')
    elif o == '*':
        print(f'A multiplicação é: {n1_f*n2_f}')
    elif o == '/':
        print(f'A divisão é: {n1_f/n2_f}')
    else:
        print('Operação invalida')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break