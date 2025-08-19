def impares(limite):
    for ip in range(1, limite + 1):
        if ip % 2 == 1:
            yield ip

gen = impares(50)
print(list(gen))
