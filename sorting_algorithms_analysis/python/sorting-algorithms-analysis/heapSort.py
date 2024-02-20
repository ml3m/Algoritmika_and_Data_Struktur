#!/usr/bin/python

## MODIFIED HEAP SORT

# Input : Array of Integers - arr
# Output : Returns sorted array

def heapSort(arr,low,high) :
	heap = []
	top = 0
	for i in range(0,high+1) :
		top=top+1
		_insertHeap(heap,top,arr[i])
	# print(heap)
	for i in range(0,high+1) :
		arr[i]=_removeHeap(heap,top)
		#sortedArr.append(_removeHeap(heap,top))
		top=top-1
	#arr = sortedArr
	#print(sortedArr)


def _removeHeap(heap,top):
	minimum = heap[0]
	heap[0] = heap[top-1]
	currentIndex = 1

	while currentIndex < top :
		## 2 child exist
		if currentIndex*2+1<=top :
			if heap[currentIndex-1]<=heap[currentIndex*2-1] and heap[currentIndex-1] <= heap[currentIndex*2] :
				return minimum
			else:
				if(heap[currentIndex*2] < heap[currentIndex*2-1]) :
					j=currentIndex*2 +1
				else:
					j=currentIndex*2
				swap(heap,currentIndex-1,j-1)
				currentIndex=j
		else:
			## one node
			if currentIndex*2<=top :
				if heap[currentIndex-1]<=heap[currentIndex*2-1] :
					swap(heap,currentIndex-1,currentIndex*2-1)
			return minimum
	return minimum


	
def _insertHeap(heap,currentIndex,value) :
	heap.append(value)
		
	while currentIndex>1 and heap[(currentIndex//2)-1] > heap[currentIndex-1] :
		swap(heap,currentIndex-1,(currentIndex//2)-1)
		currentIndex = currentIndex//2

#Generic Function to swap two elements at index 1,2
def swap(arr,index1,index2) :
	temp = arr[index1]
	arr[index1] = arr[index2]
	arr[index2] = temp



