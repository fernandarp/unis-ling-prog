"""
Faça um programa que leia a idade de uma pessoa expressa em dias e
mostre-a expressa em anos, meses e dias.
"""

def decompor_idade(idade_dias: int) -> tuple[int, int, int]:
    """Decompor a idade em anos, meses e dias.
    Foi assumido que um ano tem 365 dias e um mês tem 30 dias.
    """
    anos = idade_dias // 365
    meses = (idade_dias % 365) // 30
    dias = (idade_dias % 365) % 30
    return anos, meses, dias

if __name__ == "__main__":
    idade = int(input("Digite a sua idade em dias: "))
    anos, meses, dias = decompor_idade(idade)
    print(f"Sua idade decomposta é: {anos} anos, {meses} meses e {dias} dias")