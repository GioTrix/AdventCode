from collections import defaultdict

def leggi_file():
    regole = defaultdict(list)
    ordini = []
    with open('data.txt', 'r') as f:
        for riga in f:
            riga = riga.strip()
            if '|' in riga:  # Regola di ordinamento
                sinistra, destra = map(int, riga.split('|'))
                regole[sinistra].append(destra)  
            elif riga:  # Ordine
                ordini.append(list(map(int, riga.split(','))))
    return regole, ordini

def ordine_valido(ordine, regole):
    for i in range(len(ordine) - 1):
        if ordine[i] not in regole or ordine[i + 1] not in regole[ordine[i]]:
            return False
    return True

def correggi_ordine(ordine, regole):
    while not ordine_valido(ordine, regole):
        for i in range(len(ordine) - 1):
            if ordine[i] not in regole or ordine[i + 1] not in regole[ordine[i]]:
                ordine[i], ordine[i + 1] = ordine[i + 1], ordine[i]
    return ordine

def calcola_somma_centrali(ordini):
    return sum(ordine[len(ordine) // 2] for ordine in ordini)

if __name__ == '__main__':
    # Lettura file e separa regole e ordini
    regole, ordini = leggi_file()

    # Dividi in ordini validi e non validi
    ordini_validi = [ordine for ordine in ordini if ordine_valido(ordine, regole)]
    ordini_non_validi = [ordine for ordine in ordini if not ordine_valido(ordine, regole)]

    # Calcola la somma dei valori centrali degli ordini validi
    somma_validi = calcola_somma_centrali(ordini_validi)
    print(f"Somma dei valori centrali: {somma_validi}")

    # Correggi gli ordini non validi
    ordini_corretti = [correggi_ordine(ordine, regole) for ordine in ordini_non_validi]

    # Calcola la somma dei valori centrali degli ordini corretti
    somma_corretti = calcola_somma_centrali(ordini_corretti)
    print(f"Somma dei valori centrali corretti: {somma_corretti}")
