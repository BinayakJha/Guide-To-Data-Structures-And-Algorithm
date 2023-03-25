# @param {List [int]} input
# @return {List [int]}
def build_product_array(input):
  # Your solution here

  results = [None for _ in range(len(input))]
  
  for i in range(len(input)): # iterate through the input
      product = 1 # reset the product
      for j in range(len(input)): # iterate through the input
          if i != j: # don't multiply by the same number
              product*=input[j] # multiply the product by the number
      results[i] = product # add the product to the results list

  return results # return the results

if __name__ == "__main__":
    input = [1, 2, 3, 4, 5]
    print(build_product_array(input))