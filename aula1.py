usuarios = [
    ["alice", "Alice@gmail.com", 30], 
    ["alysson", "alysson@gmail.com", 19], 
    ["carlos", "carlos@gmail.com", 9], 
    ["leonardo", "leonardo@gmail.com", 67], 
    ["caua", "caua@gmail.com", 22], 
    ["joao", "joao@gmail.com", 18]
]

# 1. O correto é usar "usuario" no singular para não destruir a lista original
for usuario in usuarios:
    print(usuario)

# 2. Uso correto dos colchetes separados para pegar o e-mail do alysson
print(usuarios[0][0])
