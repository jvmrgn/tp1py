import os

def listar_usuarios():
    rede_infnet_path = os.path.join('data', 'rede_INFNET.txt')
    
    try:
        with open(rede_infnet_path, 'r', encoding='utf-8') as file:
            next(file)
            usuarios = []
            for linha in file:
                partes = linha.strip().split('?')
                usuario = partes[0]
                usuarios.append(usuario)
    
        return usuarios
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho do arquivo.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []

def main():
    usuarios = listar_usuarios()
    print("Usuários da rede social:")
    for usuario in usuarios:
        print(usuario)

if __name__ == "__main__":
    main()
