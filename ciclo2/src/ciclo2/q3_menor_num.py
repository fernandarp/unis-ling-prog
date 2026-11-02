"""
Faça um programa que leia 3 números inteiros e mostre o menor deles.
"""

if __name__ == "__main__":
    a = int(input("Digite o valor de A (inteiro): "))
    b = int(input("Digite o valor de B (inteiro): "))
    c = int(input("Digite o valor de C (inteiro): "))

    menor = min(a, b, c)

    print(f"O menor número entre {a}, {b} e {c} é: {menor}")
