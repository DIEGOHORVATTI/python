tam_j = 2
tam_i = 5

j=0
while j < tam_j:
  i=0
  j += 1
  while i < tam_i:
    i += 1
    matriz = [[""]*i for _ in range(j)]

print("\n Tipo:", type(matriz), "\n", matriz)

"""  """

letras = [
  ['x', 'u', 'y', 's', 'a'], 
  ['s', 'p', 'i', 'n', 'j']
]

print("\n Tipo:", type(letras), "\n", letras)

j = 0
while j < 2:
  i = 0
  while i < 5:
    print(letras[j][i])
    i += 1
  j += 1