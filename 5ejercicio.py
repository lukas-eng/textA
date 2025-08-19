def inverso(lista):
    for e in reversed(lista):
        yield e
        
paises = input("""Ingrese 3 paises:
""")
for r in inverso(paises):
    print(r)