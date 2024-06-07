import os
from modulo import *

indice = 0
opcao = 0

pessoas = []

while True:
    print ("\nAplicativo de Banco: \n")
    print('1 - Cadastrar nome no aplicativo')
    print('2 - Deletar nome no aplicativo')
    print('3 - Entrar no aplicativo')
    print('4 - Sair do programa')

    opcao1 = int(input('\nEscolha a opção desejada (1 a 4):\n'))
    
    match opcao1:
        case 1:
            while True:
                novo_nome = input('Informe o novo nome a ser inserido no banco: ')
                if novo_nome !='':
                    numero_conta = indice + 1
                    saldo = 0
                    pessoa = {"Nome": novo_nome, "Numero da Conta": numero_conta, "Saldo": saldo}
                    pessoas.append(pessoa)
                    print(f'{novo_nome} inserido com sucesso.')
                    print(f'Número da Conta: {numero_conta}.')
                    print(f'Titular da Conta: {novo_nome}.')
                    print(f'Saldo: {saldo}.')
                    print('\nLista de Clientes:')
                    for nome in pessoas:
                        print(nome)        
                    continue
                else: 
                    os.system('cls')
                    for nome in pessoas:
                        print(nome)                
                    break
        case 2:
            nome_a_excluir = input('Informe o nome que deseja retirar do banco: ')
            try:
                pessoas.remove(nome_a_excluir)
            except:
                print('Nome não pode ser excluído.')

            for nome in pessoas:
                print(nome)        
        case 3:
            nome = input('Informe o nome que deseja encontrar: ').capitalize()
            # busca o nome desejado
            try:
                indice = pessoas.index(nome)
                quantidade = pessoas.count(nome)
                print(f'Nome encontrado: {nome} {quantidade} vez(es) no índice {indice}')
            except:
                print(f'{nome} não encontrado no aplicativo.')
        case 4:
            break
        case _:
            print('Opção inváida! Digite uma opção de 1 a 4')
            continue      