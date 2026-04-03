class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        
        # create our 2d dp table

        dp = [[0] * (cols + 1) for _ in range(rows+1)]

        # then fill the table while exploring the options
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):

                # so if the characters at i and j are equal, we fill our current cell and we gotta add our 1 to the diagonal cell
                # else our current cell is going to be the max betweent the right cell or the bottom one

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        # since we are doing bottom up, then it will all end up at our first cell so we return that after populating everything

        return dp[0][0]

        