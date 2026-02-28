n=input('Digite seu nome: ')
i=input('Digite o ano do seu nascimento: ')
g=input('Digite quanto deseja gastar: ')

try:
    ii=int(i)
    gf=float(g)
    print(f'Bem vindo {n} você tem {2026-ii} anos e irá gastar R$:{gf} em nossa loja')
except: print('Digite apenas numeros')