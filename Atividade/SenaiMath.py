

def exponencial(x, k=100):
    resultado = 1.0 
    termo = 1.0
    
    for n in range(1, k):
        termo *= x / n   
        resultado += termo
    
    return resultado

print(f"e^{5} = {exponencial(5):.6f}")