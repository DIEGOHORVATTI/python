# parametros referencia
def soma(x, y):
  print(int(x+y))

soma(2, 2)
print("\n")

# parametros abtrarios
def soma(*x):
  cache=0
  for y in x: 
    y += cache
    cache=y
  print(int(y))
soma(2, 10, 10)
print("\n")

# parametros defult
def livros(title="The seven legends"):
  print(title)
livros()
livros("Linux a biblia")