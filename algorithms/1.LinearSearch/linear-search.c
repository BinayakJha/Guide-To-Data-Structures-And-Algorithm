#include <stdio.h>
void search(int arr[], int n, int x){
    int i;
    for(i=0; i<n; i++){
        if(arr[i] == x){
            printf("Element found at index %d", i+1);
            return;
        }
    }
    printf("Element not found");
}
int main(){

    int arr[] = {10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60};
    int n = sizeof(arr)/sizeof(arr[0]);
    int x = 35;
    search(arr, n, x);
    return 0;
}

// BigO will be O(n) because we are searching for the element in the worst case scenario.

// Time Complexity will be O(n) because we are searching for the element in the worst case scenario.