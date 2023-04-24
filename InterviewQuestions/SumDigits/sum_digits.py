def sum_digits(number):
    # Your solution here
    if number < 10:
        return number
    else:
        return number % 10 + sum_digits(number // 10) # return 1 + sum_digits(234) -> return 4 + sum_digits(23) -> return 3 + sum_digits(2) -> return 2 + sum_digits(0) -> return 0 = 10

print(sum_digits(1234))