import math

pi = 3.141592653589793

# Função Seno usando Série de Taylor com k=100
def seno(x, k=100):
    resultado = 0
    termo = x # Primeiro termo: n=0 -> x
    for n in range(k + 1):
        resultado += termo
        # Calcula o próximo termo a partir do atual:
        # termo_n+1 = termo_n * (-x^2) / ((2n+2)(2n+3))
        termo *= -x**2 / ((2*n + 2) * (2*n + 3))
    return resultado

def test_seno():
    test_cases = [0, pi/6, pi/4, pi/3, pi/2, pi, 3*pi/2, 2*pi]
    print(f"{'x':>10} | {'seno(x)':>20} | {'math.sin(x)':>20} | {'diff':>20}")
    print("-" * 75)
    for x in test_cases:
        my_sin = seno(x)
        lib_sin = math.sin(x)
        diff = abs(my_sin - lib_sin)
        print(f"{x:10.5f} | {my_sin:20.15f} | {lib_sin:20.15f} | {diff:20.15e}")

if __name__ == "__main__":
    test_seno()
