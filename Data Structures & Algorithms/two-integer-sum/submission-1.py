class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = list()
        for parent in range(len(nums)):
            for child in range(len(nums)):
                if nums[parent] + nums[child] == target and parent != child:
                    if parent > child :
                        indices.extend([child, parent])
                        return indices;
                    else:
                        indices.extend([parent, child])
                        return indices;
        return indices

