import os

def contar_amigos():
    rede_infnet_path = os.path.join('data', 'rede_INFNET.txt')
    
    try:
        with open(rede_infnet_path, 'r', encoding='utf-8') as file:
            next(file)
            contagem_amigos = {}
            for linha in file:
                partes = linha.strip().split('?')
                usuario = partes[0]
                amigos = partes[4:]
                
                contagem_amigos[usuario] = len(amigos) if amigos else 0
    
        return contagem_amigos
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho do arquivo.")
        return {}
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return {}

def main():
    contagem_amigos = contar_amigos()
    print("Quantidade de amigos de cada usuário:")
    for usuario, quantidade in contagem_amigos.items():
        print(f"{usuario}: {quantidade} amigo(s)")

if __name__ == "__main__":
    main()
