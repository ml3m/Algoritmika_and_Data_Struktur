#!/usr/bin/python


## MERGE SORT

# Input : Array of Integers - arr
# Output : Returns sorted array


def mergeSort(arr,low,high) :
	if low < high :
		mid = (low+high)//2
		mergeSort(arr,low,mid)
		mergeSort(arr,mid+1,high)
		_merge(arr,low,mid,high)
	
	return arr
	
def _merge(arr,low,mid,high):
	len1 = mid-low + 1
	len2 = high-mid
	list1 = [0] * (len1) 
	list2 = [0] * (len2) 
  
	for i in range(0 ,len1): 
		list1[i] = arr[low + i] 
	for j in range(0 ,len2): 
		list2[j] = arr[mid + 1 + j] 
	
	index = low
	i,j=0,0
	
	while (i<len1 and j<len2):
		if (list1[i] <= list2[j]):
			arr[index]=list1[i]
			i=i+1
		else :
			arr[index]=list2[j]
			j=j+1
		index=index+1
	while i<len1 :
		arr[index] = list1[i]
		index=index+1
		i=i+1
	while j<len2 :
		arr[index] = list2[j]
		index=index+1
		j=j+1
		
	return arr

def _mergeInPlace(arr,low,mid,high):
	
	start1,start2=low,mid+1
	
	while (start1<=mid and start2<=high):
		if (arr[start1]<=arr[start2] ):
			start1=start1+1
		else :
			val = arr[start2]
			arr[start1+1:start2+1]=arr[start1:start2]
			# while index!=start1 :
			# 	arr[index] = arr[index-1]
			# 	index = index-1
			arr[start1] = val
			start1= start1+1
			start2 = start2+1
			mid = mid+1

	return arr