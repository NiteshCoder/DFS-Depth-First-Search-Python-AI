#Depth First Search 

graph = {
	'A' : ['B','C','D'],
	'B' : ['E'],
	'C' : ['F','G'],
	'D' : ['H'],
	'E' : ['I'],
	'F' : ['J'],
	'I' : [],
	'J' : [],
	'G' : [],
	'H' : [],
}

visited = []

def dfs(visited,graph,node):
	print(node,end=" ")
	if node not in visited:
		visited.append(node)
		for neighbours in graph[node]:
			dfs(visited,graph,neighbours)
				
dfs(visited,graph,'A')

			
'''
#Depth First Search 

graph = {
	'A' : ['B','C','D'],
	'B' : ['E'],
	'C' : ['F','G'],
	'D' : ['H'],
	'E' : ['I'],
	'F' : ['J'],
	'I' : [],
	'J' : [],
	'G' : [],
	'H' : [],
}

visited = []

def dfs(visited,graph,node):
	if 'J' not in visited:
		print(node,end=" ")
		if node not in visited:
			visited.append(node)
			for neighbours in graph[node]:
				dfs(visited,graph,neighbours)
	else:
		pass
		
			
dfs(visited,graph,'A')

			
	
'''
	