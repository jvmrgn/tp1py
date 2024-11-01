import os

def carregar_dados(base_inicial_path, rede_infnet_path):
    perfis = {}

    with open(base_inicial_path, 'r', encoding='utf-8') as file:
        for line in file:
            partes = line.strip().split('?')
            if len(partes) < 4:
                continue

            nome = partes[0]
            try:
                idade = int(partes[1])
            except ValueError:
                print(f"Idade inválida para {nome}. Ignorando perfil.")
                continue 

            cidade = partes[2]
            estado = partes[3]
            amigos = set(partes[4:]) if len(partes) > 4 else set()
            perfis[nome] = {
                "idade": idade,
                "localização": (cidade, estado),
                "amigos": amigos
            }

    with open(rede_infnet_path, 'r', encoding='utf-8') as file:
        for line in file:
            partes = line.strip().split('?')
            nome = partes[0]
            if nome in perfis:
                amigos = set(partes[4:]) if len(partes) > 4 else set()
                perfis[nome]["amigos"].update(amigos)

    return perfis

def verificar_popularidade(perfis, usuario):
    contador = 0
    
    for perfil in perfis.values():
        if usuario in perfil["amigos"]:
            contador += 1
            
    if contador > 4:
        print(f"{usuario} é popular!")
    else:
        print(f"{usuario} não é popular.")

base_inicial_path = os.path.join('data', 'base_inicial.txt')
rede_infnet_path = os.path.join('data', 'rede_INFNET.txt')

perfis = carregar_dados(base_inicial_path, rede_infnet_path)

usuario_verificado = "João"
verificar_popularidade(perfis, usuario_verificado)
