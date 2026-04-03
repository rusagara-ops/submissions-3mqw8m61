class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path, opencount, closecount):

            if len(path) == 2*n:
                result.append("".join(path))
                return

            if opencount < n:
                path.append("(")
                backtrack(path, opencount + 1, closecount)
                path.pop()

            if closecount < opencount:
                path.append(")")
                backtrack(path, opencount, closecount+1)
                path.pop()

        backtrack([],0,0)

        return result

                

