#EXERCICIOde um terreno
while True:
    terreno_largura=float(input('Digite a largura do terreno: '))
    terreno_comprimento=float(input('Digite o comprimento do terreno: '))
    valor_metro_terreno=int(input('Valor do metro quadrado: '))

#CALCULO

    area=terreno_largura*terreno_comprimento
    valor_do_terreno=area*valor_metro_terreno
    comissao_5=100000
    comissao_10=100000
    cinco_porcento=5/100
    dez_porcento=10/100
    dez_porcento2='10'
    cinco_porcento2='5'

    valor_receber5=comissao_5*cinco_porcento
    valor_receber10=comissao_10*dez_porcento

    #resultados

    print(f'A area do terreno é {area} e o preço do terreno é:R$ {valor_do_terreno:,.2f}')

    if valor_do_terreno<=comissao_5:
        print(f'A sua comissão de {cinco_porcento2} é: R$ {valor_receber5:,.2f}')
    elif valor_do_terreno>comissao_10:
        print(f'A sua comissão de {dez_porcento2} é: R$ {valor_receber10:,.2f}')

#Continuar ou sair
    repetir=input('Deseja calcular outro terreno? [S]im - [N]ão:').strip().lower() # foi usado para remove quaisquer espaços em branco extras no início e no final da entrada do usuário.
    if repetir != 's':
        print('Encerramos os calculos por aqui!')
        break
