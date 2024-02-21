menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
==> 
"""

saldo = 0
extrato = ''
numero_saques = 0

def saque(numero_saques, saldo, extrato):
    if numero_saques > 3:
        print('\nNúmero máximo de saques diário excedido')
    elif saldo > 500:
        print('Limite de valor de saque excedido')
    else:
        numero_saques += 1
        valor = float(input('Informe o valor do saque: '))
        if valor > saldo:
            print('Saldo insuficiente')
        else:
            saldo -= valor
            print(f'\nSaque de R$ {valor: .2f} realizado com sucesso')
            extrato += f"Saque: R$ {valor: .2f}\n"
    return saldo, extrato


while True:
  opcao = input(menu)

  if opcao == '1':
    valor = float(input("\nInforme o valor do depósito: "))
    if valor < 0:
      print("Valor inválido")
    else:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
      print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso")

  elif opcao == '2':
    saque(numero_saques, saldo, extrato)

  elif opcao == '3':
    print(extrato)
    print(f'\nSaldo atual: R$ {saldo:.2f}')

  elif opcao == '4':
    break

  else:
    print('Operação inválida')