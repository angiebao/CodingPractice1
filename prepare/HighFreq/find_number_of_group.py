# uninon find to find the number of groups in the list
class Solution:
    def findGroup(self, arr, n):
        self.parent = [i for i in range(n)]
        for pair in arr:
            if self.is_connected(pair[0], pair[1]) == False:
                self.merge(pair[0], pair[1])
        # this is alreay a set, there will be no repeated values
        group = {self.find(i) for i in range(n)}

        return len(group)



    def find(self, index):
        if self.parent[index] != index:
            root  = self.find(self.parent[index])
            self.parent[index] = root
            return root
        # if parent[index] = index , this is actually a root.
        return index
    def is_connected(self, a, b):
        return self.find(a) == self.find(b)
    def merge(self, a, b ):
        root_a = self.find(a)
        root_b = self.find(b)
        # find the root position in parent, change the value to root b
        self.parent[root_a] = root_b


arr = [[0,1], [1,2], [3,4], [6,7],[2,7],[3,8],[5,8],[9,2],[10,11]]

n = 12
s = Solution()
print(s.findGroup(arr,n ))