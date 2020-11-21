#script que calcula la tabla de multiplicar de un numero
#solicita numero al usuario
numero = input('que numero quieres multiplicar?')
#conviertes de texto a numero
numero = int(numero)
#imprimir tipo de dato
print(type(numero))
print(f'A continuacion se muestra la table de multiplicar del numero {numero}')
print(f'----------------------------------------------------------------------')

for n in range(10):
    res = (n+1) * numero
    print(f'-> {numero} * {n+1} = {res}')
 