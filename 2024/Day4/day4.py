'''

Advent of code 2024 - Day 4

'''

#Parte 1: Conta le occorrenze di XMAS in tutte le direzioni.
def count_occurrences(grid, word):
    word_len = len(word)
    count = 0

    # Definizione delle direzioni
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for row in range(n_rows):
        for col in range(n_cols):
            for dx, dy in directions:
                if all(
                    0 <= row + i * dx < len(grid) and
                    0 <= col + i * dy < len(grid[0]) and
                    grid[row + i * dx][col + i * dy] == word[i]
                    for i in range(word_len)
                ):
                    count += 1
    return count


#parte 2: Conta le occorrenze di X-MAS.
def count_x_mas(grid):
    mas = ["MAS", "SAM"]
    count = 0

    for row in range(1, n_rows - 1):
        for col in range(1, n_cols - 1):
            # Controlla le due diagonali centrali:
            # Diagonale principale
            d1 = grid[row - 1][col - 1] + grid[row][col] + grid[row + 1][col + 1]
            # Diagonale opposta
            d2 = grid[row - 1][col + 1] + grid[row][col] + grid[row + 1][col - 1]

            # Verifica che entrambe siano "MAS" o "SAM"
            if d1 in mas and d2 in mas:
                count += 1

    return count


if __name__ == '__main__':
    with open("data.txt") as f:
        grid = [list(line.strip()) for line in f]
    
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    xmas_count = count_occurrences(grid, "XMAS")
    x_mas_count = count_x_mas(grid)

    # Risultati
    print("Numero di occorrenze di XMAS:", xmas_count)
    print("Numero di occorrenze di X-MAS:", x_mas_count)
