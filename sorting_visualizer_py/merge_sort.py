def merge_sort(draw_info, ascending=True):
	lst = draw_info.lst

	def merge(lst, l, m, r):
		n1 = m - l + 1
		n2 = r - m

		L = [0] * (n1)
		R = [0] * (n2)

		for i in range(0, n1):
			L[i] = lst[l + i]

		for j in range(0, n2):
			R[j] = lst[m + 1 + j]

		i = 0
		j = 0
		k = l

		while i < n1 and j < n2:
			if (L[i] <= R[j] and ascending) or (L[i] >= R[j] and not ascending):
				lst[k] = L[i]
				i += 1
			else:
				lst[k] = R[j]
				j += 1
			k += 1
			draw_list(draw_info, {k: draw_info.GREEN}, True)
			yield True

		while i < n1:
			lst[k] = L[i]
			i += 1
			k += 1
			draw_list(draw_info, {k: draw_info.GREEN}, True)
			yield True

		while j < n2:
			lst[k] = R[j]
			j += 1
			k += 1
			draw_list(draw_info, {k: draw_info.GREEN}, True)
			yield True
			return lst

	def merge_sort(lst, l, r, ascending=True):
		if l < r:
			m = (l + (r - 1)) // 2

			yield from merge_sort(lst, l, m, ascending)
			yield from merge_sort(lst, m + 1, r, ascending)
			yield from merge(lst, l, m, r)

	yield from merge_sort(lst, 0, len(lst) - 1, ascending)
	return lst