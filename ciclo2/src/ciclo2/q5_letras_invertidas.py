"""
 Escreva uma função que:
a) Receba uma frase como parâmetro.
b) Retorne uma nova frase com cada palavra com as letras invertidas
"""

def inverter_letras(frase: str) -> str:
    """
    Recebe uma frase e retorna uma nova frase com cada palavra com as letras invertidas.
    """
    palavras = frase.split()
    p_letras_invertidas = [palavra[::-1] for palavra in palavras]
    return ' '.join(p_letras_invertidas)


if __name__ == "__main__":
    frase = input("Digite uma frase: ")
    frase_invertida = inverter_letras(frase)
    print(f"Frase com letras invertidas: {frase_invertida}")