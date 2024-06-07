 
def extrato(titular, saldo):
    print("O saldo de {} é de {}".format(titular, saldo))

def deposita(valor):
    saldo += valor

def pode_sacar(valor): 
    return valor <= (saldo + limite)

def saca(self, valor): 
    if pode_sacar(valor):
        saldo -= valor
    else:
        print("Saldo Insuficiente!")

def transfere(valor, conta_destino): 
    if pode_sacar(valor):
        saca(valor)
        conta_destino.deposita(valor)
        print("Tranferência de {} realizada com êxito!".format(valor))
    else:
        print("Transferência não efetuada: Saldo Insuficiente!")

def codigo_banco():
    return "001"        