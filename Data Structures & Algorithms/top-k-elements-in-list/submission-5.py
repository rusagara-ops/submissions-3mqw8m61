from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)
        frequency = [[] for i in range(len(nums)+1)]

        for num,cnts in counts.items():
            frequency[cnts].append(num)

        result = []

        for i in range(len(frequency)-1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result





        