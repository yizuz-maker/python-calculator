from os import system

ask = ""
valor1 = 0
valor2 = 0
out = 0

# La funcion toma valores depurados


def message():
    system.cls()
    print("Python Calculator")
    print("------------------")
    print("1------------Suma")
    print("2------------Resta \n")


def addition(valor1, valor2):
    suma = valor1 + valor2
    return suma


def subtraction(valor1, valor2):
    resta = valor1 + valor2
    return resta


message()

while True:
    try:
        ask = int(input("Selecione una opcion: "))

        if ask > 2 or ask < 1:
            raise Exception

        else:
            break
    except ValueError:
        print("Ingrese un número")

    except Exception:
        print(
            f"No se encontró la opcion {ask}, ingrese una válida")


match ask:
    case 1:
        print("\n")
        print("-----Suma-----")
        valor1 = int(input("Ingrese valor 1: "))
        valor2 = int(input("Ingrese valor 2: "))
        out = addition(valor1, valor2)

        print(f"El resultado es {out}")

    case 2:
        print("\n")
        print("-----Resta-----")
        valor1 = int(input("Ingrese valor 1: "))
        valor2 = int(input("Ingrese valor 2: "))
        out = subtraction(valor1, valor2)

        print(f"El resultado es {out}")
