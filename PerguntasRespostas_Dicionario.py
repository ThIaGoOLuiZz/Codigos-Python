contagemCorreto = 0
contagemErrado = 0

dicionario = [
{
    'Pergunta': 'Qual a Soma de 2+2?',
    'opcoes': ['2','7','8','4'],
    'correto': '4',
},
{
    'Pergunta': 'Qual a Divisão de 10/2?',
    'opcoes': ['4','3','5','9'],
    'correto': '5',
}
]

for perguntas in dicionario:
    print(perguntas['Pergunta'])
    print("")
    
    for opcoes in perguntas['opcoes']:
        print(opcoes)
        
    print("")
    
    for respostas in perguntas['correto']:
        resposta = respostas
        
    respUsuario = input("Qual a resposta correto?: ")
    print("")
    
    if respUsuario == resposta:
        print("Você acertou!!!")
        contagemCorreto = contagemCorreto + 1
        
    else:
        print("Você Errou!!!")
        contagemErrado = contagemErrado + 1
        
        
print(f"Você acertou {contagemCorreto}!")
print(f"Você errou {contagemErrado}!")