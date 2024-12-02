"""

AdventCode2024 - Day1 part 2

"""
file_path = "data1.txt"  

a = []
b = []

# Leggi il contenuto del file
with open(file_path, "r") as f:
    for line in f:
        values = line.split()
        if len(values) == 2:
            a.append(int(values[0]))  # Aggiungi il primo numero alla lista 'a'
            b.append(int(values[1]))  # Aggiungi il secondo numero alla lista 'b'

# Contiamo le occorrenze di ogni numero nella lista 'b'
occurrences_b = {}

# Popoliamo il dizionario con le occorrenze di b
for value in b:
    if value in occurrences_b:
        occurrences_b[value] += 1
    else:
        occurrences_a[value] = 1

# Calcoliamo la similarità
similarita_totale = 0

# Per ogni elemento in 'a', calcoliamo la similarità
for x in a:
    numero_occorrenze = occurrences_b.get(x, 0)  # Ottieni il numero di occorrenze
    similarita = x * numero_occorrenze  # Calcola la similarità
    similarita_totale += similarita  # Somma alla similarità totale

# Restituisce la similarità totale
print("Similarità totale:"+str(similarita_totale))
