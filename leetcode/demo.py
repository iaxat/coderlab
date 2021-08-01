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

def rotation_method2(arr, d, n):
    for i in range(d):
        



change_rotation(arr, d, n)
rotation_method2(arr, d, n)
