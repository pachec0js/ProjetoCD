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

