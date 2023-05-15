import heapq
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target_mask = (1 << n) - 1  # Binary mask representing all nodes visited
        
        # Create a priority queue to store the states (node, mask, distance)
        queue = [(0, i, 1 << i) for i in range(n)]  # (distance, node, mask)
        
        # Create a distance table to keep track of the minimum distances
        distance = [[float('inf')] * (1 << n) for _ in range(n)]
        
        # Initialize the distance for starting nodes to 0
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
        
        return -1  # No valid path found
