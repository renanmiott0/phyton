saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    menu = """
    Menu:
    d - Depósito
    s - Saque
    e - Extrato
    q - Sair
    Escolha uma opção: 
    """

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Valor de depósito inválido. O valor deve ser positivo.")

    elif opcao == "s":
        if numero_saques < LIMITES_SAQUES:
            valor_saque = float(input("Informe o valor do saque: R$ "))
            if valor_saque > 0 and valor_saque <= limite and valor_saque <= saldo:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
            else:
                print("Saque inválido. Verifique o valor, o limite diário e o saldo disponível.")
        else:
            print("Você atingiu o limite diário de saques.")

    elif opcao == "e":
        print("\nExtrato da conta:")
        if extrato:
            print(extrato)
        else:
            print("Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}\n")

    elif opcao == "q":
        print("Saindo do sistema.")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
