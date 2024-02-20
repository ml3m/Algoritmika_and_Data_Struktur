#!/usr/bin/python

import random
import time
import resource
import sys
import matplotlib.pyplot as plt
import numpy as np
from insertionSort import insertionSort
from mergeSort import mergeSort
from heapSort import heapSort
from quickSort import quickSort
from modifiedQuickSort import modifiedQuickSort



class Compare:
	def __init__(self) :
		# Dictionary being used when testing sort for 1 algorithm
		self.FuncName = {
			'insert': insertionSort,
			'merge': mergeSort,
			'heap': heapSort,
			'quick': quickSort,
			'modifiedQuick': modifiedQuickSort
		}


		# For type DataSet
		self.data_type = {
			1: "",
			2: "_sorted",
			3: "_reverse"
		}

		self.inputSize = 1000
		self.dataSet = 1

		# Taking average given no of dataset , Default value : 3
		# For generating avg on more number of dataset , execute dataset_generator.py
		# before compare.py
		self.Num_Of_Case = 3
		

	# Function for calculating average time taken by each sorting algorithm
	def calculateAvg(self,func, execTime):
		sortingName = self.FuncName[func]
		timeElapsed = 0
		for i in range(1, self.Num_Of_Case+1):
			fileName = "DataSet/dataSet" + str(i) +self.data_type.get(self.dataSet) + ".txt"
			inputFile = open(fileName, "r")
			arr = np.loadtxt(inputFile, dtype=int, max_rows=self.inputSize)
			inputFile.close()
			startTime = time.time()
			if arr.size==1 :
				list1 = []
				list1.append(arr[()])
				arr=list1
			sortingName(arr, 0, len(arr)-1)
			timeElapsed = timeElapsed + time.time()-startTime
			# if(any(arr[i] > arr[i+1] for i in range(len(arr)-1))):
			# 	print("Test Case Failed ****")
		timeElapsed = (timeElapsed/self.Num_Of_Case)*1000
		execTime.append(timeElapsed)
		print('Time elapsed in Execution of '+func +' : '+str(timeElapsed)+' milli seconds')


	def main(self):
		print("Average of exection time taken for :", self.Num_Of_Case, " DataSet")
		print("Select Sorting Algorithm to test :")
		print("1. Insertion Sort")
		print("2. Merge Sort")
		print("3. Heap Sort")
		print("4. In-Place Quick Sort")
		print("5. Modified Quick Sort")
		print("6. All Sorting Algorithms")
	
		func = []
		while len(func) == 0:
			algorithm = int(input("Enter the Algorithm number :"))
			if algorithm == 6:
				func = [item for item in range(1, 7)]
				break
			if (algorithm >= 1 or algorithm <= 5):
				func.append(algorithm)
				break
			print("Please Enter valid Input")

		print("\nSelect Type of Data Set for sorting :")
		print("1. Random/Unsorted Input")
		print("2. Sorted Input")
		print("3. Reversely Sorted Input")

		self.dataSet = int(input("how do you want the inputs to be:"))
		
		# Input Size
		size = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000]
		#size = [1,2,3,4,5,6,7,8,9,10]

		# List to store execution time of each sorting algorithm
		insert = []
		merge = []
		heap = []
		quick = []
		modifiedQuick = []

		for num in size:
			self.inputSize = num
			print("\n For input size of :"+str(num))
			for algo in func:
				if algo == 1:
					self.calculateAvg('insert', insert)
				elif algo == 2:
					self.calculateAvg('merge', merge)
				elif algo == 3:
					self.calculateAvg('heap', heap)
				elif algo == 4:
					self.calculateAvg('quick', quick)
				elif algo == 5:
					self.calculateAvg('modifiedQuick', modifiedQuick)

		# For Ploting Graph
		if algorithm ==1 :
			plt.plot(size, insert, label = "Insertion Sort")
		elif algorithm ==2 :
			plt.plot(size, merge, label = "Merge Sort")
		elif algorithm==3 :
			plt.plot(size, heap, label = "Heap Sort")
		elif algorithm==4:
			plt.plot(size, quick, label = "Quick Sort")
		elif algorithm==5:
			plt.plot(size, modifiedQuick, label = "Modified Quick Sort")
		elif algorithm==6:
			plt.plot(size, insert, label = "Insertion Sort")
			plt.plot(size, merge, label = "Merge Sort")
			plt.plot(size, heap, label = "Heap Sort")
			plt.plot(size, quick, label = "Quick Sort")
			plt.plot(size, modifiedQuick, label = "Modified Quick Sort")
		
		plt.xlabel('Input Size')
		plt.ylabel('Execution time in milliseconds')
		plt.title('Graph comparing Sorting Algorithms !')
		plt.legend()
		plt.savefig('graph'+self.data_type.get(self.dataSet)+'.png')
		print("Check graph"+self.data_type.get(self.dataSet)+'.png'+ " for saved graph")
		print("Displaying plotted graph")
		plt.show()

resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**6)
compare = Compare()
compare.main()
