#include <stdio.h>
void BinarySearch(int arr[], int n, int x)
{
    int low = 0;
    int high = n;
    int mid;
    while(low <= high)
    {
        mid = (low + high)/2;
        if(arr[mid] == x)
        {
            printf("Element found at index %d", mid+1);
            return;
        }
        else if(arr[mid] < x)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    printf("Element not found");
}
int main()
{
    int arr[] = {10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60};
    int n = sizeof(arr)/sizeof(arr[0]);
    int x = 30;
    BinarySearch(arr, n, x);
    return 0;

    
}

// BigO of Binary Search is O(log n) because we are searching for the element in the worst case scenario.