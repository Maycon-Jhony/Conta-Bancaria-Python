menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        saldo += valor_deposito
        extrato += f'Depósito de R$ {valor_deposito:.2f}\n'

    elif opcao == "s":
        if numero_saque < LIMITE_SAQUE:
            valor_saque = float(input("Digite o valor do saque: R$ "))
            if valor_saque <= limite:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato += f'Saque de R$ {valor_saque:.2f}\n'
                    numero_saque += 1
                else:
                    print("Saldo insuficiente.")
            else:
                print(f"Limite máximo por saque é de R$ {limite:.2f}.")
        else:
            print("Limite diário de saques atingido.")

    elif opcao == "e":
        print("Extrato:")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
