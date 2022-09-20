"""
funciones
"""
from numeros import *


def obtien_opcion():
    print("[1] Ingresa 1 si viene a perfumeria.")
    print("[2] Ingresa 2 si viene a farmacia.")
    print("[3] Ingresa 3 si viene a cosmeticos.")
    print("[4] Terminar.")
    area = input("Ingresa una opcion: ")
    return area


@function_decoradora
def imprimirTurno(saludo):
    print(saludo)


generadorPerfumeria = turno_perfumeria()
generadorFarmacia = turno_farmacia()
generadorCosmeticos = turno_cosmeticos()

while True:
    area = obtien_opcion()
    if area == '1':
        texto = next(generadorPerfumeria)
        imprimirTurno(texto)
    if area == '2':
        texto = next(generadorFarmacia)
        imprimirTurno(texto)
    if area == '3':
        texto = next(generadorCosmeticos)
        imprimirTurno(texto)
    if area == '4':
        break
