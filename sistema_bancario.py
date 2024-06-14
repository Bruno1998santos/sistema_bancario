saldo_final = 0
deposito = 0
contador_deposito = 0 
contador_saque = 0
mensagem_deposito= 0
saque = 0.0
mensagem_novo_saque = 0
bloco_deposito = []
bloco_saque = []
valor_deposito =0.0
while True:
    menu = int (input('''
                                Menu
                            [1] Deposito
                            [2] Saque
                            [3] Extrato
                            [4] Sair
                '''))

    if menu == 1: # Bloco Depósito
        mensagem_deposito= int (input(f'''
                        Você acessou a opção deposito. 
                            [1] Continuar
                            [2] Voltar
                                '''))
        
        if mensagem_deposito == 1:
            valor_deposito = float(input('Informe o valor do depósito: '))
            
            if valor_deposito >=0:
                saldo_final += valor_deposito
                bloco_deposito.append (valor_deposito)
                
                while True:
                    continuar_deposito = int (input(f'''
                        Deseja Realizar outro depósito ?. 
                            [1] Sim
                            [2] Não
                                    '''))
                    
                    if continuar_deposito == 1:
                        valor_deposito= float(input('Informe o valor do depósito: '))
                        
                        if valor_deposito >= 0:
                            saldo_final += valor_deposito
                            contador_deposito += 1
                            bloco_deposito.append (valor_deposito)
                        
                        elif valor_deposito <0:
                            print ('O valor de depósito deve ser positivo.')
                            
                    elif continuar_deposito == 2:
                        print ('Voltando para o Menu.... !')
                        break
                           
            else:
                print ('O valor de depósito deve ser positivo. ')
                 
                         
    elif menu == 2: #Bloco Saque:
     
        mensagem_saque= int (input(f'''
                    Você acessou a opção saque. 
                            [1] Continuar
                            [2] Voltar
                                        '''))
        while contador_saque <=2:  
            if contador_saque<=2:
                if mensagem_saque == 1:
                    if saldo_final >0:
                        
                        saque = float(input(f'''
                    Seu saldo atual é de {saldo_final} 
                    Informe o valor do Saque:
                                '''))
                        if saque <= 500 and saque <= saldo_final and saldo_final !=0 and saque >0:
                            saldo_final -= saque
                            print (f'''
                                Realizando saque....
                                ------------------------
                                ''')
                            contador_saque +=1
                            bloco_saque.append(saque)
                            if saldo_final > 0:
                                mensagem_novo_saque = int (input(f'''
                    Deseja realizar um novo saque?. 
                            [1] Continuar
                            [2] Voltar
                                    '''))
                                
                            elif saldo_final <=0:
                                print ('Sem saldo')
                                break
                            
                        elif saldo_final <= 0:
                            print(f'Sem Saldo {saldo_final} \n')
                            break
                        
                        elif saque <=0:
                            print ('O valor do saque não deve ser menor ou igual a zero')
                        elif saque > 500:
                            print('Limite de saque R$500,00')
                            
                        
                    elif saldo_final <= 0:
                            print(f'Sem Saldo {saldo_final} \n')
                            break
                        
                elif mensagem_saque == 2:
                        print ('Voltando para o menu...')
                        break  
                else:
                        print ('Opção inválida!') 
        else:
            print ('Limite de saque excedido')
    
    
    elif menu == 3: #Bloco Extrato
        while True:
            if contador_deposito <=0 and contador_saque <=0:
                print (' Não foram realizadas movimentações')
                break
            elif contador_deposito >=0 or contador_saque >=0:
                print (f'''
                       Saldo Atual: R$ {saldo_final:.2f}''')
                print (f'''
                       Saques realizados''')
                for saque in bloco_saque:
                    print (f'''
                       R$ {saque:.2f}''')
                print (f'''
                       Depósitos realizados''')
                for valor_deposito in bloco_deposito:
                    print (f'''
                       R$ {valor_deposito:.2f}''')    
                break
                   
                         
    elif menu == 4:# Bloco Sair
        print('Até mais!')
        break           
       
    else :
        print ('Opção inválida')
