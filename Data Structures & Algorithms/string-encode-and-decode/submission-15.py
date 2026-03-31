class Solution:
    def __init__(self):
        self.hashmap = {
        }
    def encode(self, strs: List[str]) -> str:
        [self.hashmap.update({index: strs[index]}) for index in range(len(strs))]
        return ""

    def decode(self, s: str) -> List[str]:
        res = list(self.hashmap.values())
        del self.hashmap
        return res
