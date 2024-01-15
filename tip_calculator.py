# Title
print('CALCULADORA DE GORJETA')

# Validation
bloqueados = 'abcdefghijklmnopqrstuvwxyz'+' '+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'+'!#$%&()*+,-.:;<=>?@~'

# Value input looping
while True:
    # Input of Total Account
    conta_cliente = input('Digite o total da conta: ')
    if conta_cliente not in bloqueados:
        conta_cliente_float = float(conta_cliente)
    else:
        print('Digite um número, por favor')
        continue

    # Input percent of tip
    percentual_gorjeta = input('Digite o percentual de gorjeta: ')
    if percentual_gorjeta not in bloqueados:
        percentual_gorjeta_float = float(percentual_gorjeta)
        break
    else:
        print('Digite um número, por favor')
        continue
    
# Result value of percent tip
resultado = conta_cliente_float * percentual_gorjeta_float / 100
print(f'O valor que o garçom receberá é {resultado}')
