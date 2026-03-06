numero=1
while numero <= 10:
    print(numero)
    numero=numero+1
    
print('-----------------------------------------------------')
    
for num in range(1,11):
    if num>=6:
        break
    print(num)
    
print('-----------------------------------------------------')

for nume in range(1,11):
    if nume==5:
        continue
    print(nume)
    
print('-----------------------------------------------------')

frutas=['MAÇA', 'banana', 'cereja', 'abacate', 'morango', 'melão', 'banana', 'banana']
cont=0
for fru in frutas:
    if fru=='banana':
        cont+=1
    
print(f'quantidade de bananas na lista: {cont}')