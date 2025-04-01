# Funções para cada operação
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

# Função principal
def calculadora():
    print("Selecione a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input("Digite o número da operação (1/2/3/4): ")

    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida!")
        return

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
        return

    if escolha == '1':
        print(f"{num1} + {num2} = {somar(num1, num2)}")
    elif escolha == '2':
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")

# Chama a função da calculadora
calculadora()
