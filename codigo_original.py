
import math
import time

import numpy as np


def es_primo_optimizado(numero):
    """Verifica si un número es primo revisando divisores hasta su raíz cuadrada."""
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    limite = int(math.sqrt(numero)) + 1

    for divisor in range(3, limite, 2):
        if numero % divisor == 0:
            return False

    return True


def obtener_primos_optimizado(limite_superior):
    """Obtiene números primos con comprensión de listas y función optimizada."""
    return [
        numero
        for numero in range(1, limite_superior + 1)
        if es_primo_optimizado(numero)
    ]


def obtener_primos_numpy(limite_superior):
    """Obtiene números primos usando NumPy y una criba booleana."""
    es_primo = np.ones(limite_superior + 1, dtype=bool)
    es_primo[:2] = False

    for numero in range(2, int(np.sqrt(limite_superior)) + 1):
        if es_primo[numero]:
            es_primo[numero * numero::numero] = False

    return np.flatnonzero(es_primo)


inicio = time.time()
primos_optimizado = obtener_primos_optimizado(100000)
fin = time.time()

print(f"Cantidad de números primos encontrados: {len(primos_optimizado)}")
print(f"Tiempo optimizado con raíz cuadrada: {fin - inicio:.6f} segundos")

inicio = time.time()
primos_numpy = obtener_primos_numpy(100000)
fin = time.time()

print(f"Cantidad de números primos encontrados con NumPy: {len(primos_numpy)}")
print(f"Tiempo optimizado con NumPy: {fin - inicio:.6f} segundos")
