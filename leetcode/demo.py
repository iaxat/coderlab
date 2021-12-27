# 
arr1 = [1,2,3]
arr2 = [4,5,6]

arr = [*arr1, *arr2]

print(arr)


arr_total = []
arr_total.append(arr1)
arr_total.append(arr2)

print(arr_total)

allDays = []
allDays.append(arr1[:])
allDays.append(arr2[:])
print(allDays)

print(arr1[:])
