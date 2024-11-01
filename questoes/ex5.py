def carregar_perfis_validos(arquivo):
    perfis_validos = []

    with open(arquivo, 'r', encoding='utf-8') as file:
        for linha in file:
            dados = linha.strip().split('?')

            if len(dados) >= 5 and dados[0]:
                perfil = {
                    "nome": dados[0],
                    "idade": int(dados[1]) if dados[1].isdigit() else None,
                    "localização": (dados[2], dados[3]),
                    "amigos": dados[4:]
                }

                perfis_validos.append(perfil)

    return perfis_validos

arquivo_base = './data/base_inicial.txt'

perfis_validos = carregar_perfis_validos(arquivo_base)

print("Perfis válidos:")
for p in perfis_validos:
    print(p)
