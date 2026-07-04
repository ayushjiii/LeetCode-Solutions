class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}

        for index,current_number in enumerate(nums) :
            missing_number = target - current_number

            if missing_number in seen_numbers:
                return [index,seen_numbers[missing_number]]
            
            seen_numbers[current_number] = index