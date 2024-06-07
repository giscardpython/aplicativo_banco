from datetime import date
 
def extrato(titular, saldo):
    print("O saldo de {} é de {}".format(titular, saldo))
    data = date.today()
    dataFormatada = data.strftime('%d/%m/%Y')
    print(f'Data da Consulta: {dataFormatada}')

def pode_sacar(valor, saldo_atual): 
    return valor <= (saldo_atual)

def saca(valor, saldo_atual): 
    if pode_sacar(valor, saldo_atual):
        print("Saque Autorizado")
    else:
        print("Saldo Insuficiente!")
