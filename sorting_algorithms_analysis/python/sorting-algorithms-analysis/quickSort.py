#!/usr/bin/python

## QUICK SORT

# Input : Array of Integers - arr
# Output : Returns sorted array


def quickSort(arr,low,high) :
	if(low<high) :
		pivotIndex = _partition(arr,low,high)
		quickSort(arr,low,pivotIndex-1)
		quickSort(arr,pivotIndex+1,high)

	return arr


def _partition(arr,low,high) :
	## Pick first element as pivot element
	pivot = arr[low]
	#print(pivot,"low:",low,"high",high)
	i=low+1
	j=high
	
	while (True) :

		while i<=high and arr[i]<pivot :
			i=i+1
		while j>low and arr[j]>=pivot:
			j=j-1

		if i<j :
			arr[i],arr[j]=arr[j],arr[i] 
		else:
			break

	arr[low],arr[j]=arr[j],arr[low]
	return j

#Generic Function to swap two elements at index 1,2
def swap(arr,index1,index2) :
	temp = arr[index1]
	arr[index1] = arr[index2]
	arr[index2] = temp
