# deposito, apenas valor inteiro e positivo, deve ficar armazenado registro para extrato
# saque, permite apenas 3 saques diarios com limite maximo de 500 por saque, caso limite seja inferior, informe mensagem, deve registrar retirada para extrato.
# extrato, lista todas as operacoes e o saldo atual no formato R$ xxxx.xx

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def formatar_moeda(valor):
    return f"R$ {valor:.2f}".replace('.', ',')


def saque(valor):
    global saldo, numero_saques, extrato
    if numero_saques >= LIMITE_SAQUES:
        print("Você atingiu o limite máximo de saques diários.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor de saque excede o limite de R$ 500.")
    elif valor < 0:
        print(
            "Valor de saque inválido. Apenas valores inteiros e positivos são permitidos.")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"- Saque: {formatar_moeda(valor)}\n"


def deposito(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"+ Depósito: {formatar_moeda(valor)}\n"
    else:
        print("Valor de depósito inválido. Apenas valores inteiros e positivos são permitidos.")


def mostrar_extrato():
    print("=== Extrato ===")
    print(extrato if extrato else "Nenhuma operação realizada.")
    print(f"Saldo: {formatar_moeda(saldo)}")


menu = """
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
"""

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = int(input("Valor do depósito: "))
        deposito(valor)

    elif opcao == "s":
        valor = int(input("Valor do saque: "))
        saque(valor)

    elif opcao == "e":
        mostrar_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
