def matriz_nula(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz


def matriz_transposta(matriz):
    nova_matriz = matriz_nula(len(matriz), len(matriz[0]))
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            nova_matriz[j][i] = matriz[i][j]

    return nova_matriz


def get_linha(matriz, n):
    return matriz[n]


def get_coluna(matriz, n):
    coluna = []
    for linha in matriz:
        coluna.append(linha[n])
    return coluna


def multiplica_linha_coluna(linha, coluna):
    return sum(map(lambda l: l[0] * l[1], zip(linha, coluna)))


def multiplica_matrizes(matriz1, matriz2):
    resultado = matriz_nula(len(matriz1), len(matriz1[0]))
    for i, linha in enumerate(resultado):
        for j in range(len(linha)):
            linha_matriz1 = get_linha(matriz1, i)
            coluna_matriz2 = get_coluna(matriz2, j)
            resultado[i][j] = multiplica_linha_coluna(linha_matriz1, coluna_matriz2)
    return resultado


def matriz_diagonal(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    nova_matriz = matriz_nula(linhas, colunas)

    for i in range(len(nova_matriz)):
        nova_matriz[i][i] = matriz[i][i]

    return nova_matriz


def soma_matrizes(matriz1, matriz2):
    linhas = len(matriz1)
    colunas = len(matriz1[0])
    nova_matriz = matriz_nula(linhas, colunas)

    for i, linha in enumerate(nova_matriz):
        for j in range(len(linha)):
            nova_matriz[i][j] = matriz1[i][j] + matriz2[i][j]

    return nova_matriz


def formatar_matriz(matriz):
    linhas = []
    for linha in matriz:
        linhas.append(" ".join(map(str, linha)))
    return "\n".join(linhas)


def main():
    quantidade_dimensoes = int(input("Quantidade de dimensões: "))
    a = []
    b = []

    print()

    for matriz, nome in zip([a, b], ["A", "B"]):
        print(f"Matriz {nome}:")
        for i in range(1, quantidade_dimensoes + 1):
            linha = input(f"Linha {i}: ").split()
            linha = list(map(int, linha))
            matriz.append(linha)
        print()

    print("Resultado:")
    resultado = soma_matrizes(matriz_transposta(a), multiplica_matrizes(matriz_diagonal(b), b))
    print(formatar_matriz(resultado))


if __name__ == "__main__":
    main()
