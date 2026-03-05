pi = 3.141592653589793
k = 100

def radiano(x):
    return x * pi / 180


def cosseno(x):
    cos = 0
    
    for pedaco in range(k):
        fatorialAtual = 2 * pedaco
        
        termo = (-1) ** pedaco
        
        for i in range(1, fatorialAtual + 1):
            termo = termo * x / i
        
        cos += termo

    return cos


def exponencial(x, k=100):
    resultado = 1.0 
    termo = 1.0
    
    for n in range(1, k):
        termo *= x / n   
        resultado += termo
    
    return resultado

print(f"e^{5} = {exponencial(5):.6f}")

def numeroeuler(n):
    total = 0

    for pedaco in range(n):
        fatorialAtual = 1
        for i in range(1, pedaco + 1):
            fatorialAtual *= i
        expressao = 1 / fatorialAtual
        total += expressao

    return total
