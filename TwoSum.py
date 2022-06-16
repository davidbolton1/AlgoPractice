#Given an unsorted list an a number s, find all the pairs of numbers in that list such that their sum equals s

#Naive Solution
#Loop through the list twice to find two numbers that add up to the provided sum
#Would be O(n^2) since you're searching everything twice(nested array)

def twoSumNaive(num_arr, pair_sum):
  # search first element in the array
  for i in range(len(num_arr) - 1):
    # search other element in the array
    for j in range(i + 1, len(num_arr)):
      # if these two elemets sum to pair_sum, print the pair
      if num_arr[i] + num_arr[j] == pair_sum:
        print("Pair with sum", pair_sum,"is: (", num_arr[i],",",num_arr[j],")")

      

# Driver Code
num_arr = [3, 5, 2, -4, 8, 11]
pair_sum = 7

# Function call inside print
twoSumNaive(num_arr, pair_sum) 