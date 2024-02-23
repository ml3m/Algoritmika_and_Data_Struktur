def radix_sort(draw_info, ascending=True):
	lst = draw_info.lst

	def counting_sort(lst, exp1):
		n = len(lst)
		output = [0] * (n)
		count = [0] * (10)

		for i in range(0, n):
			index = (lst[i] // exp1)
			count[(index) % 10] += 1

		for i in range(1, 10):
			count[i] += count[i - 1]

		i = n - 1
		while i >= 0:
			index = (lst[i] // exp1)
			output[count[(index) % 10] - 1] = lst[i]
			count[(index) % 10] -= 1
			i -= 1

		i = 0
		for i in range(0, len(lst)):
			lst[i] = output[i]
			draw_list(draw_info, {i: draw_info.GREEN}, True)
			yield True

	max1 = max(lst)
	exp = 1
	while max1 // exp > 0:
		yield from counting_sort(lst, exp)
		exp *= 10
	return lst