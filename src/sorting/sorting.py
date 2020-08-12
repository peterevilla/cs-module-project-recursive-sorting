# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    
    i = 0
    j = 0

    arr = []

    while (i < len(arrA)) and (j < len(arrB)):
        if(arrA[i] < arrB[j]):
            arr.append(arrA[i])
            i += 1
        else:
            arr.append(arrB[j])
            j += 1

    if i == len(arrA):
        arr.extend(arrB[j:])
    else:
        arr.extend(arrA[i:])
    return arr

# TO-DO: implement the Merge Sort function below recursiveßly
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    arrA = merge_sort(arr[:mid])
    arrB = merge_sort(arr[mid:])

    arr = merge(arrA, arrB)

    
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

