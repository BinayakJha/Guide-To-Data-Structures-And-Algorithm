#include <stdio.h>

int sum_digits(int n){
    int sum = 0;
    if (n == 0){
        return 0;
    }
    return (n % 10 + sum_digits(n / 10));
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Sum of digits of %d is %d ", n, sum_digits(n));
    return 0;
}