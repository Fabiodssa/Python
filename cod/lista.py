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

listab=lista.copy() #copia a lista
print('copia', listab)
print('----------------------------------------------')

##################################################################################

indices=range(len(frutas)) #mostras o indice de cada elemento da lista
for indice in indices:
    print(indice, frutas[indice])

print('----------------------------------------------')
#lista_enumerada=enumerate(frutas)    #outra foma de enumerar usando enumerate
for item in enumerate(frutas):
    print(item)

print('----------------------------------------------')

lista_enumerada=enumerate(frutas)       #outra foma de enumerar
print(list(lista_enumerada))

print('----------------------------------------------')

for item2 in enumerate(frutas):
    numero,nome=item2
    print(numero, nome)

print('----------------------------------------------')

for numero, nome in enumerate(frutas):
    print('lista bolada',numero, nome)

############################################################################################

print('----------------------------------------------')

nome1, nome2, nome3=['fabio', 'pedro', 'kreby'] #cria uma variavel para cada valor da lista
print(nome2)
print('----------------------------------------------')

nome1, nome2, nome3, *resto=['fabio', 'pedro', 'kreby', 'carra', 'falipe', 'lucas']
print(nome3, resto) #cria uma varavel para as que não tem uma expecifica
