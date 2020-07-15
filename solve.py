def solution(lst):

	def Dots(lst):
		d = []
		for i in range(len(lst)):
			for j in range(len(lst[0])):
				if lst[i][j] == ".":
					d.append((i, j))
		return d

	def get_valid(lst, row, col):
		avail = set()
		for i in range(1, 10):
			avail.add(str(i))

		for i in range(9):
			if lst[row][i] in avail:
				avail.remove(lst[row][i])
			if lst[i][col] in avail:
				avail.remove(lst[i][col])

		row_b = (row // 3) * 3
		col_b = (col // 3) * 3

		for i in range(row_b, row_b + 3):
			for j in range(col_b, col_b + 3):
				if lst[i][j] in avail:
					avail.remove(lst[i][j])

		return list(avail)

	def solve(lst, dot):
		if len(dot) == 0:
			return True
		i, j = dot[0]
		val = get_valid(lst, i, j)

		if len(val) == 0:
			return False

		for k in val:
			lst[i][j] = k
			if solve(lst, dot[1:]):
				return True
			lst[i][j] = "."
		return False

	dot = Dots(lst)
	solve(lst, dot)
	return lst

if __name__ == "__main__":

	lst = [	["5","3",".",".","7",".",".",".","."],
			["6",".",".","1","9","5",".",".","."],
			[".","9","8",".",".",".",".","6","."],
			["8",".",".",".","6",".",".",".","3"],
			["4",".",".","8",".","3",".",".","1"],
			["7",".",".",".","2",".",".",".","6"],
			[".","6",".",".",".",".","2","8","."],
			[".",".",".","4","1","9",".",".","5"],
			[".",".",".",".","8",".",".","7","9"]]
	lst = solution(lst)
	for i in lst:
		print(i)