#include <stdio.h>
#include <stdlib.h>

int max_profit(int *prices, int pricesSize){
    if (pricesSize < 2){
        return 0;
    }
    else{
        int min_price = prices[0];
        int max_profit = prices[1] - prices[0];
        for (int i = 1; i < pricesSize; i++){
            int current_price = prices[i];
            int potential_profit = current_price - min_price;
            max_profit = (potential_profit > max_profit) ? potential_profit : max_profit;
            min_price = (current_price < min_price) ? current_price : min_price;
        }
        return max_profit;
    }


}

int main(){
    int prices[] = {10, 7, 5, 8, 11, 9};
    int pricesSize = sizeof(prices)/sizeof(prices[0]);
    int profit = max_profit(prices, pricesSize);
    return printf("Max Profit: %d", profit);
}