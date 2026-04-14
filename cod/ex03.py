

def multi(n1,n2,n3):
    return n1*n2*n3

def PorI(resultado):
    if resultado%2 == 0:
        return "O resultado é par: "
    else: 
       return "O resultado é impar: "

resultado = multi(1, 2, 3)
print(resultado)

pi=PorI(resultado)
print(pi)

print("--------------------------------------------------------")

def multiAll(*args):
    total = 1
    for numero in args: 
        total *= numero
    return total

resu = multiAll(10, 20, 100)
print(resu)

print("----------------------------------------------------")

def saudacao(msg):
    sau="seja bemvindo"
    return msg + sau

print(saudacao('olá mundo!'))


print("----------------------------------------------------")

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome} !'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz' ]:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))