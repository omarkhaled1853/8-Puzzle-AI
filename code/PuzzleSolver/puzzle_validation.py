def getInvCount(arr):
	inv_count = 0
	for i in range(0, 9):
		for j in range(i + 1, 9):
			if arr[j] != '0' and arr[i] != '0' and int(arr[i]) > int(arr[j]):
				inv_count += 1
	return inv_count

# check if solvable puzzle
def isSolvable(puzzle) :

	# Count inversions
	inv_count = getInvCount(puzzle)

	# return true if inversion count is even.
	return (inv_count % 2 == 0)
