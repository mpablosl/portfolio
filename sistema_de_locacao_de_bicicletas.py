from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

bicicletas = [
    {"codigo": "B001", "tipo": "Urbana", "disponivel": True},
    {"codigo": "B002", "tipo": "Mountain Bike", "disponivel": True},
    {"codigo": "B003", "tipo": "Elétrica", "disponivel": True},
    {"codigo": "B004", "tipo": "Infantil", "disponivel": True},
    {"codigo": "B005", "tipo": "Speed", "disponivel": True}
]
usuarios = [
    {"cpf": "11111111111", "nome": "Ana Souza", "idade": 28, "telefone": "11999990001", "endereco": "Rua A, 123 - São Paulo/SP"},
    {"cpf": "22222222222", "nome": "Bruno Lima", "idade": 35, "telefone": "11999990002", "endereco": "Rua B, 456 - São Paulo/SP"},
    {"cpf": "33333333333", "nome": "Carla Mendes", "idade": 42, "telefone": "11999990003", "endereco": "Rua C, 789 - São Paulo/SP"},
    {"cpf": "44444444444", "nome": "Daniel Torres", "idade": 19, "telefone": "11999990004", "endereco": "Rua D, 321 - São Paulo/SP"},
    {"cpf": "55555555555", "nome": "Eduarda Ribeiro", "idade": 30, "telefone": "11999990005", "endereco": "Rua E, 654 - São Paulo/SP"}
]
historico = []

def nova_bicicleta(bicicletas):
    print('=== Cadastrar NOVA BICICLETA ===\n')
    codigo = str(input('Código: ')).strip().upper()
    bike_existe = bicicleta_existe(codigo, bicicletas)

    if bike_existe:
        print(f'"{codigo}" = JÁ EXISTE ESSA BICICLETA REGISTRADA!')
        return
    
    tipo = str(input('Tipo (Urbana / Mountain Bike / Elétrica / Infantil / Speed): '))
    disponivel = True
    
    bicicletas.append({
        "codigo":codigo,
        "tipo":tipo,
        "disponivel":disponivel
    })

    print('SUCESSO! Bicicleta cadastrada!')

def bicicleta_existe(codigo, bicicletas):
    encontrar_bicicleta = [bicicleta for bicicleta in bicicletas if bicicleta['codigo'] == codigo]
    return encontrar_bicicleta[0] if encontrar_bicicleta else None

def listar_bicicletas(bicicletas):
    
    print('Código\t        Tipo   \t\t\t\t\t           Status')
    for bicicleta in bicicletas:
        print(f'{bicicleta['codigo']}\t\t{bicicleta['tipo']} {'*'*10}\t\t\t\t   {bicicleta['disponivel']}')

def listar_usuarios(usuarios):

    for index, usuario in enumerate(usuarios):

        print(f'{index+1} - {usuario['cpf']} - {usuario['nome']} - {usuario['idade']} -{usuario['telefone']} - {usuario['endereco']}')

def novo_usuario(usuarios):
    print('=== Cadastrar NOVO USUÁRIO ===\n')
    cpf = str(input('Informe o CPF (sem espaços): '))
    usuario_existe = consultar_usuario(cpf, usuarios)

    if usuario_existe:
        print('Este usuário já existe no Sistema!')
        return
    
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    telefone = str(input('Telefone - (Exemplo: 11999990000): '))
    endereco = str(input('Endereço - (Exemplo: Rua A, 123 - São Paulo/SP) '))
    
    usuarios.append({'cpf':cpf, 'nome':nome, 'idade':idade, 'telefone':telefone, 'endereco':endereco})
    print('Usuario registrado com sucesso!')

def consultar_usuario(cpf, usuarios):

    encontrar_usuario = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return encontrar_usuario[0] if encontrar_usuario else None

def alugar_bicicleta(usuarios, bicicletas, historico):

    cpf = str(input('Informe o CPF (sem espaços): '))
    usuario_existe = consultar_usuario(cpf, usuarios)

    if not usuario_existe:
        print('Este usuário não está cadastrado')
        return
    
    codigo = str(input('Código: ')).strip().upper()
    bike_existe = bicicleta_existe(codigo, bicicletas)

    if not bike_existe:
        print('Bicicleta não cadastrada no sistema!')
        return
    
    bike_existe['disponivel'] = False

    data_formatada = datetime.now().strftime("%d de %B de %Y às %H:%M")

    print(f'Bicicleta "{codigo}" alugada para {usuario_existe['nome']}!')

    historico.append({'cpf':usuario_existe["cpf"],'nome':usuario_existe["nome"],'codigo':bike_existe["codigo"], 'tipo':bike_existe["tipo"], 'data_aluguel':data_formatada, 'status':'Aluguel'})

def devolucao_bicicleta(usuarios, bicicletas, historico):

    cpf = str(input('Informe o CPF (sem espaços): '))
    usuario_existe = consultar_usuario(cpf, usuarios)

    if not usuario_existe:
        print('Este usuário não está cadastrado!')
        return
    
    codigo = str(input('Código: ')).strip().upper()
    bike_existe = bicicleta_existe(codigo, bicicletas)

    if not bike_existe:
        print('Bicicleta não cadastrada no sistema!')
        return
    
    data_formatada = datetime.now().strftime("%d de %B de %Y às %H:%M")

    if bike_existe['disponivel']:
        print('A bicicleta já foi devolvida!')
        return
        
    print(f'Bicicleta "{codigo}" devolvida por {usuario_existe['nome']}!')
    historico.append({'cpf':usuario_existe["cpf"],'nome':usuario_existe["nome"],'codigo':bike_existe["codigo"], 'tipo':bike_existe["tipo"], 'data_aluguel':data_formatada, 'status':'Devolução'})
    
    bike_existe['disponivel'] = True

def consultar_historico(historico):

    print('=+=+=+= HISTÓRICO DE ALUGUEL =+=+=+= \n')

    if not historico:
        print('Não há nenhum registro no histórico!')
        return

    for registro in historico:        

        print(f"{registro['cpf']} - {registro['nome']} - {registro['codigo']} - {registro['tipo']} - {registro['data_aluguel']} - {registro['status']} ")


def menu():
    menu = '''
[nb] Nova bicicleta
[lb] Listar bicicleta
[lu] Listar usuários
[nu] Novo usuário
[a] Alugar bicicleta
[d] Devolver bicicleta
[h] Histórico de aluguel
[q] Sair
===>>'''

    return input(menu)

def main():

    while True:
        
        opcao = menu().strip().lower()

        if opcao == 'nb':
            
            nova_bicicleta(bicicletas)

        elif opcao == 'lb':
            
            listar_bicicletas(bicicletas)

        elif opcao == 'lu':
            
            listar_usuarios(usuarios)

        elif opcao == 'nu':
            
            novo_usuario(usuarios)

        elif opcao == 'a':
            
            alugar_bicicleta(usuarios, bicicletas, historico)

        elif opcao == 'd':
            
            devolucao_bicicleta(usuarios, bicicletas, historico)

        elif opcao == 'h':
            
            consultar_historico(historico)
        
        elif opcao == 'q':
            print('Obrigado')
            break

        else:
            print('Entrada inválida! Tente novamente!')

main()
