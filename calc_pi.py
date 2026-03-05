def calcular_pi(k):
    soma = 0

    for n in range(k):

        numerador = (-1) ** n

        denominador = (2 * n) + 1 

        formula = numerador / denominador

        soma += formula

    pi_final = 4 * soma

    return pi_final

k = 1000
resultado_pi = calcular_pi(k)
print(f"O valor de Pi calculado é: {resultado_pi:.5f}")
