'''

Advent of Code 2024 - Day 3

'''

import re

with open('data3.txt') as f:

    string = f.read()
    
    # Pattern per trovare le espressioni "mul(x, y)"
    pattern = r'mul\((\d+),(\d+)\)'
    
    # Trova tutte le corrispondenze con il pattern nel testo
    matches = re.findall(pattern, string)
    
    sum1 = 0
    for m in matches:
        sum1 += (int(m[0]) * int(m[1])) 
    
    # Stampa la somma per la parte 1
    print(f"La somma parte 1: {sum1}")
    
    # Sostituisce tutte le occorrenze di "don't() e do()" con una stringa vuota
    filtered_text = re.sub(r"don't\(\).*?do\(\)", "", string, flags=re.DOTALL)
    
    matches = re.findall(pattern, filtered_text)

    sum2 = 0
    for m in matches:
        sum2 += (int(m[0]) * int(m[1]))
        
    # Stampa la somma per la parte 2    
    print(f"La somma parte 2: {sum2}")
