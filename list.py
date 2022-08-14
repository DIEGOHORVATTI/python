onePiece = ["Luffy", "Zoro", "Usoop", "Nami", "Robin"]
onePiece.append("Brook")
onePiece.append("Sanji")
onePiece.append("Choop")
onePiece.append("Jinbe")
onePiece.append("Frank")
onePiece.append("Oden")

onePiece.remove("Jinbe") # remover elemento por id
onePiece.pop()           # remover ultimo elemento
del onePiece[2]          # remover por indezação
# onePiece.clear()

eiichiroOda = list(onePiece) # passar lista para outra variável
naruto = ["naruto", "sasuke", "hinata", "kakashi"]

# juntar lista
shonnenJump = onePiece+naruto

print(eiichiroOda, len(eiichiroOda), type(eiichiroOda))
for x in eiichiroOda:
  print(x)
print("\n")

print(shonnenJump, len(shonnenJump), type(shonnenJump))
for x in shonnenJump:
  print(x)