class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultindex = 0
        resultlength = 0

        for i in range(len(s)):
            # when odd
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultlength:
                    resultlength = (r - l + 1)
                    resultindex = l

                l -= 1
                r += 1

            # when even
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultlength:
                    resultlength = (r - l + 1)
                    resultindex = l

                l -= 1
                r += 1

        return s[resultindex : (resultindex + resultlength)]
