saldo = 1000

print("Bem-vindo ao banco!")
print("1-Saque\n2-Deposito\n3-Saldo\n4-Sair")

while True:
    comando = input("Qual operação você deseja realizar?\n")

    if comando == "1":
        valor_saque = input("Qual valor do saque?\n")
        saque = int(valor_saque)  # Convertendo a entrada para inteiro
        if saque > saldo:
            print("Saldo insuficiente\n")
        else:
            saldo -= saque  # Subtrai o valor do saque do saldo
            print(f"Saque realizado com sucesso! Saldo atual: {saldo}")


    if comando == "2":
        valor_deposito = input("Qual valor do deposito?\n")
        deposito = int(valor_deposito)

        saldo += deposito
        print(f"Deposito realizado com sucesso! Saldo atual: {saldo}")


    if comando == "3":
        print(f"Seu saldo é: {saldo}")

    if comando == "4":
        break