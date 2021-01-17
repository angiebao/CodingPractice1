# Def isValidTree(self, lists, n):
# 	Graph = {}
# 	For edge in lists:
# 		_n, v = edge[0], edge[1]
# 		Graph[_n].append(v)
# 		graph[v].append(_n)
#
# 	Visited = set()
# If self.dfs(0, -1, graph, visited):
# Return False
# If len(visited) != n:
# 	Return False
# Return True
#
# Def dfs(self, curr, parent, graph, visited):
# 	visited.add(curr)
# 	For neighbor in graph[curr]:
# 		If neighbor not in visited:
# 			If self.dfs(neighbor, curr, graph, visited):
# 				Return True
# 		Elif neighbor in visited and neighbor != parent:
# 			Return True
# 	Return False
#
# Def isValidTree(self, n, lists):
# 	If n != len(lists) + 1:
# 		Return False
#
# 	If self.numOfConnectedComp(n, lists) != 1:
# 		Return False
# 	Else:
# 		Return True
#
#
# Def numOfConnectedComp(self, n, lists):
# 	Graph = {}
# 	For edge in lists:
# 		_n, v = edge[0], edge[1]
# 		Graph[_n].append(v)
# 		graph[v].append(_n)
# 	Res = 0
# 	Visited = [0] * n # visited = set()
# 	For i in range(n):
# 		If not visited[i]:
# 			 self.dfs(visited, i, graph)
# 			 Res += 1
#
# 	Return res
#
# Def dfs(self, visited, n, graph):
# 	If visited[n] == 1:
# 		Return
# 	Visited[n] = 1
# 	For neighbor in graph[n]:
# 		self.dfs(neighbor, graph, visited)
# 	