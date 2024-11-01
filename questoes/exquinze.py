import os
from collections import defaultdict

def carregar_perfis():
    rede_infnet_path = os.path.join('data', 'rede_INFNET_atualizado.txt')
    
    try:
        perfis = defaultdict(set)
        with open(rede_infnet_path, 'r', encoding='utf-8') as file:
            next(file)
            for linha in file:
                partes = linha.strip().split('?')
                usuario = partes[0]
                amigos = partes[4:]
                
                for amigo in amigos:
                    perfis[amigo].add(usuario)
            
        return perfis
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho do arquivo.")
        return {}
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return {}

def encontrar_usuarios_populares(perfis):
    usuarios_populares = sorted(perfis.items(), key=lambda x: len(x[1]), reverse=True)
    
    return usuarios_populares[:5]

def main():
    perfis = carregar_perfis()
    usuarios_populares = encontrar_usuarios_populares(perfis)

    print("Top 5 usuários mais populares:")
    for usuario, amigos in usuarios_populares:
        print(f"{usuario}: {len(amigos)} amigo(s)")

if __name__ == "__main__":
    main()
