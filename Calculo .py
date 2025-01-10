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
""" 
f"{valor:,.2f}"
f-string (disponível a partir do Python 3.6) permite inserir variáveis diretamente em strings, usando a sintaxe {variável:formatação}.
:,.2f é o especificador de formato:
, insere vírgulas como separadores de milhar (padrão americano).
.2f formata o valor como um número decimal com 2 casas após a vírgula.

.replace(",", ".")
Aqui, usamos o método replace(",", ".") para substituir todas as vírgulas geradas pelo formato padrão americano por pontos. Isso transforma 1,234,567.89 em 1.234.567.89.

A função .strip().lower() foi adicionada no momento de entrada da variável repetir para melhorar a usabilidade e evitar erros devido a espaços ou diferenças de maiúsculas e minúsculas. Aqui está a explicação detalhada:

.strip()

Remove quaisquer espaços em branco extras no início e no final da entrada do usuário.
Isso é útil porque, às vezes, o usuário pode pressionar a barra de espaço antes ou depois de digitar o valor. Exemplo:
Sem .strip(): " s " (com espaços) seria tratado como inválido.
Com .strip(): " s " se torna "s", o que é válido.
.lower()

Converte todas as letras para minúsculas.
Isso permite que o programa trate as entradas de forma consistente, independentemente de o usuário digitar "S", "s", "Sim" ou "sim". Apenas o "s" minúsculo será avaliado.
"""