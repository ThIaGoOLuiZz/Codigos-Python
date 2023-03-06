calculo_cpf = input('Digite seu CPF(somente números): ')
lista = []
lista_range = []
lista_range2 = []
calculo_lista1 = []
calculo_lista2 = []
digito1 = 0
digito2 = 0
calculo_digito1 = 0
calculo_digito2 = 0
novo_cpf = 0
validador1 = True


#_________________________________PRIMEIRO DIGITO____________________________________
if calculo_cpf.isnumeric():
    if len(calculo_cpf) == 11:

        for i in calculo_cpf:
            lista.append(int(i))

        for x in range(10, 1, -1):
            lista_range.append(int(x))

        for y in range(11, 1, -1):
            lista_range2.append(int(y))


        calculo_lista1 = lista[0] * lista_range[0] + lista[1] * lista_range[1] + lista[2] * lista_range[2] + lista[3] * lista_range[3] + lista [4] * lista_range[4] + lista[5] * lista_range[5]+ lista[6] * lista_range[6] + lista[7] * lista_range[7] + lista[8] * lista_range[8]

        calculo_digito1 = 11 - (calculo_lista1%11)

        if calculo_digito1 > 9:
            digito1 = 0

        else:
            digito1 = calculo_digito1

#_________________________________SEGUNDO DIGITO____________________________________

        calculo_lista2 = lista[0] * lista_range2[0] + lista[1] * lista_range2[1] + lista[2] * lista_range2[2] + lista[3] * lista_range2[3] + lista[4] * lista_range2[4] + lista[5] * lista_range2[5] + lista[6] * lista_range2[6] + lista[7] * lista_range2[7] + lista[8] * lista_range2[8] + digito1 * lista_range2[9]

        calculo_digito2 = 11 - (calculo_lista2%11)

        if calculo_digito2 > 9:
            digito2 = 0

        else:
            digito2 = calculo_digito2

        if ((digito1 == int(calculo_cpf[9])) and (digito2 == int(calculo_cpf[10]))):
            print('CPF valido!')
        else:
            print('CPF invalido')

    else:
        print('CPF incorreto.')

else:
    print('Somente Digitos!')