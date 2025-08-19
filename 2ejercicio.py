cadena = input("""Escribe una palabra :):
""")

def separar_letras(palabra):
     for letra in palabra:
         yield letra

for letra in separar_letras(cadena):
    print(letra)