# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_index]:
                cur_index = j
        if cur_index != i:
            arr[cur_index], arr[i] = arr[i], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    sort = False
    while sort != True:
        sort = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                sort = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here

    return arr


print(bubble_sort([4, 7, 5, 9, 10, 0, 3, 6]))
