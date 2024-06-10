import os
from modulo import *
from datetime import date

indice = 0
opcao = 0

pessoas = []

while True:
    print ("\nAplicativo de Banco: \n")
    print('1 - Cadastrar nome no aplicativo')
    print('2 - Deletar nome no aplicativo')
    print('3 - Entrar no aplicativo - Consultar o Saldo')
    print('4 - Entrar no aplicativo - Deposita')
    print('5 - Entrar no aplicativo - Saca')
    print('6 - Sair do programa')

    opcao1 = int(input('\nEscolha a opção desejada (1 a 6):\n'))
    
    match opcao1:
        case 1:
            while True:
                novo_nome = input('Informe o novo nome a ser inserido no banco: ')
                if novo_nome !='':
                    tamanho_dicionario = len(pessoas);
                    if tamanho_dicionario == 0:
                        numero_conta = 1
                    else:
                        numero_conta = tamanho_dicionario + 1    
                    saldo = 0
                    pessoa = {"Nome": novo_nome, "Numero da Conta": numero_conta, "Saldo": saldo}
                    pessoas.append(pessoa)
                    print(f'{novo_nome} inserido com sucesso.')
                    print(f'Número da Conta: {numero_conta}.')
                    print(f'Titular da Conta: {novo_nome}.')
                    print(f'Saldo: {saldo}.')
                    extrato(novo_nome, saldo)
                    print('\nLista de Clientes:')
                    for nome in pessoas:
                        print(nome)        
                    continue
                else: ca
                    os.system('cls')
                    for nome in pessoas:
                        print(nome)                
                    break
        case 2:
            indice_excluir = int(input('Informe o índice que deseja deletar da lista de dicionário: '))
            indice_excluir -=1
            try:
                del(pessoas[indice_excluir])
            except:
                print('Não foi possível deletar o índice!')
            for i in range(len(pessoas)):
                    print(f'Índice: {i + 1}')
                    print(f'Nome: {pessoas[i]['Nome']}')
                    print(f'Conta: {pessoas[i]['Numero da Conta']}')
                    print(f'Saldo: {pessoas[i]['Saldo']}\n')
        case 3:
            nome_busca = input('Informe o nome da pessoa que deseja consultar o saldo: ').capitalize()
            # busca o nome desejado
            for i in range(len(pessoas)):
                if nome_busca in pessoas[i]['Nome']:
                    extrato(pessoas[i]['Nome'],pessoas[i]['Saldo'])
                else:
                    continue
        case 4:
            nome_busca1 = input('Informe o nome da pessoa que deseja depositar: ').capitalize()
            # busca o nome desejado
            for i in range(len(pessoas)):
                if nome_busca1 in pessoas[i]['Nome']:
                    print(f'Índice: {i + 1}')
                    print(f'Nome: {pessoas[i]['Nome']}')
                    print(f'Conta: {pessoas[i]['Numero da Conta']}')
                    print(f'Saldo: {pessoas[i]['Saldo']}')
                    saldo_atual = pessoas[i]['Saldo']
                    valor_deposito = int(input('Informe o valor que será depositado: '))
                    if valor_deposito > 0:
                        pessoas[i]['Saldo'] += valor_deposito
                        print(f'Novo Saldo: {pessoas[i]['Saldo']}')
                    else:    
                        print('Digite um valor > 0')            
                else:
                    continue
        case 5:
            nome_busca2 = input('Informe o nome da pessoa que deseja sacar: ').capitalize()
            # busca o nome desejado
            for i in range(len(pessoas)):
                if nome_busca2 in pessoas[i]['Nome']:
                    print(f'Índice: {i + 1}')
                    print(f'Nome: {pessoas[i]['Nome']}')
                    print(f'Conta: {pessoas[i]['Numero da Conta']}')
                    print(f'Saldo: {pessoas[i]['Saldo']}')
                    saldo_atual = pessoas[i]['Saldo']
                    valor_saque = int(input('Informe o valor que será sacado: '))
                    if valor_saque > 0:
                        pode_sacar(valor_saque, saldo_atual)
                        saca(valor_saque, saldo_atual)
                        if saldo_atual >= valor_saque:
                            pessoas[i]['Saldo'] -= valor_saque
                            print(f'Novo Saldo: {pessoas[i]['Saldo']}')
                        else:
                            print('Saldo insuficiente!')    
                    else:    
                        print('Digite um valor > 0')            
                else:
                    continue
        case 6:
            break
        case _:
            print('Opção inváida! Digite uma opção de 1 a 6')
            continue      