# Author: Jesus Emiliano Reyes Gomez
# Id: 4668974
# Maestria Big Data, UAG
# Date: 21/02/2024
# Description: Backtraking Sudoku

class Nodo:
    def __init__(self, nivel, valor, peso, incluidos):
        self.nivel = nivel
        self.valor = valor
        self.peso = peso
        self.incluidos = incluidos 
        self.cota = 0 

def cota_superior(nodo, capacidad, objetos):
    if nodo.peso >= capacidad:
        return 0
    else:
        cota = nodo.valor
        peso_total = nodo.peso
        for i in range(nodo.nivel, len(objetos)):
            if peso_total + objetos[i][1] <= capacidad:
                peso_total += objetos[i][1]
                cota += objetos[i][0]
            else:
                cota += (capacidad - peso_total) * (objetos[i][0] / objetos[i][1])
                break
        return cota

def insertar_ordenado(cola, nodo):
    cola.append(nodo)
    cola.sort(key=lambda x: x.cota, reverse=True)

def ramificacion_y_poda(objetos, capacidad):
    objetos.sort(key=lambda x: x[0]/x[1], reverse=True)
    cola_prioridad = []
    nodo_inicial = Nodo(0, 0, 0, [])
    mejor_valor = 0
    mejor_solucion = []
    insertar_ordenado(cola_prioridad, nodo_inicial)

    while cola_prioridad:
        nodo_actual = cola_prioridad.pop(0)  #Extraemos el primer elemento
        if nodo_actual.nivel < len(objetos):
            for i in [1, 0]: #revisar rama con objeto incluido y luego sin él
                nuevo_incluidos = nodo_actual.incluidos.copy()
                nuevo_valor = nodo_actual.valor
                nuevo_peso = nodo_actual.peso
                if i == 1:  #validar si se incluye
                    nuevo_peso += objetos[nodo_actual.nivel][1]
                    nuevo_valor += objetos[nodo_actual.nivel][0]
                    nuevo_incluidos.append(nodo_actual.nivel+1)
                if nuevo_peso <= capacidad and nuevo_valor > mejor_valor:#Validar si la solucion es mejor y si cabe en la mochila
                    mejor_valor = nuevo_valor
                    mejor_solucion = nuevo_incluidos
                nuevo_nodo = Nodo(nodo_actual.nivel + 1, nuevo_valor, nuevo_peso, nuevo_incluidos)
                nuevo_nodo.cota = cota_superior(nuevo_nodo, capacidad, objetos)
                if nuevo_nodo.cota > mejor_valor: #Validar si la cota es mejor que el mejor valor
                    insertar_ordenado(cola_prioridad, nuevo_nodo)

    return mejor_valor, mejor_solucion

objetos = [(79, 85), (32, 26), (47, 48), (18, 21), (26, 22), (85, 95), (33, 43), (40, 45), (45, 55), (59, 52)]
capacidad = 101

mejor_valor, mejor_solucion = ramificacion_y_poda(objetos, capacidad)
print("Mejor valor:", mejor_valor)
print("Objetos en la mochila:", mejor_solucion)
