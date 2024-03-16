def sacar(saldo, valor):
    saldo -= valor
    print("Novo saldo após saque: %d" % saldo)
    return saldo

def depositar(saldo, valor):
    saldo += valor
    print("Novo saldo após depósito: %d" % saldo)
    return saldo

def continuar():
    continuar = input("Deseja realizar outra operação? (s/n): ").lower()
    return continuar != "s"  # Retorna True se continuar for diferente de 's'
    
def obter_valor(mensagem):
    while True:
        valor_str = input(mensagem)
        if valor_str.isdigit():  # Verifica se a entrada é um número inteiro
            return int(valor_str)
        else:
            print("Por favor, insira um valor inteiro válido.")

saldo = obter_valor("Quanto você tem de saldo? ")
while True:
    operacao = input("Qual ação deseja fazer? Saque || Deposito: ").lower()
    if operacao == "saque":
        saque = obter_valor("Quanto deseja sacar? ")
        saldo = sacar(saldo, saque)
        if continuar():
            break
    elif operacao == "deposito":
        deposito = obter_valor("O quanto deseja depositar? ")
        saldo = depositar(saldo, deposito)
        if continuar():
            break
    else:
        print("Operação inválida!")
print("Sessão finalizada.\nSaldo Final: %d" % saldo)
