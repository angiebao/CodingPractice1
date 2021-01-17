Def findFriendCircle(self, Matrix):
	Map = defaultdict(set)
	self.init(Matrix, map)

	Visited = [False for i in range(len(matrix))]

	Cnt = 0

	# there are len(matrix) of people to loop through

	For i in range(len(Matrix)):
		If not visited[i]:
		self.dfs(i, map, visited)
		Cnt +=  1

	Return cnt

Def dfs(self, i, map, visited):
	Visited[i] = True
	For nxt in map[i]:
		If not visited[nxt]:
			Visited[nxt] = True
			self.dfs(nxt, map, visited)

Def init(self, matrix, map):
	For i in range(len(Matrix)):
		For j in range(len(Matrix)):
If Matrix[i][j] == 1:
map[i].add(j)
map[j].add(i)