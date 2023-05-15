from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]  # Gráfico direcionado representando relacionamentos mais ricos
        result = [-1] * n  # Guarda a resposta no array
        
        # Constroi o gráfico
        for x, y in richer:
            graph[y].append(x)
        
        # Função DFS para achar a pessoa menos quieta
        def dfs(person):
            if result[person] >= 0:
                return result[person]
            
            result[person] = person  # Initializa o resultadi com a pessoa atual

            for neighbor in graph[person]:
                if quiet[result[person]] > quiet[dfs(neighbor)]:
                    result[person] = result[neighbor]
            
            return result[person]
        
        # Chama a função DFS para cada pessoa
        for person in range(n):
            dfs(person)
        
        return result
