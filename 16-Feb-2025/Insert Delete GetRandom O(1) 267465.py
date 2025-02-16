# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:
    def __init__(self):
        self.elem = {}

    def insert(self, val: int) -> bool:
        if val in self.elem:
            return False
        self.elem[val] = True
        return True

    def remove(self, val: int) -> bool:
        if val not in self.elem:
            return False
        self.elem.pop(val)
        return True

    def getRandom(self) -> int:
        random_key = random.choice(list(self.elem.keys()))
        return random_key

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()