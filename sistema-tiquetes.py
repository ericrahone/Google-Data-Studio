# -*- coding: utf-8 -*-
"""BOOZOO

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11720lHtSQiqvTNLpaN6Tzha8kkxwWiJl

##SISTEMA DE TÍQUETES BOOZOO
"""

from time import sleep
conto = contx = 0
disp = []
indisp = []
bus = [[1, 0, 0, 0, 0], [2, 2, 0, 2, 2], [2, 2, 0, 2, 2],
       [2, 2, 0, 2, 2], [2, 2, 0, 2, 2], [2, 2, 0, 2, 2],
       [2, 2, 0, 2, 2], [2, 2, 0, 2, 2]]

arquivo = open('vendas.txt', 'w')

while True:
    print('-'*30)
    opt = input('OLA! BEM-VINDO AO SISTEMA DE \n      TIQUETES POCCOBUS\t  \n   DIGITE A OPCAO DESEJADA:\n\n'
                    '1 - VISUALIZAR ASSENTOS\n2 - COMPRAR PASSAGENS\n0 - SAIR\n')
    print('-'*30)

    #VISUALIZACAO DE ASSENTOS
    if opt == '1':
        contx = conto = 0
        for l in range(0, 8):
            for c in range(0,6):
                if l == 0:
                    print(f'{c:^2}',end=' ')
            print()
            print(f'{l+1:^2}', end=' ') ##COMO MINHA PRIMEIRA LINHA COMECA EM ZERO, UTILIZEI L+1 PARA QUE O ZERO DAS COLUNAS NAO SE REPITA

            for c in range(0, 5):
                if bus[l][c] == 1:
                    print(f'{"M":^2}',end=' ')
                elif bus[l][c] == 0:
                    print(f'{"-":^2}',end=' ')
                elif bus[l][c] == 2:
                    print(f'{"O":^2}',end=' ')
                    conto += 1
                elif bus[l][c] == 3:
                    print(f'{"X":^2}', end=' ')
                    contx += 1

        print(f'\n\nM (MOTORISTA)\n- (CORREDORES)'
              f'\n{"O":^2}(LUGARES DISPONIVEIS): {conto}'
              f'\n{"X":^2}(LUGARES OCUPADOS): {contx}')

        ver = str(input('\nDESEJA CONTINUAR? [S|N]\n')).upper().strip()
        while ver != 'S':
            if ver == 'N':
                break
            else:
                print('ENTRADA INVALIDA!')
                ver = str(input('DESEJA CONTINUAR? [S|N]\n')).upper().strip()
        if ver == 'N':
            print('\nOBRIGADO POR VIAJAR COM A POCCOBUS!')

            conto = contx = 0
            for l in range(0, 8):
                for c in range(0, 5):
                    if bus[l][c] == 2:
                        disp.append(f'{l + 1},{c + 1}')
                        conto += 1
                    elif bus[l][c] == 3:
                        indisp.append(f'{l + 1},{c + 1}')
                        contx += 1

            arquivo.write(
                f'OBRIGADO POR VIAJAR COM A POCCOBUS!\n\nLUGARES DISPONIVEIS: {conto}\n{disp}\n\nLUGARES OCUPADOS: {contx}\n{indisp}')
            break

    #COMPRA DE PASSAGENS
    elif opt == '2':
        while True:
            l = int(input('DIGITE O Nº DA LINHA (1 A 8) DO ASSENTO DESEJADO: '))
            if l > 0 and l < 9:
                break
            else:
                print('VALOR INVALIDO! DIGITE UM VALOR VALIDO!\n')
        while True:
            c = int(input('DIGITE O Nº DA COLUNA (1 A 5) DO ASSENTO DESEJADO: '))
            if c > 0 and c < 6:
                break
            else:
                print('VALOR INVALIDO! DIGITE UM VALOR VALIDO!\n')
        l=l-1 #UTILIZEI ESSE ARTIFICIO POIS A LINHA QUE O USUARIO VE COMECA EM UM, MAS SUA POSICAO E ZERO
        c=c-1 #MINHA PRIMEIRA COLUNA ESTAO NA POSICAO ZERO, MAS E PREENCHIDA PELOS INDICES DAS LINHAS, PORTANTO USO APENAS A PARTIR DA POSICAO 1

        if l == 0:
            if c == 0:
                print('\nIMPOSSIVEL COMPRAR AQUI, LUGAR DO MOTORISTA! \U0001f914')
            elif c > 0 and c < 6:
                print('\nIMPOSSIVEL COMPRAR AQUI, E O CORREDOR! \U0001f914')

        elif l > 0 and l < 9:
            if bus[l][c] == 2:
                print('\nLUGAR DISPONIVEL! PASSAGEM ADQUIRIDA! \U0001f603')
                bus[l][c] = 3

            elif bus[l][c] == 0:
                print('\nIMPOSSIVEL COMPRAR AQUI, E O CORREDOR! \U0001f914')

            elif bus[l][c] == 3:
                print('\nLUGAR INDISPONIVEL! \U0001f610')
        else:
            print('VALOR INVALIDO! DIGITE UM VALOR VALIDO \U0001f634')

        sleep(1)
        ver = str(input('\nDESEJA CONTINUAR? [S|N]\n')).upper().strip()
        while ver != 'S':
            if ver == 'N':
                break
            else:
                print('ENTRADA INVALIDA!')
                ver = str(input('DESEJA CONTINUAR? [S|N]\n')).upper().strip()
        if ver == 'N':
            print('\nOBRIGADO POR VIAJAR COM A POCCOBUS!')

            conto = contx = 0
            for l in range(0, 8):
                for c in range(0, 5):
                    if bus[l][c] == 2:
                        disp.append(f'{l + 1},{c + 1}')
                        conto += 1
                    elif bus[l][c] == 3:
                        indisp.append(f'{l + 1},{c + 1}')
                        contx += 1
            arquivo.write(f'OBRIGADO POR VIAJAR COM A POCCOBUS!\n\nLUGARES DISPONIVEIS: {conto}\n{disp}\n\nLUGARES OCUPADOS: {contx}\n{indisp}')
            break

    #SAIDA
    elif opt == '0':
        print('OBRIGADO POR VIAJAR COM A POCCOBUS!! \U0001f609')
        sleep(1)
        conto = contx = 0
        for l in range(0, 8):
            for c in range(0, 5):
                if bus[l][c] == 2:
                    disp.append(f'{l + 1},{c + 1}')
                    conto += 1
                elif bus[l][c] == 3:
                    indisp.append(f'{l + 1},{c + 1}')
                    contx += 1

        arquivo.write(f'\nOBRIGADO POR VIAJAR COM A POCCOBUS!\n\nLUGARES DISPONIVEIS: {conto}\n{disp}\n\nLUGARES OCUPADOS: {contx}\n{indisp}')
        sleep(1)
        break

    #ENTRADA DE VALORES INVALIDOS
    else:
        print('OPCAO INVALIDA! \U0001f925')
        sleep(1)
        ver = str(input('DESEJA CONTINUAR? [S|N]\n')).upper().strip()
        while ver != 'S':
            if ver == 'N':
                break
            else:
                print('ENTRADA INVALIDA!')
                ver = str(input('DESEJA CONTINUAR? [S|N]\n')).upper().strip()
        if ver == 'N':
            print('\nOBRIGADO POR VIAJAR COM A POCCOBUS!')

            conto = contx = 0
            for l in range(0, 8):
                for c in range(0, 5):
                    if bus[l][c] == 2:
                        disp.append(f'{l + 1},{c + 1}')
                        conto += 1
                    elif bus[l][c] == 3:
                        indisp.append(f'{l + 1},{c + 1}')
                        contx += 1

            arquivo.write(f'OBRIGADO POR VIAJAR COM A POCCOBUS!\n\nLUGARES DISPONIVEIS: {conto}\n{disp}\n\nLUGARES OCUPADOS: {contx}\n{indisp}')
            break