""" tipos de dados | fim de linha"""
from os import system


quatro=cinco=seis=sete=0
print(quatro)

um = 1;           # ineteiro
print(um) 
dois = "2"        # caracter/string
print(dois) 

umDois = 1.2      # bollean
print(umDois)

print("\n")
dadosAbstrato = complex(2, 8)
print(dadosAbstrato.real)     # parte real
print(dadosAbstrato.imag)     # parte imaginaria
print("\n")

# array, list, vetor
personagensJojo = ["Giorno Giovanna", "Funny Valentine", "Jotaro Kujo"]
for x in personagensJojo: 
  print(x)
print("\n")

# Tupla, constvetor
personagensJojo = ("Giorno Giovanna", "Funny Valentine", "Jotaro Kujo")
for x in personagensJojo:
  print(x)
print("\n")

# lista altomática
y = range(10, 20, 1) #list 10 á 20 1 á 1
for x in y:
  print(x)
print("\n")

# Dict, dicionario
artistas = {
  "Eiichiro oda": "One Piece",
  "Masashi kishimoto" : "Naruto",
  "Turtleme" : "The Beginning After The End"
}
print(type(artistas))
print(artistas)
print(artistas["Eiichiro oda"])
print("\n")

# set não imprime o mesmo numero
kapa={4,8,9,3,4,8} # set desbloqueado
kapa = frozenset({4, 8, 9, 3, 4, 8})  # set bloqueado
print(kapa)
print("\n")


""" concatenação """
print(um, dois, umDois)
print(str(um) + " " + str(dois) + " " + str(umDois))

""" operadores aritiméticos """
a = 5
b = 2
c = pow(2, 3)
print("a + b = ", a+b)
print("a - b = ", a-b)
print("a * b = ", a*b)
print("a / b = ", a/b)
print("pow(c) = ", c)

""" Ler do teclado """
teclado = input("\nDigite um numero: ")
if int(teclado) == 0:
  system("clear && python variaveis.py")
elif int(teclado) < 5:
  print("Menor que cinco")
elif int(teclado) == 5:
  print("Iqual a cinco")
else:
  print("Maior que cinco")