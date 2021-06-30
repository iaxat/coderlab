# grokking algorithm
arr_ = [10,5,2,99,0,23,54,11,32,43,56,87,78,33,65,70,50,19,3,4,5]
new_arr = []
smallest = arr_[0]
# selection sort
def selection_sort(arr_,new_arr,smallest):
    # starting selection sort
    for i in range(0,len(arr_)):
        for j in range(i,len(arr_)):
            if arr_[j] < smallest:
                smallest = arr_[j]
        print(smallest)
        new_arr.append(smallest)                

    return new_arr

# print(selection_sort(arr_,new_arr,smallest))
# -------------------------------
# def selection_sort_multiple_function():






# -----------------------------
def selectionsort_another(arr_,new_arr):
    for i in arr_:
        new_arr.append(min(arr_))
        arr_.pop(arr_.index(min(arr_)))
    return new_arr

print(selectionsort_another(arr_,new_arr))


# recursion
# selection sort
# quick sort










# quick sort







