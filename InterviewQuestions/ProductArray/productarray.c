#include <stdio.h>

int build_product_array(int input[], int size){
    int i,j;
    int result[size];
    if (size < 2){
        printf("Invalid input");
    }
    else{
        for(i=0; i<size; i++){
            int product = 1;
            for(j=0;j<size;j++){
                if(i != j){
                    product *= input[j];
                }
            }
            result[i] = product;
        }
        for (i=0;i<size;i++){
            printf("%d ", result[i]);
        }
    }
}

int main(){
    int input[] = {-1, 2, 3, 4, 5};
    int size = sizeof(input)/sizeof(int);
    build_product_array(input, size);
    return 0;
}