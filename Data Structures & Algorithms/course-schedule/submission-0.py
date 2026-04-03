from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[b].append(a)

        processingset = set()
        doneset = set()

        def dfs(node):
            # if not dfs(node):
            #     return False
            if node in processingset:
                return False
            if node in doneset:
                return True
            processingset.add(node)

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            processingset.remove(node)
            doneset.add(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True