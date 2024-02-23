def count_sort(draw_info, ascending=True):
	lst = draw_info.lst
	count = [0] * (max(lst) + 1)
	for i in lst:
		count[i] += 1
	i = 0
	for j, item in enumerate(count):
		for k in range(item):
			lst[i] = j
			i += 1
			draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
			yield True
	return lst