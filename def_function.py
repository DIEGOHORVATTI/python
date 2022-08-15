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

# parametros referencia
def soma(x, y):
  return(int(x+y))
print("\n", soma(2, 2), "\n")

# função anônima 
soma = lambda x,y : x+y
print("\n", soma(10, 10), "\n\n", ((lambda x,y : x-y)(4, 2)) )

r = lambda x,func : (x+func(x))
res = r(2, lambda x:x+3)
print("\n", res)