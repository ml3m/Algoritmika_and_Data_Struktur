def selection_sort(draw_info, ascending=True):
	lst = draw_info.lst

	for i in range(len(lst)):
		min_index = i

		for j in range(i + 1, len(lst)):
			if (lst[j] < lst[min_index] and ascending) or (lst[j] > lst[min_index] and not ascending):
				min_index = j
		lst[i], lst[min_index] = lst[min_index], lst[i]
		draw_list(draw_info, {i: draw_info.GREEN, min_index: draw_info.RED}, True)
		yield True