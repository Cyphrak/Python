try:
    a = int(input('Digite um número que será dividido: '))
    b = int(input('Digite um número do divisor: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário não informou os dados.')
except Exception as error:
    print('O erro encontrado foi {error.__cause__}')
else:
    print(f'O resultado é {r:.2f}')    