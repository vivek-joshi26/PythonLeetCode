#Two sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
from typing import List


class Solution:
    '''
    def twosum(self, nums: List[int], target: int) -> List[int]:
        list_len = len(nums)
        a = 0
        while(a < list_len - 1):
            b = a + 1
            while(b < list_len):
                if nums[a] + nums[b] == target:
                    return [a,b]
                b += 1
            a += 1
            '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        index = 0
        for n in nums:
            diff = target - n
            if(map.keys().__contains__(diff)):
                return [index,map.get(diff)]
            map[n] = index
            index += 1





s = Solution()
print(s.twoSum([1,2,3,1],5))
