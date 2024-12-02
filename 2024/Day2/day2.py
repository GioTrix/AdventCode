"""

AdventCode2024 - Day 2 part 1

"""

# Lettura del file "data2.txt"
file_path = "data2.txt"

# Creazione della matrice
matrice = []
with open(file_path, 'r') as file:
    for line in file:
        matrice.append(list(map(int, line.split())))

# Funzione per verificare se la distanza tra gli elementi è tra 1 e 3
def verifica_distanze(riga):
    for i in range(len(riga) - 1):
        if not (1 <= abs(riga[i] - riga[i + 1]) <= 3):
            return False
    return True

# Controllo righe sicure
sicuro = 0

for riga in matrice:
    crescente = all(riga[i] < riga[i + 1] for i in range(len(riga) - 1))
    decrescente = all(riga[i] > riga[i + 1] for i in range(len(riga) - 1))
    
    if (crescente or decrescente) and verifica_distanze(riga):
        sicuro += 1

# Restituzione del numero di righe sicure
print("Numero di righe sicure:"+str(sicuro))
