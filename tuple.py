import os
os.system('clear')

onePiece_1 = ("Luffy", "Zoro", "Usoop", "Nami", "Robin")
onePiece_2 = list(onePiece_1)
onePiece_2.append("Brook")
onePiece_1 = tuple(onePiece_2)

for x in onePiece_1:
    print(x)
print('\n')