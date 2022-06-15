#Binary search is used to guess a number in the middle, then trim it down based on if it's higher or lower

def binary_search(list, item):
    #First, we need low and high to keep track of which part of the list you'll search in
    low = 0
    high = len(list) -1
    #While you haven't narrowed it down to one element
    while low <= high: 
        #check the middle element
        mid = (low + high)
        guess = list[mid]
        #If the guess is the correct number!
        if guess == item: 
            return mid
        #If the guess is too high
        if guess > item: 
            high = mid - 1
        #If the guess is too low
        else: 
           low = mid + 1
        #If the item doesn't exist
    return None

my_list = [1, 3, 5, 7, 9]
print binary_search(my_list, 3)

#run time is log(n) <<Fast!
#if this was simple search, run time would be linear, or 0(n)