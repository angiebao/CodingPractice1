class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        q = deque()
        q.append(beginWord)
        n = len(beginWord)
        res = [beginWord]
        visited = set()
        length = 0

        while q:
            length += 1
            for j in range(len(q)):
                item = q.popleft()
                if item == endWord:
                    return length
                neighbors = self.getNeighbors(item, s, n, visited)
                for neighbor in neighbors:
                    q.append(neighbor)
                    visited.add(neighbor)

        return 0

    def getNeighbors(self, item, s, n, visited):
        res = []
        for i in range(n):
            for c in range(ord('a'), ord('z') + 1):
                cur = item[:i] + chr(c) + item[i + 1:]
                if cur in s and cur not in visited:
                    res.append(cur)

        return res

