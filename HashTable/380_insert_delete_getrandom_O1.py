import collections
import random


import collections
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyMap = dict()
        self.valueMap = dict()
        self.id = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.keyMap:
            return False
        else:
            n = len(self.keyMap)
            self.keyMap[val] = n
            self.valueMap[n] = val

            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.keyMap:
            return False
        else:
            # 6 对应的是 1 in key map, 找到之后把6删除就可以了，因为我们已经得到 key = 1， 接下来只需要把8 对应的 key 变掉就可以了
            key = self.keyMap[val]
            self.keyMap.pop(val)
            # if val is the last one, simply remove Else move the last one to current vacancy.
            n = len(self.valueMap)
            if key == n - 1:
                self.valueMap.pop(key)
            else:
                self.valueMap[key] = self.valueMap[n - 1]
                self.keyMap[self.valueMap[n - 1]] = key
                self.valueMap.pop(n - 1)
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        randIdx = random.randint(0, len(self.valueMap))
        print(self.valueMap)
        print(randIdx)
        return self.valueMap[randIdx]



# Your RandomizedSet object will be instantiated and called as such:
["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
# [[],[1],[2],[2],[],[1],[2],[]]
# ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
# [[],                [0],     [1],     [0],     [2],     [1],     []]

obj1 = RandomizedSet()
print(obj1.insert(0))
print(obj1.insert(1))
print(obj1.remove(0))
print(obj1.insert(2))
print(obj1.remove(1))
print(obj1.getRandom())

# obj2 = RandomizedSet()
# print(obj2.insert(1))
# print(obj2.remove(2))
# print(obj2.insert(2))
# print(obj2.getRandom())
# print(obj2.remove(1))
# print(obj2.remove(2))
# print(obj2.getRandom())

