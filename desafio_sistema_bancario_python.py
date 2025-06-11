menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 

while True:

    opcao = input(menu).strip().lower()[0]

    if opcao == 'd':
        deposito = float(input('Quanto deseja depositar? '))
        
        if deposito <= 0:
            print("Operação falhou! O Valor informado é inválido!")
        else:
            print(f"Deposito efetuado no valor de R$ {deposito:.2f}")
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
    
    elif opcao == 's':
        while numero_saques < LIMITE_SAQUES:
            saque = float(input('Quanto deseja sacar? Limite de R$500 por saque: R$'))

            if saldo <= 0:
                print('Operação falhou! Não tem saldo suficiente!')
                break
            else:
                if saque > 500 or saque > saldo:
                    print('Operação falhou! Saque acima do limite permitido.')
                    break
                else:
                    print(f"Saque no valor de R$ {saque:.2f} efetuado!")
                    saldo -= saque
                    numero_saques += 1
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    print(f'{numero_saques}/3 saque diário realizado!')
                    break
        
        if numero_saques == LIMITE_SAQUES:
            print(f'Limite de saques diário atingido. {numero_saques}')
            
                   

    elif opcao == 'e':
        print('============== EXTRATO ==================')
        print('Não foram realizados movimentações.' if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        
    elif opcao == 'q':
        print(" Até logo! ".center(20, '#'))
        break
    
    else:
        print("Operação inválida, por favor selecione novamente uma operação desejada.")
