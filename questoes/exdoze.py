import os

def carregar_dados():
    perfis = {}
    
    rede_infnet_path = os.path.join('data', 'rede_INFNET.txt')
    with open(rede_infnet_path, 'r', encoding='utf-8') as file:
        next(file)
        for linha in file:
            partes = linha.strip().split('?')
            usuario = partes[0]

            try:
                idade = int(partes[1])
                localizacao = (partes[2], partes[3])
                amigos = set(partes[4:]) if len(partes) > 4 else set()
                
                perfis[usuario] = {
                    "idade": idade,
                    "localização": localizacao,
                    "amigos": amigos
                }
            except ValueError as e:
                print(f"Erro ao processar {usuario}: {e}")
    
    base_inicial_path = os.path.join('data', 'base_inicial.txt')
    with open(base_inicial_path, 'r', encoding='utf-8') as file:
        next(file)
        for linha in file:
            partes = linha.strip().split('?')
            usuario = partes[0]

            try:
                idade = int(partes[1])
                localizacao = (partes[2], partes[3])
                amigos = set(partes[4:]) if len(partes) > 4 else set()
                
                if usuario in perfis:
                    perfis[usuario]["amigos"].update(amigos)
                else:
                    perfis[usuario] = {
                        "idade": idade,
                        "localização": localizacao,
                        "amigos": amigos
                    }
            except ValueError as e:
                print(f"Erro ao processar {usuario}: {e}")
    
    return perfis

def remover_amigo(perfis, usuario, amigo):
    if usuario in perfis:
        if amigo in perfis[usuario]["amigos"]:
            perfis[usuario]["amigos"].remove(amigo)
            print(f"{amigo} foi removido da lista de amigos de {usuario}.")
        else:
            print(f"{amigo} não é amigo de {usuario}.")
    else:
        print(f"O usuário {usuario} não existe.")

def salvar_dados(perfis):
    with open('data/rede_INFNET_atualizado.txt', 'w', encoding='utf-8') as file:
        file.write("Usuário?Idade?Localização?Amigos\n")
        for usuario, dados in perfis.items():
            amigos = '?'.join(dados["amigos"])
            localizacao = '?'.join(dados["localização"])
            file.write(f"{usuario}?{dados['idade']}?{localizacao}?{amigos}\n")

def main():
    perfis = carregar_dados()
    
    usuario = input("Digite o nome do usuário: ")
    amigo = input("Digite o nome do amigo a ser removido: ")

    remover_amigo(perfis, usuario, amigo)

    salvar_dados(perfis)

if __name__ == "__main__":
    main()
