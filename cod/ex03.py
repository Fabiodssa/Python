

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