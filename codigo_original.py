
import time


def es_primo_original(numero):
    """Verifica si un número es primo usando un método no optimizado."""
    if numero < 2:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True


inicio = time.time()
primos_originales = []

for numero in range(1, 100001):
    if es_primo_original(numero):
        primos_originales.append(numero)

fin = time.time()

print(f"Cantidad de números primos encontrados: {len(primos_originales)}")
print(f"Tiempo de ejecución código original: {fin - inicio:.6f} segundos")
