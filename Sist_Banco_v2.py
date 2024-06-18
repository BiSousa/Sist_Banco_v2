def menu():
    menu = """

    [0] - Depositar
    [1] - Sacar
    [2] - Extrato
    [3] - Novo usuário
    [4] - Nova conta
    [5] - Listar contas
    [6] - Sair

    --> """
    return input(menu)

def depositar(saldo, valor, extrato, /): #função apenas por posição
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado!")
    else:
        print("Não é possível realizar o depósito!")
    
    return saldo, extrato

def sacar(*, valor, saldo, extrato, limite, num_saques, limite_saques): #função nomeada
    if valor > saldo:
        print("Operação inválida. Saldo insuficiente.")
    elif valor > limite:
        print("Falha na operação. O valor é maior que o limite.")
    elif num_saques >= limite_saques:
        print("Limite de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        num_saques += 1
        print("Saque realizado!")
    else:
        print("Operação inválida. O valor não é válido.")
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato): #função mista
    print("----------EXTRATO----------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: {saldo:.2f}")
    print("---------------------------")

def cria_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        print("O usuário já existe!")
        return
    
    nome = input("Nome completo: ")
    data_nasc = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})

    print("Usuário criado!")
    
def filtra_usuario(cpf, usuarios):
    usuario_filtrado = [usuario_ind for usuario_ind in usuarios if usuario_ind["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def cria_conta(agencia, numero_conta, usuarios):
    cpf = input("Insira o CPF: ")
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado!")
0
def lista_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        #print("=" + 100)
        print(linha)

def main():
    menu()

    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    limite_saques = 3
    agencia = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao ==  "0": #DEPÓSITO
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato  = depositar(saldo, valor, extrato)           
        elif opcao == "1": #SAQUE
            valor = float(input("Informe o valor que deseja sacar: "))

            saldo, extrato = sacar(
                  valor = valor,
                  saldo = saldo,
                  extrato = extrato,
                  limite = limite,
                  num_saques = num_saques,
                  limite_saques = limite_saques)
        elif opcao == "2": #EXIBIR EXTRATO
            mostrar_extrato(saldo, extrato = extrato)
        elif opcao == "3": #NOVO USUÁRIO
            cria_usuario(usuarios)
        elif opcao == "4": #NOVA CONTA
            numero_conta = len(contas) + 1
            conta = cria_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "5": #LISTAR CONTAS
            lista_contas(contas)
        elif opcao == "6": #SAIR
            print("Até a próxima operação!")
            break
        else:
            print("Operação inválida. Insira uma operação válida!")

main()