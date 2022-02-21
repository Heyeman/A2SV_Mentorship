def threeNums(a, n):
	nums = []
	if len(a) == 3:
		if sum(a) == n:
			return a
		else:
			return []
	elif len(a) < 3:
		return []
	elif len(a) > 3:
		for i in range(len(a)-2):
			for j in range(i, len(a)-1):
				for k in range(j,len(a)):
					if a[i] + a[j] + a[k] == n:
						nums.append([a[i], a[j], a[k]])
	return nums




li = [-25, -10, -7, -3, 2, 4, 8, 10]
print(threeNums(li, 0))