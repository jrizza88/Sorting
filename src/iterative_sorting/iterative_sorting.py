# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # remember, this algorithm is O(n^2) n squared..
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # print(f'smallest {smallest_index}')
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        temp_index = arr[cur_index]
        # print(f'temp index{arr[cur_index]}')
        arr[cur_index] = arr[smallest_index]
        # print(f'second temp index{arr[smallest_index]}')
        arr[smallest_index] = temp_index

    return arr
            
                



        # TO-DO: swap



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr) - 1):
        print(f'i {i}')
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                print(f'j {j}')
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                print(f'j X 2:  {j}')
        #for each element in list look at element to its right
        #if out of order to each other, (val on left > val on right)
        # swap them! 
        #  arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        # once highest value element is at the end, it remains there.
    return arr

def bubble_sort2( arr ):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(arr) - 1):
            largest_index = i
            if arr[largest_index] > arr[largest_index + 1]:
                temp = arr[largest_index]
                arr[largest_index] = arr[largest_index + 1]
                arr[largest_index + 1] = temp
                swap = True
 
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr