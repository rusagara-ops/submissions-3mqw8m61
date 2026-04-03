class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        frequency = {}
        

        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        
        sorted_elements = sorted(frequency.keys(), key=lambda x:frequency[x], reverse= True)
        return sorted_elements[:k]
    

