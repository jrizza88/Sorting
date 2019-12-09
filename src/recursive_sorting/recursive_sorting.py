# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    print(elements)
    print(f"merge({arrA}, {arrB})")
    merged_arr = [0] * elements
    # TO-DO

    for i in range(0, len(merged_arr)):
        # write if statement if there is just one element
        # put things to the left of the pivot
        # put things to the right of the pivot
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            arrB.remove(arrB[0])
            print(f' if len(arrA) == 0: merged_arr[i] = arrB ===== {merged_arr}')
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            arrA.remove(arrA[0])
            print(f' if len(arrB) == 0: merged_arr[i] = arrA ===== {merged_arr}')
        elif arrA[0] <= arrB[0]:
            merged_arr[i] = arrA[0]
            arrA.remove(arrA[0])
            print(f'len(arrA[0]) <= len(arrB[0]): {merged_arr}')
        elif arrA[0] > arrB[0]:
            merged_arr[i] = arrB[0]
            arrB.remove(arrB[0])
            print(f'len(arrB[0]) <= len(arrA[0]): {merged_arr}')

    merged_arr.sort()
    print(f'did merg_arr.sort() work? : {merged_arr}')
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    pivot = len(arr) // 2
    left = None
    right = None

    print(f'Mid value: {pivot}')
    left = merge_sort(arr[:pivot])
    right = merge_sort(arr[pivot:])

    return merge(left, right)
    # return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
