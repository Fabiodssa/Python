frutas=['MAÇA', 'banana', 'cerela', 'abacate', 'morango', 'melão']
print(frutas)
print(f'A primeira futa é: {frutas[0]}')
print(f'A ultima futa é: {frutas[-1]}')

frutas[1:3]= 'caju', 'jaca' # substitue na lista, idice 1 e 2
print(f'--------------------- {frutas}-------------')

frutas[1]= 'umbu'
frutas.append('caja') # salva no final da lista
print(f'--------------------- {frutas}-------------')

frutas.insert (5,'tamara') # insere
print(f'--------------------- {frutas}-------------')

frutas.remove('abacate') # remove da lista
print(f'--------------------- {frutas}-------------')

del frutas[-1] # deleta o ultimo da lista
print(f'--------------------- {frutas}-------------')

lista=[10,20,30,40]
lista.append(50) #adiciona ao final da lista
print(lista)

lista.pop() #remove do final da lista
lista.append(60)
print(lista)
