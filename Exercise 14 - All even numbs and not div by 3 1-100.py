#Exercício 14:
#Imprima todos os números pares e não divisíveis por 3 de 1 a 100

for contador in range (1,101,+1):
    if contador %2==0 and contador %3!=0 :
        print(contador)
