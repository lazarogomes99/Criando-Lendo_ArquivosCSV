import csv

def ler_arquivo(dados):
    with open(dados, 'r', newline='') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            print(f'{linha[0]}, {linha[1]}, {linha[2]}')

ler_arquivo('blog_dados')