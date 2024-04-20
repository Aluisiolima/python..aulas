menu = """
   Qual operação deixa fazer?
     [1] sacar
     [2] depositar
     [3] ver extrato
     [0] sair

     -->
"""


estrato_bancario = ""
saldo = 0
saques = 0


LIMITE_DE_SAQUE_DIARIO = 3
LIMITE_DIARIO_VALOR_SAQUE = 500


while True:
    opcao = input(menu)

    if opcao == "1":
    
        if saques < LIMITE_DE_SAQUE_DIARIO:
           
            valor_do_saque = input("quanto deseja sacar:")
           
            if int(valor_do_saque) <= LIMITE_DIARIO_VALOR_SAQUE and int(valor_do_saque) <= saldo:
                print("saque concluido")
                saques += 1
                saldo -= int(valor_do_saque)
                print(f"voce sacou {float(valor_do_saque)} da sua conta ")
                estrato_bancario += f"saque de {float(valor_do_saque)}\n"
           
            elif  int(valor_do_saque) > LIMITE_DIARIO_VALOR_SAQUE :
                print(f"seu limete diario de saque e somente de R${float(LIMITE_DIARIO_VALOR_SAQUE)}")  
           
            elif  int(valor_do_saque) >= saldo :
                print(f"""voce nao tem saldo suficiente para esse saque
Seu saldo e de {float(saldo)}""")   
            else : 
                print('operacao invalida')

        else :
            print(f"vocw ja excedeu o limete de saques diario de {LIMITE_DE_SAQUE_DIARIO}")        
   
   
    elif opcao == "2":
        print('depositor')
        valor_do_deposito = input("quanto deseja depositar:")
        saldo += int(valor_do_deposito)
        print(f"voce depositou {float(valor_do_deposito)} na sua conta ")
        estrato_bancario += f"depositor de {float(valor_do_deposito)}\n"
       

    elif  opcao == "3":
        print(f"\n####### EXTRATO ###### ")
        print(f"Nao foram realizado nenhuma operacao ate agora." if not estrato_bancario else estrato_bancario)
        print(f"seu saldo e de {saldo:.2f}")
        print('##########################################')

    elif opcao == "0":
        break

    else :
        print('escolha um operacao')

            






