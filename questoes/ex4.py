perfis = [
    {"nome": "João", "idade": 25, "localização": ("Piracicaba", "SP")},
    {"nome": "Ana", "idade": 22, "localização": ("Limeira", "SP")},
    {"nome": "", "idade": 30, "localização": ("Belo Horizonte", "MG")}, 
    {"nome": "Carlos", "idade": 28, "localização": ("", "PR")},
    {"nome": "Mariana", "idade": 24, "localização": ("São Paulo", "SP")},
]

perfis_validos = []

for perfil in perfis:
    if perfil["nome"] and perfil["localização"][0]:
        perfis_validos.append(perfil)

print("Perfis válidos:")
for p in perfis_validos:
    print(p)
