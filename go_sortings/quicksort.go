
func QuickSort[T any](array []T, less func(T, T) bool) {
	if len(array) <= 1 {
		return
	}

	var mid int = positionPivotLomuto(array, less)
	QuickSort(array[:mid], less)

	if mid+1 < len(array) {
		QuickSort(array[mid+1:], less)
	}
}

func QuickSort3way[T any](array []T, less func(T, T) bool) {
	if len(array) <= 1 {
		return
	}

	var middle_start, middle_end int = positionPivot3way(array, less)
	QuickSort(array[:middle_start], less)

	if middle_end+1 < len(array) {
		QuickSort(array[middle_end+1:], less)
	}
}

func positionPivotLomuto[T any](array []T, less func(T, T) bool) int {
	if len(array) <= 1 {
		return 0
	}

	end := len(array) - 1

	var greaterElemsIndex int = 0

	for i := 0; i < end; i++ {
		if !less(array[i], array[end]) {
			continue
		}

		if i != greaterElemsIndex {
			array[i], array[greaterElemsIndex] = array[greaterElemsIndex], array[i]
		}

		greaterElemsIndex++
	}

	if end != greaterElemsIndex {
		array[end], array[greaterElemsIndex] = array[greaterElemsIndex], array[end]
	}

	return greaterElemsIndex
}

func positionPivotHoare[T any](array []T, less func(T, T) bool) int {
	length := len(array)
	if length <= 1 {
		return 0
	}

	var pivot *T = &array[length-1]
	var low, high int = 0, length - 2

	for low < high {
		if !less(array[low], *pivot) && less(array[high], *pivot) {
			array[low], array[high] = array[high], array[low]
			low++
			high--
			continue
		}

		if less(array[low], *pivot) {
			low++
		}

		if !less(array[high], *pivot) {
			high--
		}
	}

	if less(array[low], *pivot) {
		low++
	}
	array[length-1], array[low] = array[low], array[length-1]

	return low
}

func positionPivot3way[T any](array []T, less func(T, T) bool) (int, int) {
	if len(array) <= 1 {
		return 0, 0
	}

	end := len(array) - 1

	var greaterOrEqualIndex int = 0

	for i := 0; i < end; i++ {
		if !less(array[i], array[end]) {
			continue
		}

		if i != greaterOrEqualIndex {
			array[i], array[greaterOrEqualIndex] = array[greaterOrEqualIndex], array[i]
		}

		greaterOrEqualIndex++
	}

	var equalElemsIndex int = end - 1

	for i := end - 1; i >= greaterOrEqualIndex; i-- {
		// pivot >= array[i]
		if !less(array[end], array[i]) {
			continue
		}

		if i != equalElemsIndex {
			array[i], array[equalElemsIndex] = array[equalElemsIndex], array[i]
		}
		equalElemsIndex--
	}

	equalElemsIndex++

	if end != equalElemsIndex {
		array[end], array[equalElemsIndex] = array[equalElemsIndex], array[end]
	}

	return greaterOrEqualIndex, equalElemsIndex
}
