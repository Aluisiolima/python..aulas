def menu():
    menu = """\n
    =====menu=====
    [1] saque
    [2] depositor
    [3] extrato
    [4] cria usuario
    [5] cria conta 
    [6] sair

    """
    return int(input(menu))

def saque(*,saldo, extrato, valor, limite_valor_diario, limite_saques, saques):
    excedeu_limite = valor > limite_valor_diario
    excedeu_limite_diario = saques >= limite_saques
    excedeu_valor_em_conta = valor > saldo

    if excedeu_limite :
        print(f"voce excedeu seu limete valor diario, porfavor tente novamente")
    elif excedeu_limite_diario :
        print(f"voce excedeu seu limete de saques diario, porfavor tente novamente amanha")
    elif excedeu_valor_em_conta :
        print(f"voce nao tem saldo suficiente para concluir essa operacao")
    elif valor > 0:
        saldo -= valor 
        extrato += f"saque: R${valor:.2f} \n"
        saques += 1
        print(f"operacao concluida com sucesso, voce sacou R${valor}")
    else:
        print("operacao invalida tente novamente ")
    
    return saldo, extrato ,saques

def depositor(valor, extrato, saldo , /):
    if valor > 0:
        saldo += valor
        extrato += f"depositor: R${valor:.2f}\n"
        print(f"seu depositor de R${valor} foi concluido com suceso")
    else :
        print("valor invalido tente novamente")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("====extrato====")
    print("ainda nao fez nenhuma movimentacao"if not extrato else extrato)
    print(f"saldo: R${saldo:.2f}")
    print("===============")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (numero da casa, - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")


def main():
    saldo = 0
    LIMITE_VALOR_DIARIO = 500
    LIMITE_SAQUES = 3
    saques = 0
    extrato =""
    usuario = []
    contas = []
    AGENCIA = "0001"

    while True :
        opcao = menu()

        if opcao == 1 :
            valor = float(input("quanto deseja sacar:"))

            saldo, extrato,saques =saque(
                saldo = saldo,
                extrato=extrato,
                valor=valor,
                limite_valor_diario= LIMITE_VALOR_DIARIO,
                limite_saques= LIMITE_SAQUES,
                saques=saques
            )
        elif opcao == 2 :
            valor = float(input("quanto deseja depositar:"))

            saldo, extrato = depositor(
                valor,
                extrato,
                saldo
            )
        elif opcao == 3:
            exibir_extrato(
                saldo,
                extrato=extrato
            )
        elif opcao == 4:
          criar_usuario(usuarios=usuario)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuario)
            
            if conta:
                contas.append(conta)

                            
        elif opcao == 6:
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
          
main()