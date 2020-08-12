# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if end >= 1:
        middle = start + (end - 1) // 2
        if target == arr[middle]:
            return print(middle)
        if target > arr[middle]:
            start = middle + 1
            return binary_search(arr, target, start, end)
        if target < arr[middle]:
            end = middle - 1
            return binary_search(arr, target, start, end)
    else:
        return -1

arr = [3, 4, 5, 2, 8, 9]

binary_search(arr, 3, 0, 5 )

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

