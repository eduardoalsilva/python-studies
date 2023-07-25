generos = ['policial', 'indefinido', 'terror', 'suspense', 'amor']

for genero in generos:
    print(genero)

generos[-1] = 'romantico'

print("Gêneros:")
for i, genero in enumerate(generos):
    print(i + 1, '=>', genero.capitalize())
