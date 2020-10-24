def descending_order(n):
    print('The number is: ', n)
    lst = []
    for i in range(0,n):
        ele = int(input())
        lst.append(ele)
    print(lst)
    
# The main function
n = int(input('Enter the number: '))
descending_order(n)