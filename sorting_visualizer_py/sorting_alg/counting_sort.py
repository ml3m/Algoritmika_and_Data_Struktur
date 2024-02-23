def counting_sort(draw_info, ascending=True):
	lst = draw_info.lst
	max_val = max(lst)
	min_val = min(lst)
	range1 = max_val - min_val + 1
	count = [0] * range1
	output = [0] * len(lst)

	for i, item in enumerate(lst):
		count[item - min_val] += 1

	for i in range(1, len(count)):
		count[i] += count[i - 1]

	for i in range(len(lst) - 1, -1, -1):
		output[count[lst[i] - min_val] - 1] = lst[i]
		count[lst[i] - min_val] -= 1
		draw_list(draw_info, {i: draw_info.GREEN, count[lst[i] - min_val]: draw_info.RED}, True)
		yield True

	for i in range(len(lst)):
		lst[i] = output[i]
		draw_list(draw_info, {i: draw_info.GREEN}, True)
		yield True

	return lst