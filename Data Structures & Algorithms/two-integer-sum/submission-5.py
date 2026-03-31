class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Bad Time Complexity O(n^2)
        # let improve it !
        hashmap = {}
        target - 2 
        for index in range(len(nums)):
            if hashmap.get(target - nums[index], None) != None:
                return [hashmap.get(target - nums[index]), index]
            else:
                hashmap[nums[index]] = index
        return []
