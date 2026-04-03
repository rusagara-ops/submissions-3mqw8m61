class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False

    def addword(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for wordd in words:
            root.addword(wordd)

        rows = len(board)
        cols = len(board[0])
        result = set()
        visited = set()

        def dfs(r,c,curr,word):
            if (r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited or board[r][c] not in curr.children):
                return

            visited.add((r,c))
            curr = curr.children[board[r][c]]
            word += board[r][c]
            if curr.isword:
                result.add(word)

            dfs(r+1,c,curr,word)
            dfs(r,c+1,curr,word)
            dfs(r-1,c,curr,word)
            dfs(r,c-1,curr,word)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root, "")

        return list(result)
            




        