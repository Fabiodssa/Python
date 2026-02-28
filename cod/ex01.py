n=input('DIGITE SEU NOME: ').strip()
i=input('Digite sua idade: ')
if  n and i:
    print(f'Seu nome é:{n}')
    print(f'seu nome ivnertido é:{n[::-1]}')
    
    if ' ' in n:
        print('seu nome tem espaço')
    else: 
        
        print('seu nome não tem espaço')
    print(f'seu nome tem {len(n)} letras')
        
    print('A primeira letra do seu nome é:',n[0])
    print( 'A ultima letra do seu nome é:',n[-1])
else:    
    print('Desculpe, você deixou campos vazio.')