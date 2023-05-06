import os

ask = ""
valor1 = 0
valor2 = 0
out = 0


def message():
    os.system("cls")
    print("Python Calculator")
    print("------------------")
    print("1------------Suma")
    print("2------------Resta \n")


def input_valores():
    try:
        return float(input("Ingrese valor 1: ")),  float(input("Ingrese valor 2: "))
    except ValueError:
        print("Ingrese un número")
        return input_valores()


def addition(element1):

    valor1 = element1[0]
    valor2 = element1[1]
    suma = valor1 + valor2
    return suma


def subtraction(element1):
    resta = valor1 - valor2
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
        print(f"No se encontró la opcion {ask}, ingrese una válida")

valores = input_valores()

match ask:
    case 1:
        os.system("cls")
        print("-----Suma-----")

        out = addition(valores)

        print(f"El resultado es {out}")

    case 2:
        os.system("cls")
        print("-----Resta-----")

        out = subtraction(valores)

        print(f"El resultado es {out}")
