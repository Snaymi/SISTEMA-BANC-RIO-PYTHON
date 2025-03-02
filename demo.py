import datetime

depositos = []

saques = []

SAQUES_MAXIMOS = 3

while True: # Começa o loop, sendo que ele é executado PELO MENOS uma vez!

    print("OLA, SEJA BEM VINDO, digite a opcao desejada: \n 1 - Deposito \n 2 - Saque \n 3 - Ver extrato")
    # Mostra as opções para o usuário

    opcao = int(input("Digite: ")) #Pede para ele digitar qual opção ele deseja
   

    if (opcao ==1): # Condicional para caso ele tecle a OPÇÃO 1

        print("Tecla digitada: 1 - Deposito \n Processando...")

        valor_deposito = int(input("Qual valor do deposito? "))
        if (valor_deposito>1): # Condicional para que o valor do deposito seja maior que 1

            print("Valor digitado: ", valor_deposito , "\n Confirma o Deposito desse valor?\n 1 - SIM \n 2 - NAO\n")

            confirmacao = int(input()) #Confirmação do valor do deposito


            if(confirmacao == 1 ): 

                depositos.append(valor_deposito)

                print("Deposito realizado com sucesso!\n \n Obrigado por ser nosso cliente!\n")

            else: print("Deposito Cancelado") #caso tenha algo erro no deposito

        else: print("Valor do deposito inválido!")

    elif(opcao == 2): 
        agora = datetime.datetime.now()

        saques_24h = [saque for saque in saques if (agora - saque).total_seconds() < 86400]

        if len(saques_24h) < SAQUES_MAXIMOS:
            print("Tecla digitada: 2 - Saque \n Processando...")

            valor_saque = int(input("Digite o Valor do Saque: "))
        if(valor_saque<=500):
            print("Valor do saque: " , valor_saque , " Confirma? \n 1 - Sim \n 2 Nao\n")
        
            confirmacao = int(input())
        
            if (confirmacao==1): 
                saques.append(agora)
                print("Validacao de seguranca em andamento...\n Sucesso!! \n \n OBRIGADO POR SER NOSSO CLIENTE!")
            else: 
                print("Deposito cancelado.")

        else:print("Valor excede o limite pode saque")
       
    elif(opcao == 3): 

        print("Tecla digitada: 3 -Ver extrato \n Processando...")

        print("Extrato de depositos: \n\n")

        for i, valor in enumerate(depositos, 1):

            print(f"{i}.R${valor:.2f}\n")

    else: print("Tecla invalida, favor digitar uma opcao valida!")

    tentar_novamente = input("Gostaria de tentar novamente?\n 1 - Sim \n 2 - Nao")

    if (tentar_novamente ==1): 

        
        break
