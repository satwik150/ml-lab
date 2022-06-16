from collections import defaultdict

visited = defaultdict(lambda: False)

j1 , j2 , aim = 4, 3, 2

def waterJug(amt1, amt2):

	#Base condition - if the current already satisfies the solution state 
	if(amt1 == 2 and amt2 == 0) or (amt1 == 0 and amt2 == 2):
		print(amt1, amt2)
		return True

	#if the current state is not visited
	if(visited[(amt1,amt2)] == False):
		print(amt1, amt2)
		visited[(amt1, amt2)] = True

		return (
			waterJug(0,amt2) or
			waterJug(amt1, 0) or
			waterJug(j1, amt2) or
			waterJug(amt1, j2) or
			waterJug(amt1 + min(amt2, j1 - amt1), amt2 - min(amt2, j1 - amt1)) or
			waterJug(amt1 - min(amt1, j2 - amt2), amt2 + min(amt1, j2 - amt2))
		)
	else:
		return False

waterJug(0,0)