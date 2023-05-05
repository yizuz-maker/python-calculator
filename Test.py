def addition(valor1, valor2):
    suma = valor1 + valor2
    return suma


def subtraction(valor1, valor2):
    resta = valor1 + valor2
    return resta


print("Python Calculator")
print("------------------")
print("1------------Suma")
print("2------------Resta \n")

ask = int(input("Selecione una opcion: "))

match ask:
    case 1:
        print("-----Suma-----")
        valor1 = int(input("Ingrese valor 1: "))
        valor2 = int(input("Ingrese valor 2: "))
        out = addition(valor1, valor2)

        print(f"El resultado es {out}")

    case 2:
        print("-----Resta-----")
        valor1 = int(input("Ingrese valor 1: "))
        valor2 = int(input("Ingrese valor 2: "))
        out = subtraction(valor1, valor2)

        print(f"El resultado es {out}")
