def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("Dividir() deve receber apenas argumentos inteiros")
    try:
        aux = dividendo / divisor
    except:
        print(f"Não foi possível dividir {dividendo} por {divisor}")
        raise
    return aux


def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f"O resultado da divisão de 10 por {divisor} é {resultado}")


# try:
#     testa_divisao(2.5)
# except AttributeError as error:
#     print(error.__class__.__bases__)
# except ZeroDivisionError as error:
#     print(error.__class__.__bases__)
# except TypeError as error:
#     print(error)

try:
    print("O fluxo está aqui")
    raise ValueError
except Exception:
    print("Agora o fluxo veio pra ca")
print("E enfim ele continua...")
print("Programa encerrado.")
