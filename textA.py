def generador_primos():
    """Genera números primos indefinidamente"""
    
    def es_primo(n):
        if n <= 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while True:
        if es_primo(num):
            yield num
        num += 1

# Ejemplo de uso
primos = generador_primos()

# Obtener los primeros 10 números primos
print("Los primeros 10 números primos:")
for i in range(10):
    print(next(primos))

print("\nSiguientes 5 números primos:")
for i in range(5):
    print(next(primos))