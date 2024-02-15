/* A program that checks which sort algotrihm(Bubble, Selection, Merge Sort) is faster than the others */   ␍
␍
#include<stdio.h>␍
#include<stdlib.h>␍
#include<time.h>␍
#include<conio.h>␍
␍
// Function implementation␍
void merge(int *array,int l,int m,int r)        ␍
{␍
    int i,j,k;␍
    int n1=m-l+1;␍
    int n2=r-m;␍
 	␍
 	// Create temp arrays␍
    int L[n1],R[n2];       					  ␍
 ␍
    // Copy data to temp arrays L[] and R[] ␍
    for (i=0;i<n1;i++)␍
        L[i]=array[l+i];␍
    for (j=0;j<n2;j++)␍
        R[j]=array[m+1+j];␍
 ␍
    //Merge the temp arrays back into arr[l..r]␍
    i=0;     	  //Initial index of first subarray␍
    j=0;    	 //Initial index of second subarray␍
    k=l;    	//Initial index of merged subarray␍
    ␍
    while (i<n1 && j<n2)␍
    {␍
        if (L[i]<=R[j])␍
        {␍
            array[k]=L[i];␍
            i++;␍
        }␍
        ␍
        else␍
        {␍
            array[k]=R[j];␍
            j++;␍
        }␍
        ␍
        k++;␍
    }␍
    ␍
    // Copy the remaining elements of L[], if there are any.␍
    while (i<n1)         ␍
    {␍
        array[k]=L[i];␍
        i++;␍
        k++;␍
    }␍
     ␍
    // Copy the remaining elements of R[], if there are any.␍
    while (j<n2)        ␍
    {␍
        array[k]=R[j];␍
        j++;␍
        k++;␍
    }␍
}␍
 ␍
// l is for left index and r is right index of the sub-array of arr to be sorted.␍
   ␍
void merge_sort(int *array, int l, int r)␍
{␍
    if (l<r)␍
    {␍
    	// Same as (l+r)/2, but avoids overflow for large l and h␍
        int m = l+(r-l)/2;					␍
 ␍
        // Sort first and second halves.␍
        merge_sort(array,l,m);␍
        merge_sort(array,m+1,r);␍
        merge(array,l,m,r);␍
    }␍
}␍
␍
void selection_sort(int *array, int n)␍
{␍
	int i,j,swap,min;␍
	␍
	// Loop through all numbers. ␍
	for(i=0;i<n-1;i++)       			   ␍
	{␍
		// Set current element as minimum.␍
		min=i;							    ␍
		␍
		for (j=i+1;j<n;j++)	             ␍
		{␍
			// Check the element to be minimum.␍
			if (array[min]>array[j])␍
			{	␍
            	min=j;␍
        	}␍
   		}␍
␍
   		// Swap the numbers.␍
   		swap=array[min];        		␍
    	array[min]=array[i];␍
    	array[i]=swap;␍
    	␍
	}␍
}␍
␍
void bubble_sort(int *array, int n)␍
{␍
	int i,j, swap;␍
	␍
	// loop through all numbers.␍
	for(i=0;i<n-1;i++)            			  	        	␍
	{␍
		// loop through numbers falling ahead.␍
		for(j=0;j<n-i-1;j++)                    ␍
		{␍
			if(array[j]>array[j+1])	     		␍
			{␍
				// Swap the numbers.␍
				swap=array[j];                 ␍
        		array[j]=array[j+1];␍
        		␍
        		// Bubble up the highest number.␍
        		array[j+1] = swap;			 ␍
			}␍
		}␍
	}␍
}␍
␍
int main()                  					␍
{␍
	int i=0, selected, a;␍
	int *array;␍
	unsigned long int n;␍
	double run_bubble,run_selection,run_merge;␍
	clock_t start_bubble, end_bubble,start_selection,end_selection,start_merge,end_merge;␍
	double total_bubble,total_merge,total_selection;␍
	␍
	// Size of array was taken from user.␍
	printf("Enter the size of array: ");␍
	scanf("%lu",&n);		             	    ␍
␍
	do␍
	{␍
		// Allocate and zero memory for our array with n element.␍
		array=(int*)calloc(n,sizeof(int));	     	␍
		if(array==NULL)␍
		{␍
			n=n-(n/2);␍
		}␍
	} while(array==NULL);␍
		␍
	srand(time(NULL));␍
	␍
		while(i<n)␍
		{␍
			// The program generate approximately up to 327000 with a random function. ␍
	       *(array+i)=(10+rand()%320000)*(rand()%31250);     ␍
			i++;␍
		}␍
	␍
	// Run Bubble Sort Algorithm M times (M>9) with the same number of inputs.␍
    for(a=0;a<10;a++)                    ␍
	{␍
		// Timer for bubble sort algorithm is starting.␍
		start_bubble=clock();                      	␍
		␍
		// Calling bubble sort function.					 ␍
		bubble_sort(array,n);       ␍
		␍
		// Timer for bubble sort algorithm is finishing.␍
		end_bubble=clock();				␍
		␍
		// Total time for bubble sort algortihm.  				   	   ␍
		total_bubble = (double)(end_bubble - start_bubble)/CLOCKS_PER_SEC;		      ␍
		//printf("%d. Time taken by CPU for Bubble Sort: %lf\n",a+1,total_bubble);  ␍
		run_bubble+=total_bubble;  ␍
	}	␍
	printf("Run time of Bubble Sort with %d elements: %lf sec\n", n, run_bubble/10);␍
	␍
	// Run Selection Sort Algorithm M times (M>9) with the same number of inputs.␍
	for(a=0;a<10;a++)                    ␍
	{␍
		// Timer for selection sort algorithm is starting. ␍
		start_selection=clock();	␍
		␍
		// Calling selection sort function.						␍
		selection_sort(array,n);	␍
		␍
		// Timer for selection sort algorithm is finishing.␍
		end_selection=clock();										␍
		␍
		// Total time for selection sort algortihm.				     ␍
		total_selection = (double)(end_selection - start_selection)/CLOCKS_PER_SEC;		␍
		//printf("%d. Time taken by CPU for Selection Sort: %f\n",a+1,total_selection);␍
		run_selection+=total_selection;␍
	}␍
	printf("Run time of Selection Sort with %d elements: %lf sec\n", n, run_selection/10);␍
	␍
	// Run Merge Sort Algorithm M times (M>9) with the same number of inputs. ␍
	for(a=0;a<10;a++)                   ␍
	{␍
		// Timer for merge sort algorithm is starting.␍
		start_merge=clock();␍
		␍
		// Calling merge sort function.												␍
		merge_sort(array,0,n);		␍
		␍
		// Timer for merge sort algorithm is finishing.␍
		end_merge=clock();		␍
		␍
		// Total time for merge sort algortihm.														  ␍
		total_merge = (double)(end_merge - start_merge) / CLOCKS_PER_SEC; 				␍
		//printf("%d. Time taken by CPU for Merge Sort: %f\n",a+1,total_merge);␍
		run_merge+=total_merge;␍
	}␍
	printf("Run time of Merge Sort with %d elements: %lf sec\n",n,run_merge/10);␍
	␍
	getch();␍
	␍
	// Free the memory allocated.␍
	free(array);                 ␍
	return 0;␍
}
