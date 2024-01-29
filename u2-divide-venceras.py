# Author: Jesus Emiliano Reyes Gomez
# Id: 4668974
# Maestria Big Data, UAG
# Date: 29/01/2024
# Description: Divide y venceras algoritmo

# Steps:
# [] Dividir el problema en subproblemas a menor escala pero de la misma naturaleza
# [] Conquistar los subproblemas resolviendolos recursivamente
# [] Combinar las soluciones de los subproblemas para resolver problemas mayores

# Ejercicio n-enisimo numero de fibonacci
# Matriz inicial 2x2 = [[0,1],[1,1]]^n

inicial = [[0,1],[1,1]]

#Funcion para multiplicar matrices

def multiplicar(a,b):
    c = [[0,0],[0,0]] # Inicializar matriz de resultado
    c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    return c

def potencia(a, n):
    if n == 0:
        return [[1,0],[0,1]] # Matriz de identidad 2x2 ^0
    if n == 1:
        return a
    # Aplicamos exponenciacion rapida
    if n % 2 == 0:
        # Aplicamos recursividad
        return potencia(multiplicar(a,a), n//2)
    else:
        return multiplicar(a, potencia(multiplicar(a,a), (n-1)//2))
    
def fibonacci(n):
    resultado = 'No existe el numero de fibonacci'
    if n < 0:
        return resultado
    else:
        resultado = potencia(inicial, n)
        return resultado[0][1]
    
# Ejercicio exponenciación rápida

def exponenciacion_rapida(a, n):
    print(a,n)
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 0:
        # Aplicamos recursividad
        return exponenciacion_rapida(a*a, n//2)
    else:
        return a * exponenciacion_rapida(a*a, (n-1)//2)
    
# Funcion de menu
def menu():
    opt = input('1. Fibonacci \n2. Exponenciacion rapida \n3. Salir \n')
    while opt != '3': # terminar hasta que el usuario lo indique
        if opt == '1':
            n = int(input('Ingrese el numero de fibonacci: '))
            print(fibonacci(n))
        elif opt == '2':
            a = int(input('Ingrese la base: '))
            n = int(input('Ingrese el exponente: '))
            print(exponenciacion_rapida(a,n))
        else:
            print('Opcion no valida')
        opt = input('1. Fibonacci \n2. Exponenciacion rapida \n3. Salir \n')
    print('Hasta luego')

menu()