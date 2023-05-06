import os

ask = ""
mensaje = ""

valor1 = 0
valor2 = 0
suma = 0
resta = 0
out = 0


def subtraction_art_ascii():

    print("______             _     ")
    print("| ___ \           | |    ")
    print("| |_/ /  ___  ___ | |_   __ _ ")
    print("|    /  / _ \/ __|| __| / _` |")
    print("| |\ \ |  __/\__ \| |_ | (_| |")
    print("\_| \_| \___||___/ \__| \__,_|")

    return ""


def addition_art_ascii():
    print(" _____ ")
    print("/  ___|")
    print("\\ `--.  _   _  _ __ ___    __ _ ")
    print(" `--. \| | | || '_ ` _ \  / _` |")
    print("/\\__/ /| |_| || | | | | || (_| |")
    print("\\____/  \\__,_||_| |_| |_| \\__,_|")

    return ""


def message():
    os.system("cls")

    print("              _               _         _ ")
    print("             | |             | |       | |")
    print("  ___   __ _ | |  ___  _   _ | |  __ _ | |_   ___   _ __")
    print(" / __| / _` || | / __|| | | || | / _` || __| / _ \ | '__|")
    print("| (__ | (_| || || (__ | |_| || || (_| || |_ | (_) || |")
    print(" \___| \__,_||_| \___| \__,_||_| \__,_| \__| \___/ |_|")
    print("\n")

    print("1 |------------> Suma")
    print("2 |------------> Resta \n")


def input_valores():
    try:
        return float(input("Ingrese valor 1: ")),  float(input("Ingrese valor 2: "))
    except ValueError:
        print("Ingrese un número")
        return input_valores()


def options():
    try:
        ask = int(input("Selecione una opcion: "))

        if ask > 2 or ask < 1:
            raise Exception
        else:
            return ask
    except ValueError:
        print("Ingrese un número")

        return options()

    except Exception:

        print(f"No se encontró la opcion {ask}, ingrese una válida")
        return options()


def addition(element1):

    valor1 = element1[0]
    valor2 = element1[1]
    suma = valor1 + valor2
    return suma


def subtraction(element1):

    valor1 = element1[0]
    valor2 = element1[1]
    resta = valor1 - valor2
    return resta


mensaje = message()
ask = options()

os.system("cls")

print(addition_art_ascii() if ask == 1 else subtraction_art_ascii())

valores = input_valores()

match ask:
    case 1:

        out = addition(valores)

        print(f"El resultado es {out}")

    case 2:

        out = subtraction(valores)

        print(f"El resultado es {out}")
