# input
stack = [2,5,8,5,5,5]

# push , pop, getmax
import collections

class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        #self.q = collections.deque()
        self.q = []
        self.s = []
        #sliding window , 小于栈顶 不append
    def push(self, x):

        if not self.q or self.q[-1] <= x:
            self.q.append(x)

        self.s.append(x)

    def pop(self):
        x = self.s.pop()
        if self.q[-1] ==x:
            self.q.pop()
        return x
    def getMax(self):
        return self.q[-1]



MS = MaxStack()
MS.push(3);
MS.push(5);
MS.push(2);
MS.push(4);
print(MS.getMax()); #-> 5
print(MS.pop()); #-> 4
print(MS.pop()); #-> 2
print(MS.getMax()); # -> 5

print(MS.pop()); #-> 5
print(MS.getMax()); # ->3