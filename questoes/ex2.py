usuarios = [
    ["Ana Paula", 28, "Piracicaba", "SP"],
    ["Carlos Silva", 32, "Limeira", "SP"],
    ["Mariana Souza", 25, "São Carlos", "SP"],
    ["João Mendes", 22, "Araraquara", "SP"],
    ["Paula Rocha", 30, "Sorocaba", "SP"]
]

perfis = []

for usuario in usuarios:
    perfil = {
        "nome": usuario[0],
        "idade": usuario[1],
        "localizacao": (usuario[2], usuario[3])
    }
    perfis.append(perfil)

for perfil in perfis:
    print(perfil)
