def fibonacci(limite):
    a, b  = 0, 1
    for _ in range(limite):
        yield a
        a, b = b, a + b

limite = int(input("Cuantos numeros quieres ver de Fibonacci?"))
for num in fibonacci(limite):
    print(num)