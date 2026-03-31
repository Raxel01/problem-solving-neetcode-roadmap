class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if hashMap.get(num, None) != None:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        return list(dict(sorted(hashMap.items(), key=lambda item: item[1])).keys())[-k:]

        