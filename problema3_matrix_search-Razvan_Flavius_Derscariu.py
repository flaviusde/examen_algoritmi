# Problema 3 – Căutare într-o matrice sortată (15p)

from typing import List

def search_sorted_matrix(mat: List[List[int]], x: int) -> bool:
    if mat is None:     # Daca matricea e None, returnez False
        return False

    rows, cols = len(mat), len(mat[0])  #randul e fiecare lista in parte, coloana e fiecare pozitie dintr-o lista
    row, col = 0, cols-1    #incep de la primul rand(deci prima lista) si de ultima coloana, deci coltul dreapta sus

    while row < rows and col >= 0:  #cat timp n-am ies inafara matricei, sa tot caut
        if mat[row][col] == x:  #daca am gasit, returnez True
            return True
        elif mat[row][col] > x: #daca valoarea unde caut e mai mare decat targetul, mut coloana in stanga si ma uit acolo
            col -= 1
        else:
            row += 1    #daca pozitia unde caut e mai mica decat targetul, ma uit in randul urmator
    return False

if __name__ == "__main__":
    mat = [
        [1, 4, 7],
        [2, 5, 9],
        [3, 6, 10]
    ]
    print(search_sorted_matrix(mat, 5))  # True
