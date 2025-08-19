# Problema 5 – A* (10p)
# a) Explicați algoritmul A* în comentarii
#   Algoritmul A* incearca sa afle cea mai scurta distanta dintre 2 puncte folosind heuristica. Spre deosebire de Dijskastra,
#foloseste o aproximare (euristica) prin care analizeaza mai intai optiunile date ca fiind cele mai scurte, scurtand astfel
#timpul de gandire. Practic, din heap ar fi analizate mai intai optiunile unde heuristica aproximeaza cel mai scurt drum
#Dupa ce am gasit cel mai scurt drum pana la un vecin, analizam mai intai heuristica de la acel vecin spre destinatie sa vedem
#daca aceea este cea mai buna optiune.

# b) Implementați A* pe un grid 3x3 cu obstacol în centru
import heapq
from heapq import heappush, heappop

Grid = list[list[int]]

def heuristic(a, b):
    (x1, y1), (x2, y2) = a, b
    return abs(x1 - x2) + abs(y1 - y2)

def astar(grid: Grid, start: tuple[int,int], goal: tuple[int,int]):
    heap = [start]
    venit = [start]
    cost = [start]

    while heap:
        _, current_node = heapq.heappop(heap)
        if current_node == goal[1]:
            break

        for neighbor, c in grid[current_node]:
            new_cost = cost[current_node] + c
            if cost[neighbor] not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                venit[neighbor] = neighbor
                priority = new_cost + heuristic(neighbor)
                heapq.heappush(heap, priority)
    return venit, cost

if __name__ == "__main__":
    grid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    print(astar(grid, (0,0), (2,2)))

#Inteleg ca nu merge. Problema e ca am lucrat aproape deloc cu tuple si nu inteleg exact ce si cum trebuie sa rezolv. Nu prea
#inteleg si functia heuristic si nu prea am timp de debug. Am incercat