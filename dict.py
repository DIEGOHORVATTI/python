mangakas = {
  "Eiichiro oda": "One Piece",
  "Masashi kishimoto" : "Naruto",
  "Turtleme" : "The Beginning After The End"
}

mangakas["Kentaro Miura"] = "Berserk"

print(mangakas["Masashi kishimoto"]) #print(mangakas.get("Masashi kishimoto"))

mangakas["Masashi kishimoto"] = "Boruto"

print("\n", mangakas, "\n")

for x in mangakas:
  print(x, ":", mangakas[x])   # chave, valor
print("\n")

for c,v in mangakas.items():
  print(c, ":", v)   # chave, valor

mangakas = {
  "Eiichiro oda":{
    "Naruto": 1999,
    "Boruto": 2015
  }
}

print("\n", mangakas["Eiichiro oda"], "\n")
print(
  "\n", 
  list(mangakas["Eiichiro oda"].keys())[ 
    (list(mangakas["Eiichiro oda"].values()).index(1999)) 
  ],
  ":", 
  mangakas["Eiichiro oda"]["Naruto"], 
  "\n"
)

letra_1 = { 1:"a" }

letra_2 = { 2: "b" }

letra_3 = { 3: "c" }

letras = {
  "L_1": letra_1,
  "L_2": letra_2,
  "L_3": letra_3
}

print(type(letras), ":" ,letras)