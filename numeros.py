"""
Generadores y decoradores
"""


def function_decoradora(funcion):
    """
    es un decorador para envolver el turno en un saludo predeterminado
    """

    def texto_generado(texto):
        print("--------------")
        print("Su turno es:")
        funcion(texto)
        print("Aguarde y \nsera atendido")
        print("--------------")

    return texto_generado


def turno_perfumeria():
    """
    retorna un turno nuevo para el area de perfumeria
    :return: un string con el turno nuevo para el cliente
    """
    numero = 0
    while True:
        numero += 1
        yield 'P-' + str(numero)


def turno_farmacia():
    """
    retorna un turno nuevo para el area de farmacia
    :return: un string con el turno nuevo para el cliente
    """
    numero = 0
    while True:
        numero += 1
        yield 'F-' + str(numero)


def turno_cosmeticos():
    """
    retorna un turno nuevo para el area de cosmeticos
    :return: un string con el turno nuevo para el cliente
    """
    numero = 0
    while True:
        numero += 1
        yield 'C-' + str(numero)
