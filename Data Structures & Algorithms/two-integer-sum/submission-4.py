class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Bad Time Complexity O(n^2)
        indices = list()
        for parent in range(len(nums)):
            for child in range(parent+1, len(nums)):
                if nums[parent] + nums[child] == target and parent != child:
                        indices.extend([ parent, child])
                        return indices;
        return indices

