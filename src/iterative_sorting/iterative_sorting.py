# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for num in range(len(arr)-1,0,-1):
        for i in range(num):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

    return arr 



# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
     counts = [0] * (maximum -1)
     for item in arr:
         counts[item] +=1
     num_items_before = 0 
     for i, count in enumerate(counts):
         counts[i] = num_items_before
         num_items_before += count
     sorted_arr = [None] * len(arr)
     for item in arr:
         sorted_arr[ counts[item]] = item
         counts[item] -=1

     return sorted_arr



