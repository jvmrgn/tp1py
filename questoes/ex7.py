import os

perfis = {
    "João": {
        "idade": 25,
        "localização": ("Piracicaba", "SP"),
        "amigos": {"Ana", "Marcos"}
    },
    "Ana": {
        "idade": 22,
        "localização": ("Limeira", "SP"),
        "amigos": {"João"}
    },
    "Carlos": {
        "idade": 30,
        "localização": ("Belo Horizonte", "MG"),
        "amigos": set()
    }
}

def adicionar_amigo(usuario, novo_amigo):
    if usuario in perfis:
        perfis[usuario]["amigos"].add(novo_amigo)
        print(f"{novo_amigo} adicionado como amigo de {usuario}.")
        salvar_dados()
    else:
        print(f"Usuário {usuario} não encontrado.")

def salvar_dados():
    rede_infnet_path = os.path.join('data', 'rede_INFNET.txt')
    
    with open(rede_infnet_path, 'w', encoding='utf-8') as file:
        for usuario, info in perfis.items():
            amigos = '?'.join(info["amigos"])
            localizacao = f"{info['localização'][0]}?{info['localização'][1]}"
            linha = f"{usuario}?{info['idade']}?{localizacao}?{amigos}\n"
            file.write(linha)
    
    print("Dados salvos em rede_INFNET.txt.")

usuario_especifico = "João"
novo_amigo = "Carlos"
adicionar_amigo(usuario_especifico, novo_amigo)

print(perfis[usuario_especifico]["amigos"])
