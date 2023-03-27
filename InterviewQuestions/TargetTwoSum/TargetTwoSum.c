#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int get_target_indexes(int *arr, int target, int size)
{
    int i, j;
    int count = 0;

    /* This is a nested for loop that is iterating through the array and checking if the sum of any two
    elements in the array is equal to the target. If it is, then it increments the count by 2. */
    for (i = 0; i < size; i++){
        for (j = i + 1; j < size; j++){
            if (arr[i] + arr[j] == target){
                count += 2;
            }
        }
    }

    int *indexes = (int *)malloc(sizeof(int) * count);

    int k = 0;

   
    for (i = 0; i < size; i++){
        for (j = i + 1; j < size; j++){
            if (arr[i] + arr[j] == target){
                indexes[k++] = i; 
                indexes[k++] = j;
            }
        }
    }
    // Making the output work

    printf("[");
    for (i = 0; i < count - 1; i += 2){

        printf("[%d, %d], ", indexes[i], indexes[i + 1]);

    }
    printf("[%d, %d]]", indexes[count - 2], indexes[count - 1]);
}

int main(){
    int arr[] = {3, 4, 1, 8, 9, 2, 10};
    int target = 11;
    int size = sizeof(arr) / sizeof(arr[0]);
    get_target_indexes(arr, target, size);
}