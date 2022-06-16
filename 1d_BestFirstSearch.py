from queue import PriorityQueue
v = 14

#create a list of lists, each of the list represents ith node's children and it's corresponding cost to the children from that node
graph = [[] for i in range(v)]
# print(graph)

def best_first_search(source, target, n):
    #initially mark all the vertices as not visited by initializing the entire list with False 
	visited = [False] * n

    #Now we have visited the first vertex , so mark it as visited
	visited[0] = True

    #creation of priority queue
	pq = PriorityQueue()

    #Add the source to priority queue
	pq.put((0, source))

    #Iterate the priority queue until it is empty
	while pq.empty() == False:
		# w = pq.get() --> it returns a tuple
		# print(w)
		# u = w[1]
		u = pq.get()[1] #we are accessing the 2nd element of the tuple
		print(u, end=" ")
		if u == target:
			break

		#We will iterate through all the children of the node u, and add each of the child to the priorityQueue and mark them as visited
		for v, c in graph[u]:
			if visited[v] == False:
				visited[v] = True
				pq.put((c, v))
	print()


def addedge(x, y, cost):
	#Adding the cost of reaching child y from node x 
	graph[x].append((y, cost))

	#Adding the cost of reaching child x from node y
	graph[y].append((x, cost))

#Creating the graph
'''
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)
'''
addedge(0,1,4)
addedge(0,2,1)
addedge(1,3,1)
addedge(1,4,2)
addedge(2,5,2)
addedge(2,6,3)
addedge(5,7,4)
addedge(5,8,3)
addedge(6,9,1)

# print(graph)
source = 0
target = 9
best_first_search(source, target, v)

# o/p: 0 2 5 6 9 