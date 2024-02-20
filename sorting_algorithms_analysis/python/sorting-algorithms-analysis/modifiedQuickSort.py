#!/usr/bin/python

from insertionSort import insertionSort
## MODIFIED QUICK SORT

# Input : Array of Integers - arr
# Output : Returns sorted array

def modifiedQuickSort(arr,low,high) :
	if(low+10<=high) :
		if(low<high) :
			pivotIndex = _partitionModified(arr,low,high)
			modifiedQuickSort(arr,low,pivotIndex-1)
			modifiedQuickSort(arr,pivotIndex+1,high)
	else :
		arr[low:high+1] = insertionSort(arr[low:high+1],0,high-low)

	return arr
	

def _partitionModified(arr,low,high) :
	## Pick media of first ,middle,last element as pivot element
	pivotIndex=(low+high)//2
	arr[low],arr[pivotIndex],arr[high] = findMedian(arr[low],arr[(low+high)//2],arr[high])
	pivot = arr[pivotIndex]
	arr[pivotIndex],arr[high-1]=arr[high-1],arr[pivotIndex]
		
	i=low+1
	j=high-2
	
	while (True) :

		while i<=high and arr[i]<pivot :
			i=i+1
		while j>low and arr[j]>=pivot:
			j=j-1
		if i<j :
			arr[i],arr[j]=arr[j],arr[i] 
		else :
			break
	arr[i],arr[high-1]=arr[high-1],arr[i] 
	return i

def findMedian(low,mid,high) :
	if (low >mid) :
		mid,low=low,mid
	if (low > high) :
		high,low=low,high
	if (mid > high) :
		mid,high=high,mid
	return low,mid,high
