from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        # Guarda quais salas já visitei
        visited = [False] * n
        visited[0] = True  # Começa pela primeira sala (0)
        
        queue = [0]  # Fila pra guardar quais salas ainda precisa visitar
        
        while queue:
            # Remove a sala da fila
            room = queue.pop(0)
        
            for key in rooms[room]:
                # Se ainda não tiver visitado a sala, atribui true para o valor de visited
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)
        
        return all(visited)
