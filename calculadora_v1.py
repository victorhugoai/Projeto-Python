# Calculadora em Python

# Vamos desenvolver uma calculadora em Python com tudo que você aprendi nos capítulos até aqui no curso da DSA (condicionais, loops, funções etc).
# A solução será apresentada no próximo capítulo!

from time import sleep
from math import sqrt, pow, factorial

# Definindo a função que repete o processo, função main:


def main():
    # Pedindo a opção do usuário
    print(
        '\n\033[1;32m******************* Calculadora em Python *******************\033[m')
    print('\nSelecione o número da operação desejada:')
    print('''
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potenciação
6 - Porcentagem
7 - Raíz quadrada
8 - Raíz cúbica
9 - Fatorial
10 - Inverso''')
    opcao_do_usuario = input('\nEscolha uma opção (1/2/3/4/5/6/7/8/9/10): ')

    # Não avança enquando a opção for inválida
    while opcao_do_usuario not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        print('\033[1;31mOpção Inválida! Tente novamente...\033[m')
        opcao_do_usuario = input(
            '\nEscolha uma opção (1/2/3/4/5/6/7/8/9/10): ')

    # Pede os números ao usuário
    if opcao_do_usuario in ('1', '2', '3', '4'):
        numero_1 = int(input('\nInforme o primeiro número: '))
        numero_2 = int(input('Informe o segundo número: '))
    elif opcao_do_usuario == '5':
        numero_1 = int(input('\nInforme a base: '))
        numero_2 = int(input('Informe o expoente: '))
    elif opcao_do_usuario == '6':
        print('\nA porcentagem funciona assim: X% DE Y. Por exemplo: 30% DE 100 = 30')
        numero_1 = int(input('\nInforme o primeiro número: '))
        numero_2 = int(input('Informe o segundo número: '))
    elif opcao_do_usuario == '7':
        numero_1 = int(input('Informe um número pra ver sua raíz quadrada: '))
    elif opcao_do_usuario == '8':
        numero_1 = int(input('Informe um número pra ver sua raíz cúbica: '))
    elif opcao_do_usuario == '9':
        numero_1 = int(input('Informe um número pra ver seu fatorial: '))
    else:
        numero_1 = int(input('Informe um número para ver seu inverso: '))

    # Criando as funções para cada operação
    def soma():
        return (f'\n{numero_1} + {numero_2} = {numero_1 + numero_2}')

    def subtracao():
        return (f'\n{numero_1} - {numero_2} = {numero_1 - numero_2}')

    def multiplicacao():
        return (f'\n{numero_1} x {numero_2} = {numero_1 * numero_2}')

    def divisao():
        return (f'\n{numero_1} / {numero_2} = {numero_1 / numero_2}')

    def potencia():
        return (f'\n{numero_1} Elevado a {numero_2} = {pow(numero_1, numero_2)}')

    def porcentagem():
        return (f'\n{numero_1}% de {numero_2} = {numero_1/100 * numero_2}')

    def raiz_quadrada():
        return (f'\n{sqrt(numero_1)}')

    def raiz_cubica():
        return (f'\n{numero_1 ** (1/3)}')

    def fatorial():
        return (f'\n{factorial(numero_1)}')

    def inverso():
        return (f'\nO inverso de {numero_1} é {1/numero_1}')

    # Verificando a opção do usuário para imprimir o resultado
    if opcao_do_usuario == '1':
        print('\033[1;36m', soma())
    elif opcao_do_usuario == '2':
        print('\033[1;36m', subtracao())
    elif opcao_do_usuario == '3':
        print('\033[1;36m', multiplicacao())
    elif opcao_do_usuario == '4':
        print('\033[1;36m', divisao())
    elif opcao_do_usuario == '5':
        print('\033[1;36m', potencia())
    elif opcao_do_usuario == '6':
        print('\033[1;36m', porcentagem())
    elif opcao_do_usuario == '7':
        print('\033[1;36m', raiz_quadrada())
    elif opcao_do_usuario == '8':
        print('\033[1;36m', raiz_cubica())
    elif opcao_do_usuario == '9':
        print('\033[1;36m', fatorial())
    else:
        print('\033[1;36m', inverso())

    # Verificando se o usuário quer usar a calculadora novamente
    usar_novamente = input(
        '\n\033[mQuer usar a calculadora novamente (S ou N): ').strip().upper()
    while usar_novamente not in ('S', 'N'):
        print(
            '\033[1;31mResposta Inválida. Digite apenas S (para Sim) e N (para Não)!\033[m')
        usar_novamente = input(
            '\nQuer usar a calculadora novamente (S ou N): ').strip().upper()
    if usar_novamente == 'S':
        print('\033[1;36PROCESSANDO...\033[m')
        sleep(2)
        main()
    else:
        print('\033[1;36mPROCESSANDO...\033[m')
        sleep(2)
        print('\033[1;32mPrograma Finalizado com sucesso!\033[m')
main()
