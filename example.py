def dividir(dividendo, divisor):
    # print(divisor.resultado)
    return dividendo / divisor


def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f"O resultado da divisão de 10 por {divisor} é {resultado}")


try:
    testa_divisao(0)
except AttributeError as error:
    print(error.__class__.__bases__)
    print("Erro de atributo tratado.")
except ZeroDivisionError as error:
    print(error.__class__.__bases__)
    print("Erro de divisão pro 0 tratado.")
except TypeError as error:
    print(error.__class__.__bases__)
    print("Erro de divisão por string tratado.")
print("Programa encerrado.")
