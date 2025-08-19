def tab_multiplicar(num, limite = 10):
    for n in range (1, limite + 1):
        yield f" {num} * {n} = {num * n}"

numero = int(input("""¿Que tabla de multiplicar quieres ver?
"""))
for fila in tab_multiplicar(numero):
    print(fila)