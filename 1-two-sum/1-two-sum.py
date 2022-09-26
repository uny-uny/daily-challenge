class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for index, value in enumerate(nums):
            remaining = target - nums[index]
            if remaining in dic:
                return [index, dic[remaining]]
            dic[value] = index