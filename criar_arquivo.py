import csv

def criar_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        for linha in dados:
            escritor.writerow(linha)


blog_dados_csv = 'blog_dados'
dados_para_escrever = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', 25, 'São Paulo'],
    ['Maria', 30, 'Rio de Janeiro'],
    ['Carlos', 22, 'Belo Horizonte'],
    ['Ana', 28, 'Porto Alegre'],
    ['Rafael', 35, 'Curitiba'],
    ['Juliana', 40, 'Salvador'],
    ['Pedro', 31, 'Fortaleza'],
    ['Mariana', 25, 'Recife'],
    ['Lucas', 29, 'Belém'],
    ['Fernanda', 33, 'Manaus'],
    ['Gabriel', 27, 'Vitória'],
    ['Isabela', 22, 'Florianópolis'],
    ['Felipe', 38, 'Natal'],
    ['Carolina', 30, 'Porto Velho'],
    ['Daniel', 26, 'Goiânia'],
    ['Patrícia', 34, 'Teresina'],
    ['Thiago', 32, 'Campo Grande'],
    ['Amanda', 23, 'João Pessoa'],
    ['Rodrigo', 36, 'Cuiabá'],
    ['Laura', 31, 'Aracaju']
]


criar_arquivo(blog_dados_csv, dados_para_escrever)
print(f'Arquivo .CSV "{blog_dados_csv}" criado com sucesso')