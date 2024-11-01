usuarios = [
    ["João", 25, "Piracicaba", "SP"],
    ["Ana", 22, "Limeira", "SP"],
    ["Carlos", 30, "Belo Horizonte", "MG"],
    ["Fernanda", 28, "Curitiba", "PR"],
    ["Marcos", 27, "Porto Alegre", "RS"]
]

perfis = [
    {"nome": "João", "idade": 25, "localização": ("Piracicaba", "SP")},
    {"nome": "Ana", "idade": 22, "localização": ("Limeira", "SP")},
    {"nome": "Carlos", "idade": 30, "localização": ("Belo Horizonte", "MG")},
    {"nome": "Fernanda", "idade": 28, "localização": ("Curitiba", "PR")},
    {"nome": "Marcos", "idade": 27, "localização": ("Porto Alegre", "RS")}
]

def criar_dados_rede(usuarios, perfis):
    dados_rede = []

    for usuario in usuarios:
        nome, idade, cidade, estado = usuario
        dados_rede.append(f"{nome}?{idade}?{cidade}?{estado}?")

    for perfil in perfis:
        nome = perfil["nome"]
        idade = perfil["idade"]
        cidade, estado = perfil["localização"]
        dados_rede.append(f"{nome}?{idade}?{cidade}?{estado}?")

    return dados_rede

def salvar_dados_arquivo(dados, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as file:
        for dado in dados:
            file.write(dado + "\n")

dados_rede = criar_dados_rede(usuarios, perfis)

arquivo_rede = 'data/rede_INFNET.txt'

salvar_dados_arquivo(dados_rede, arquivo_rede)

print("Dados salvos em rede_INFNET.txt.")
