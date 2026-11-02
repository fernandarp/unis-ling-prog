"""
 Implementar uma função que retorne verdadeiro se o número for primo
(falso caso contrário). Testar de 1 a 100.
"""
import math


def eh_primo(n: int) -> bool:
    """
    Verifica se um número é primo.
    Um número é considerado primo se for maior que 1 e não tiver divisores além de 1 
    e ele mesmo.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # noqa: SIM110
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    for i in range(1, 101):
        if eh_primo(i):
            print(f"{i} é primo.")