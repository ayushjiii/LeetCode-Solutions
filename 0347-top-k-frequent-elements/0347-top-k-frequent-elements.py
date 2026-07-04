class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1 :
            return nums

        counts = {}

        for num in nums :
            if num not in counts :
                counts[num] = 0
            counts[num] += 1

        sorted_nums = sorted(counts.items(),key = lambda x : x[1] ,reverse= True)

        output = []
        for i in range(k) :
            output.append(sorted_nums[i][0])

        return output