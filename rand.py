import random

def aleatorio(x):
  print(x, ':', random.randrange(0, 100, 1))

x = 0
while x < 100:
  aleatorio(x)
  x+=1