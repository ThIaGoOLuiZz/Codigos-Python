#Variaveis
conta = ""
repeticaoConta = 1
repeticaoNumero = 1
repeticaoDivisao = 1
repeticaoPrograma = 1
repeticao = 1

escolhaPartes = 1

##Funcao adição
def soma(a, b):
    resultado = a + b
    return resultado
    
##Funcao Subtração
def subtracao(a, b):
    resultado = a - b
    return resultado
    
##Funcao Multiplicação
def multiplicacao(a, b):
    resultado = a * b
    return resultado
    
##Funcao Divisão
def divisao(a, b):
    resultado = a/b
    return resultado


###############################################

while(repeticaoPrograma):
    if escolhaPartes == 1:
    
        #Primeiro Número
        while(repeticaoNumero):  
            try:
                valor1 = int(input("Digite um valor: "))
                break
    
            except:
                print("Não foi possível continuar, pois o valor digitado não é um número!")
                continue

        #Segundo Número
        while(repeticaoNumero):  
            try:
                valor2 = int(input("Digite outro valor: "))
                break
    
            except:
                print("Não foi possível continuar, pois o valor digitado não é um número!")
                continue
        escolhaPartes = 2
        continue
    
    elif escolhaPartes == 2:
    
        ##Repeticao das contas
        while(repeticaoConta):
    
            print("\nDigite o nome de uma das operações matemáticas abaixo que você deseja realizar:\n")
            print("Adição")
            print("Subtração")
            print("Multiplicação")
            print("Divisão\n\n")
            conta = input()
    
            #Adicao
            if conta.startswith("a") or conta.startswith("A"):
                print("Resultado =", soma(valor1, valor2))
                break
        
            #Subtracao
            elif conta.startswith("s") or conta.startswith("S"):
                print("Resultado =", subtracao(valor1, valor2))
                break
    
            #multiplicacao
            elif conta.startswith("m") or conta.startswith("M"):
                print("Resultado =", multiplicacao(valor1, valor2))
                break
    
            #divisao        
            elif conta.startswith("d") or conta.startswith("D"):
                while(repeticaoDivisao):
                    if valor2 == 0:
                        valor2 = int(input("\nnão é possível dividir o valor por zero!Por favor, digite outro valor\n\n"))
                        continue
                    else:
                        print("Resultado =", divisao(valor1, valor2))
                        break
                break
        
        
            else:
                print("conta inválida, tente novamente")
                continue
    
        #Repeticao do programa
        repeticaoParte_1 = input("\nVocê deseja continuar no programa?(sim ou não)")
    
        while(repeticao):
            if repeticaoParte_1.startswith("s") or repeticaoParte_1.startswith("S"):
                escolhaPartes2 = input("Deseja manter os mesmos números?")
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
        
        