saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'
usuarios = []
contas = []

def menu():
    return '''
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
=> '''

def criar_usuario(usuarios):
    cpf = int(input('Digite o CPF: (Somente números): '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuário com este CPF!')
    else:
        nome = str(input('Digite o seu nome: '))
        data_nascimento = str(input('Data de Nascimento: '))
        endereco = str(input('Digite seu endereço: Ex:(logradouro, nro  - bairro - cidade/sigla estado)'))

        usuarios.append({'nome':nome, 'data_nascimento': data_nascimento,'cpf':cpf,'endereco':endereco})

        print('Usuário cadastrado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input('Informe o CPF do usuário: '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print('Usuario não encontrado!')

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def consultar_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(linha)


while True:

    opcao = input(menu())

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)
        # if valor > 0:
        #     saldo += valor
        #     extrato += f"Depósito: R$ {valor:.2f}\n"
        #
        # else:
        #     print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "e":
        consultar_extrato()
        # print("\n================ EXTRATO ================")
        # print("Não foram realizadas movimentações." if not extrato else extrato)
        # print(f"\nSaldo: R$ {saldo:.2f}")
        # print("==========================================")

    elif opcao == 'nu':

        criar_usuario(usuarios)

    elif opcao == 'nc':
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == 'lc':
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")