
def duplica(numero):
    du = numero * 2
    return du  

def triplica(numero):
    tri = numero * 3
    return tri

def quadripica(numero):
    qua = numero * 4
    return qua
n=10
print(duplica((n)))
print(triplica((n)))
print(quadripica((n)))


print('-------------------------------------------------------')

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(10)) # 20
print(triplicar(10))
print(quadruplicar(10))