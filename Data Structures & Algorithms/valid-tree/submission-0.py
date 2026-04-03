from collections import defaultdict 
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        visited = set()
        adj = defaultdict(list)
        
        for edge1,edge2 in edges:
            adj[edge1].append(edge2)
            adj[edge2].append(edge1)


        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0,-1) and n == len(visited)

