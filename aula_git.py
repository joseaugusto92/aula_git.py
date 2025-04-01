    # ESTÁ TUDO APAGADO



# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para entrada de dados dos alunos
def entrada_notas():
    alunos = {}
    for i in range(1, 3):  # Para 2 alunos
        nome = input(f"Digite o nome do aluno {i}: ")
        notas = []
        for j in range(1, 5):  # 4 notas por aluno
            while True:
                try:
                    nota = float(input(f"Digite a nota {j} de {nome}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota deve ser entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida! Digite um número.")
        alunos[nome] = notas
    return alunos

# Função principal
def calcular_media_alunos():
    alunos = entrada_notas()

    for nome, notas in alunos.items():
        media = calcular_media(notas)
        print(f"\nA média do aluno {nome} é: {media:.2f}")

# Chama a função principal
calcular_media_alunos()

