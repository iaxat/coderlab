# 
arr = [1,2,3,4,5,6,7,8,9]

# array rotation
d = 2
n = 7
# method 1
def change_rotation(arr, d, n):
    for i in range(d):
        temp_data = arr.pop(0)
        arr.append(temp_data)

    print(arr)


def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n-1] = temp


def leftRotate(arr, d, n):
    for i in range(d):
        leftRotate(arr, n)
        



change_rotation(arr, d, n)
leftRotate(arr, d, n)
