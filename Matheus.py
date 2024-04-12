from scipy.integrate import quad

valor_inicial = 50000
porcentagem = 0.1
vida_util = 8
valor_residual = valor_inicial * porcentagem
depreciacao_anual = (valor_inicial - valor_residual) / vida_util

def equad(x):
    return depreciacao_anual * x / vida_util

result, error = quad(equad, 0, 6)

print(f"o resultado da depreciação acumulada:{result}")