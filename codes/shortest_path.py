import heapq
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # Máscara binária representando todos os nós visitados
        target_mask = (1 << n) - 1 
        
        # Cria uma fila de prioridade para armazenar os estados (nó, máscara, distância)
        queue = [(0, i, 1 << i) for i in range(n)]
        
        # Cria uma tabela de distâncias para acompanhar as distâncias mínimas
        distance = [[float('inf')] * (1 << n) for _ in range(n)]
        
        # Inicialize a distância para os nós iniciais em 0
        for i in range(n):
            distance[i][1 << i] = 0
        
        while queue:
            dist, node, mask = heapq.heappop(queue)
            
            if mask == target_mask:
                return dist
            
            if dist > distance[node][mask]:
                continue
            
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                new_dist = dist + 1
                
                if new_dist < distance[neighbor][new_mask]:
                    distance[neighbor][new_mask] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor, new_mask))
        
        return -1  # Nenhum caminho válido encontrado
