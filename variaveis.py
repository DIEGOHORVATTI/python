""" tipos de dados | fim de linha"""
um = 1; print(um)
dois = "2"
print(dois)

umDois = 1.2
print(umDois)

quatro=cinco=seis=sete=0
print(quatro)

""" concatenação """
print(um, int(dois), umDois)
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
if int(teclado) < 5:
  print("Menor que cinco")
elif int(teclado) == 5:
  print("Iqual a cinco")
else:
  print("Maior que cinco")