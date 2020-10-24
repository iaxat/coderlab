def descending_order():
    n = int(input('Enter the number: '))
    print('The number is: ', n)
    lst = []
    for i in range(0,n):
        ele = int(input())
        lst.append(ele)
    print(lst)
    
# The main function

descending_order()