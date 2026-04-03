class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for word in strs:
            sortedWord = "".join(sorted(word))

            if not sortedWord in anagrams:
                anagrams[sortedWord] = [word]
            else:
                anagrams[sortedWord].append(word)
        return anagrams.values()