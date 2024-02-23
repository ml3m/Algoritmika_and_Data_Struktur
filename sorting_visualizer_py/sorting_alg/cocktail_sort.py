def cocktail_sort(draw_info, ascending=True):
	lst = draw_info.lst

	def cocktail_shaker_sort(lst, ascending=True):
		n = len(lst)
		swapped = True
		start = 0
		end = n - 1

		while swapped:
			swapped = False

			for i in range(start, end):
				if (lst[i] > lst[i + 1] and ascending) or (lst[i] < lst[i + 1] and not ascending):
					lst[i], lst[i + 1] = lst[i + 1], lst[i]
					swapped = True
					draw_list(draw_info, {i: draw_info.GREEN, i + 1: draw_info.RED}, True)
					yield True

			if not swapped:
				break

			swapped = False
			end -= 1

			for i in range(end - 1, start - 1, -1):
				if (lst[i] > lst[i + 1] and ascending) or (lst[i] < lst[i + 1] and not ascending):
					lst[i], lst[i + 1] = lst[i + 1], lst[i]
					swapped = True
					draw_list(draw_info, {i: draw_info.GREEN, i + 1: draw_info.RED}, True)
					yield True

			start += 1

		return lst

	yield from cocktail_shaker_sort(lst, ascending)
	return lst
    