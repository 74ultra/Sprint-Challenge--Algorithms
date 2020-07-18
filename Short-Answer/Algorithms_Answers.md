#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) --> The while loop will run the number of times as the value 'n'


b) O(n^2) --> Each loop will run O(n) times resulting in O(n) * O(n)


c) O(n) --> The number of times the function is called is the same as the value of 'n'

## Exercise II

A method to reduce the total number of drops necessary and eggs broken: Binary Search

    1. Establish two inital values (low and high):
        'low' set to the numeric value of the first floor
        'high' set to the numeric value of the top floor
    2. Establish a 'last_broken' value:
        'last_broken' initially set to zero
    3. Set up a while loop:
        loop will continue while the value of 'low' is less than or equal to 'high'
    4. Establish a 'mid_point' value:
        'mid_point' set equal to the average of 'low' and 'high'
    5. Drop an egg from the floor with the value of 'mid-point'
        if the egg does not break:
            the 'low' value is set to ('mid_point' + 1)
        if the egg does break:
            'last_broken' is updated with the value of 'mid_point'
            the 'high' value is set to ('mid_point' - 1)
    6. When the loop ends, 'last_broken' is returned add will be equal to the value of floor 'f'

O(log n) --> On each iteration of the loop the number of elements to search/inspect is reduced by half


Proposed algorithm:

def egg_drop(arr, target):
  low = 0
  high = len(arr)-1
  last_broken = 0
  counter = 0
  while high >= low:
    counter += 1
    print(counter)
    mid = (low+high)//2
    # break
    if arr[mid] >= target:
      last_broken = arr[mid]
      high = mid - 1
    # no break
    if arr[mid] < target:
      low = mid + 1
  return last_broken