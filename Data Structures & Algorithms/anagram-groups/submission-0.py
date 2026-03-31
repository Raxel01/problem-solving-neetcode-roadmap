class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1000 array elemnts
        # string lenght 0 => 100
        # strs are all lowercases
        Hashmap = {}
        for index in range(len(strs)):
            copy = "".join(sorted(strs[index]))
            if Hashmap.get(copy, None) != None:
                Hashmap[copy].append(strs[index])
            else:
                Hashmap[copy] = [strs[index]]
        return list(Hashmap.values())