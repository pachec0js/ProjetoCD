pi = 3.141592653589793


def numeroeuler(n):
    total = 0

    for pedaco in range(n):
        fatorialAtual = 1
        for i in range(1, pedaco + 1):
            fatorialAtual *= i
        expressao = 1 / fatorialAtual
        total += expressao

    return total


print(numeroeuler(100))
