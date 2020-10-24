def descending_order():
    n = int(input('Enter the number: '))
    lst = list(str(n))
    print('The number is: ', lst)
    lst_new = lst.sort()
    print(lst_new)
    


# The main function
descending_order()