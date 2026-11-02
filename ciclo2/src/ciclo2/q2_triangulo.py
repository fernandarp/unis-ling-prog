"""
Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam ou
não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso os
valores formem um triângulo, calcular e escrever a área deste triângulo. Se não
formam triângulo escrever os valores lidos. (Se a > b + c não formam triângulo
algum, se a é o maior)
"""

import math


def eh_triangulo(a: int, b: int, c: int) -> bool:
    """
    Verifica se os lados a, b e c podem formar um triângulo.
    Assumiu-se que os valores lidos são inteiros e positivos
    """
    return (a + b) > c and (a + c) > b and (b + c) > a

def area_triangulo(a: int, b: int, c: int) -> float:
    """
    Calcula a área de um triângulo.
    """
    semiperimetro = (a + b + c) / 2
    return math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))  # noqa: E501
  

if __name__ == "__main__":
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))

    if eh_triangulo(a, b, c):
        area = area_triangulo(a, b, c)
        print(f"Os lados formam um triângulo. A área é: {area:.2f}")
    else:
        print(f"Os lados não formam um triângulo. Lados informados: {a}, {b}, {c}")
