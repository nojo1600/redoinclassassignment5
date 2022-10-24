#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. 
You left by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists 
based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''
 
def partition(numbers_in_a_list, left, right):
  pivot = numbers_in_a_list[left]
  start = left + 1
  end = right

  while True:
    while start <= end and numbers_in_a_list[end] >= pivot:
      end = end - 1
    while start <= end and numbers_in_a_list[start] <= pivot:
      start = start + 1
    if start <= end:
      numbers_in_a_list[start], numbers_in_a_list[end] = numbers_in_a_list[end], numbers_in_a_list[start]
    else:
      break

  numbers_in_a_list[left], numbers_in_a_list[end] = numbers_in_a_list[end], numbers_in_a_list[left]

  return end

# Please build a function called "quicksort" that uses
# recursion to define the quicksort algorithm for a list of
# any length.
def quicksort(numbers_in_a_list, left, right):
  if left >= right:
      return
  pivot = partition(numbers_in_a_list, left, right)
  quicksort(numbers_in_a_list, left, pivot-1)
  quicksort(numbers_in_a_list, pivot+1, right)
  
  

def main():

# WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM, 
# AND WRITE OUT YOUR FILE

  # read the list from numbers.txt in the following form:
  # in proper list formate [1,2,3,6,4,5,7,8,9,10]
  with open('numbers.txt', 'r') as f:
    numbers_in_a_list = f.read()  # read the entire file into a string
    numbers_in_a_list = numbers_in_a_list[1:-1]  # remove the square brackets
    numbers_in_a_list = numbers_in_a_list.split(', ')  # split the string into a list of strings
    numbers_in_a_list = [int(x) for x in numbers_in_a_list]  # convert the list of strings to a list of ints
    
    # run the list through your quicksort algorithm
    quicksort(numbers_in_a_list, 0, len(numbers_in_a_list)-1)
    
    # write the sorted list to sorted.txt in the following form:
    # in proper list formate [1,2,3,4,5,6,7,8,9,10]
    with open('sorted.txt', 'w') as f:
      f.write(str(numbers_in_a_list))
      
    return 0 #WHAT DOES IT RETURN?


if __name__ == "__main__":
    main()
