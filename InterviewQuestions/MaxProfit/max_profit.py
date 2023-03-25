def get_max_profit(total_versions):
    size = len(total_versions)
    
    if size < 2:
        return 0
    else:
        min_num = min(total_versions)
        profit = []
        i = 0
        for i in range(size):
            for j in range(1, size):
                if i < j and min(total_versions) == total_versions[i] :
                    p =  total_versions[j] -  min(total_versions) 
                    profit.append(p)
        if len(profit) == 0:
            return 0
        else:     
            print("To get the maximum profit, you should buy at: " + str(min_num) + " and sell at: " + str(max(profit) + min_num))
            return max(profit)


prices = [10, 7, 5, 8, 11, 9]

print(get_max_profit(prices))

