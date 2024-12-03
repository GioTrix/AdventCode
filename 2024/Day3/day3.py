'''

Advent of Code 2024 - Day 3 part 1

'''

import re

file_path = "data3.txt"

total_sum = 0

# Lettura file
with open(file_path, "r") as f:
    for line in f:
        line = line.strip()

        # Trova tutte le occorrenze del pattern mul(X,Y), dove X e Y sono numeri validi
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, line)  # Trova tutte le coppie di numeri

        # Processa le coppie trovate
        for m in matches:
            x, y = map(int, m)  # Converte le stringhe in numeri interi
            prod = x * y  
            total_sum += prod 

# Stampa il risultato finale
print(f"La somma totale: {total_sum}")
