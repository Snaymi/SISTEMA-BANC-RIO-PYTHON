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


            if(confirmacao == 1 ): #Condicional para confirmação (1)

                depositos.append(valor_deposito)#Adciona o valor do depósito à lista de depósitos

                print("Deposito realizado com sucesso!\n \n Obrigado por ser nosso cliente!\n")

            else: print("Deposito Cancelado") #caso tenha algo erro no deposito

        else: print("Valor do deposito inválido!")#Valor do deposito deve ser maior que 1

    elif(opcao == 2): #Condicional para OPÇÃO 2
        agora = datetime.datetime.now() #Obtém a hora e data atuais.

        saques_24h = [saque for saque in saques if (agora - saque).total_seconds() < 86400]
        #Filtra saques realizados nas últimas 24 horas.

        if len(saques_24h) < SAQUES_MAXIMOS: #Verifica se o n° de saques nas últimas 24 horas é menor que o máximo permitido (3)
            print("Tecla digitada: 2 - Saque \n Processando...")

            valor_saque = int(input("Digite o Valor do Saque: "))
        if(valor_saque<=500): #verifica se o valor do saque é menor ou igual ao valor máximo permitido de R$500,00
            print("Valor do saque: " , valor_saque , " Confirma? \n 1 - Sim \n 2 Nao\n")
        
            confirmacao = int(input()) #confirmação do valor do saque
        
            if (confirmacao==1): #confirmação do valor saque
                saques.append(agora)#Adiciona a data e hora do saque à lista de saques diários permitiros (+1) max(3)
                print("Validacao de seguranca em andamento...\n Sucesso!! \n \n OBRIGADO POR SER NOSSO CLIENTE!")
            else: 
                print("Deposito cancelado.")#caso não haja confirmação

        else:print("Valor excede o limite pode saque")#valor do saque deve ser menor ou igual a R$500,00
       
    elif(opcao == 3):#Condicional para caso ele tecle a OPÇÃO 3

        print("Tecla digitada: 3 -Ver extrato \n Processando...")

        print("Extrato de depositos: \n\n")

        for i, valor in enumerate(depositos, 1): #Loop pelos depósitos, i é o índice começando de 1 e "valor" é o valor do deposito
            

            print(f"{i}.R${valor:.2f}\n")#Exibe o índice e o valor do deposito formatado com 2 (.2f) casas decimais

    else: print("Tecla invalida, favor digitar uma opcao valida!") #Caso a opção desejada não seja válida

    tentar_novamente = input("Gostaria de tentar novamente?\n 1 - Sim \n 2 - Nao")
    #Pergunta ao usuário se ele gostaria de tentar novamente.
    if (tentar_novamente ==1): #Se a resposta for NÃO(2), encerra o loop

        
        break
