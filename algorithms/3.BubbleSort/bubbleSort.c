#include <stdio.h>
#include <stdlib.h>

void BubbleSort(int arr[], int n ){
    int i,j,temp;
    for(i=0;i<n-1;i++){  // n-1 because the last element will be sorted after the first iteration. here value of n is 10 
        for(j=0;j<n-i-1;j++){ // n-i-1 to find the second element to be compared with the element that came in the first element. Here the value of n is 
            if(arr[j]>arr[j+1]){
                // here at first arr[0] = 10 and arr[1] = 2. so 10>2 is true and the value of temp is 10.
                temp = arr[j];
                arr[j]= arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    // Printing the sorted array
    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}

int main(){
    int arr[] = {10,2,6,3,2,5,4,7,9,8};
    int n = sizeof(arr)/sizeof(arr[0]);
    BubbleSort(arr,n);
}