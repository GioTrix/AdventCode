"""

AdventCode2024 - Day 2 part 2

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

# Funzione per controllare se una riga è crescente o decrescente
def controlla_crescita(riga):
    crescente = all(riga[i] < riga[i + 1] for i in range(len(riga) - 1))
    decrescente = all(riga[i] > riga[i + 1] for i in range(len(riga) - 1))
    return crescente or decrescente

# Funzione per verificare se una riga è sicura (dopo aver rimosso un elemento)
def riga_sicura(riga):
    if controlla_crescita(riga) and verifica_distanze(riga):
        return True
    # Prova a rimuovere ogni elemento e controlla se la riga risultante è sicura
    for i in range(len(riga)):
        nuova_riga = riga[:i] + riga[i+1:]
        if controlla_crescita(nuova_riga) and verifica_distanze(nuova_riga):
            return True
    return False

# Controllo righe sicure
sicuro = 0

for riga in matrice:
    if riga_sicura(riga):
        sicuro += 1

# Restituzione del numero di righe sicure
print(f"Numero di righe sicure: {sicuro}")
