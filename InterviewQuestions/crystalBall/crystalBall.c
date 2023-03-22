// Given two crystal balls that will break if dropped from the high enough distance,
// determine the exact spot in which it will break in the most optimized way

// We want to jump by square root of N 

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){
    // make a breaks array which is boolean 
    int breaks[1000];
    // make a for loop to fill the array with 0's
    for(int i = 0; i < 1000; i++){
        breaks[i] = 0;
    }
    // fill 1 in random indexes
    for(int i = 0; i < 100; i++){
        int random = rand() % 1000;
        breaks[random] = 1;
    }
    
    
    
    // MAIN ALGORITHM


    int N = sizeof(breaks)/sizeof(breaks[0]);
    int jmpAmt = sqrt(N);
    int i = jmpAmt;
    int j = 0;

    for(i; i < N; i += jmpAmt){
        if(breaks[i] == 1){
            printf("The 1st ball broke at %d \n", i);
            break; //here the first ball breaks now for the second one we will go backwards with same jmpAmt
        }
    }
    // now we will go backwards with the same jmpAmt
    i -= jmpAmt;

    /* This is the second part of the algorithm. We are going backwards from the first ball breaking
    point. */
    for(j; j < jmpAmt; j++){ // jpmAmt value is 10
        if(breaks[i] == 1){
            printf("The 2nd ball broke at %d", i);
            break;
        }
        /* Incrementing the value of i by 1. This is because we are going backwards. */
        i++;
    }
    return 0;


}