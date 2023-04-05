def calcularIndiceDeMasaCorporal(p,a):
    return p/a**2

def obtener_valor_float(mensaje):
    while True:
        valor_str = input(mensaje)
        try:
            valor_float = float(valor_str)
            return valor_float
        except ValueError:
            print("Ingrese un valor float")


def main():
    peso = obtener_valor_float("Ingrese su peso en Kg: ")
    altura = obtener_valor_float("Ingrese su altura en metros: ")
    indice=calcularIndiceDeMasaCorporal(p,a)
    print(f"Tu índice de masa corporal es: {indice:.2f}")

if __name__ == "__main__":
    main()
