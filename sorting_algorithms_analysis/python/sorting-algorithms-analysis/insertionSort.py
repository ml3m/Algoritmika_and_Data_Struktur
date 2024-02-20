#!/usr/bin/python

## INSERTION SORT

# Input : Array of Integers - arr
# Output : Returns sorted array

def insertionSort(arr,low,high) :
	for i in range(1,high+1):
		keyValue = arr[i]		
		j=i-1
		while j>=0 and keyValue<=arr[j]:
			arr[j+1]=arr[j]
			j=j-1
		arr[j+1]=keyValue
	#print(arr)
	return arr


