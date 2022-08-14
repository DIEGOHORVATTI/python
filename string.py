estado = " Mó sono"

# imprimir posições da string
print(estado[0:len(estado)]) 
print("\n")

# remover espaços string
print(estado.strip())
print("\n")

# string minuscula
print(estado.lower().strip())
print("\n")

# string maiuscula
print(estado.upper().strip())
print("\n")

# string separada em lista
x = estado.strip().split(" ")
print( x )
print( x[1] )
print("\n")

# verificar ocorrencia de palavra em string
ocorrencia = "sono".upper() in estado.upper()
print(ocorrencia, '\n')

# concatenação fácil
city = "Videira"
dia = 14
mes = 8
ano = 2021
data = "{}, {}, {}, {}"
print(data.format(city, dia, mes, ano), '\n')
