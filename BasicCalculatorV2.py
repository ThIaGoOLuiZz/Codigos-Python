#Variaveis
conta = ""
repeticao = True

escolhaPartes = 1
    
def contas(a, b):
    while(repeticao):
        print("\nQual a conta você deseja realizar?\n")
        print("Adição")
        print("Subtração")
        print("Multiplicação")
        print("Divisão\n\n")
        conta = input()
        
        if conta.upper() == "ADICAO" or conta.upper() == "ADIÇÃO":
            resultado = a + b
            return resultado
            
        elif conta.upper() == "SUBTRACAO" or conta.upper() == "SUBTRAÇÃO":
            resultado = a - b
            return resultado
            
        elif conta.upper() == "MULTIPLICACAO" or conta.upper() == "MULTIPLICAÇÃO":
            resultado = a * b
            return resultado
            
        elif conta.upper() == "DIVISAO" or conta.upper() == "DIVISÃO":
            resultado = a / b
            return resultado 
            
        else:
            print("Conta não identificada, tente novamente!")

###############################################

while(repeticao):
    if escolhaPartes == 1:
    
        #Primeiro Número
        while(repeticao):  
            try:
                valor1 = int(input("Digite um valor: "))
                break
    
            except:
                print("Não foi possível continuar, pois o valor digitado não é um número!")
                continue

        #Segundo Número
        while(repeticao):  
            try:
                valor2 = int(input("Digite outro valor: "))
                break
    
            except:
                print("Não foi possível continuar, pois o valor digitado não é um número!")
                continue
        escolhaPartes = 2
        continue
    
    elif escolhaPartes == 2:
    
        print("Resultado =", contas(valor1, valor2))
            
        #Repeticao do programa
        repeticaoParte_1 = input("\nVocê deseja continuar no programa?(sim ou não)\n")
    
        while(repeticao):
            if repeticaoParte_1.startswith("s") or repeticaoParte_1.startswith("S"):
                escolhaPartes2 = input("Deseja manter os mesmos números?\n")
                if escolhaPartes2.startswith("s") or escolhaPartes2.startswith("S"):
                    escolhaPartes = 2
                    break
                else:
                    escolhaPartes = 1
                    break
                break
            elif repeticaoParte_1.startswith("n") or repeticaoParte_1.startswith("N"):
                escolhaPartes = 0
                break
           

    elif escolhaPartes == 0:
        break
        
        