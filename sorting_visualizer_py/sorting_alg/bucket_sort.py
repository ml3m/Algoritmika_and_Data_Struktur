from draw_pygame import draw_list

def bucket_sort(draw_info, ascending=True):
	lst = draw_info.lst

	def bucket_sort(lst, ascending=True):
		arr = []
		slot_num = 10
		for i in range(slot_num):
			arr.append([])

		for j in lst:
			index_b = int(slot_num * j)
			arr[index_b].append(j)

		for i in range(slot_num):
			arr[i] = sorted(arr[i])

		k = 0
		for i in range(slot_num):
			for j, item in enumerate(arr[i]):
				lst[k] = item
				k += 1
				draw_list(draw_info, {k: draw_info.GREEN}, True)
				yield True

	yield from bucket_sort(lst, ascending)
	return lst