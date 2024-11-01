import random
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

def encontrar_amigos_em_comum(perfis, usuario1, usuario2):
    amigos_usuario1 = perfis[usuario1]["amigos"]
    amigos_usuario2 = perfis[usuario2]["amigos"]
    
    amigos_em_comum = amigos_usuario1.intersection(amigos_usuario2)
    
    return amigos_em_comum

def main():
    perfis = carregar_dados()

    usuarios = list(perfis.keys())
    usuario1, usuario2 = random.sample(usuarios, 2)

    print(f"Usuário 1: {usuario1}")
    print(f"Usuário 2: {usuario2}")

    amigos_em_comum = encontrar_amigos_em_comum(perfis, usuario1, usuario2)

    if amigos_em_comum:
        print(f"Amigos em comum entre {usuario1} e {usuario2}: {', '.join(amigos_em_comum)}")
    else:
        print(f"{usuario1} e {usuario2} não têm amigos em comum.")

if __name__ == "__main__":
    main()
