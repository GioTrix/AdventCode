"""

AdventCode2024 - Day1 part 1

"""

# Apriamo il file di input
file_path = "data1.txt"

# Leggiamo il file e separiamo i dati in due liste (a e b)
a = []
b = []

# Leggi il contenuto del file
with open(file_path, "r") as f:
    for line in f:
        values = line.split()
        if len(values) == 2:  
            a.append(int(values[0]))  # Aggiungi il primo numero alla lista 'a'
            b.append(int(values[1]))  # Aggiungi il secondo numero alla lista 'b'

# Calcola la somma delle distanze
somma = 0
while len(a) != 0 and len(b) != 0:
    mina = min(a)
    minb = min(b)
    
    distanza = abs(mina - minb)
    
    somma += distanza
    
    a.remove(mina)
    b.remove(minb)

print("Somma totale:", somma)
