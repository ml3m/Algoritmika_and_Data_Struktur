def shell_sort(draw_info, ascending=True):
	lst = draw_info.lst

	gap = len(lst) // 2

	while gap > 0:
		for i in range(gap, len(lst)):
			temp = lst[i]
			j = i

			while j >= gap and lst[j - gap] > temp and ascending:
				lst[j] = lst[j - gap]
				j -= gap
				draw_list(draw_info, {j: draw_info.GREEN, j - gap: draw_info.RED}, True)
				yield True

			while j >= gap and lst[j - gap] < temp and not ascending:
				lst[j] = lst[j - gap]
				j -= gap
				draw_list(draw_info, {j: draw_info.GREEN, j - gap: draw_info.RED}, True)
				yield True

			lst[j] = temp
			draw_list(draw_info, {j: draw_info.GREEN}, True)
			yield True

		gap //= 2

	return lst