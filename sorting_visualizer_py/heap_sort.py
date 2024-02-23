def heap_sort(draw_info, ascending=True):
	lst = draw_info.lst

	def heapify(lst, n, i):
		largest = i
		l = 2 * i + 1
		r = 2 * i + 2

		if l < n and lst[i] < lst[l]:
			largest = l

		if r < n and lst[largest] < lst[r]:
			largest = r

		if largest != i:
			lst[i], lst[largest] = lst[largest], lst[i]
			draw_list(draw_info, {i: draw_info.GREEN, largest: draw_info.RED}, True)
			yield True
			yield from heapify(lst, n, largest)

	def heap_sort(lst, ascending=True):
		n = len(lst)

		for i in range(n, -1, -1):
			yield from heapify(lst, n, i)

		for i in range(n - 1, 0, -1):
			lst[i], lst[0] = lst[0], lst[i]
			draw_list(draw_info, {i: draw_info.GREEN, 0: draw_info.RED}, True)
			yield True
			yield from heapify(lst, i, 0)

		return lst

	yield from heap_sort(lst, ascending)
	return lst