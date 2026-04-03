class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenset = set()
        l = 0
        length = 0
        res = 0
        
        for j in range(len(s)):
            while s[j] in seenset:
                seenset.remove(s[l])
                l += 1
            seenset.add(s[j])
            length = j - l+1
            res = max(length, res)

        return res