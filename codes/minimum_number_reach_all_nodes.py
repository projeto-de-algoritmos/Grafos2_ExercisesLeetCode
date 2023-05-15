from typing import List
from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Cria a representação da lista de adjacências do grafo
        graph = defaultdict(list)
        # Acompanha a contagem de arestas recebidas para cada nó
        incoming = [0] * n  
        
        # Adiciona "to_node" à lista de adjacência do "from_node" e incrementamos a contagem "to_node"
        for from_node, to_node in edges:
            graph[from_node].append(to_node)
            incoming[to_node] += 1
        
        smallest_set = []
        
        # Encontrar os vértices sem arestas de entrada
        for i in range(n):
            if incoming[i] == 0:
                smallest_set.append(i)
        
        return smallest_set
