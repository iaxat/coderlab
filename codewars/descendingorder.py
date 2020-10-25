def descending_order():
    n = int(input('Enter the number: '))
    lst = list(str(n))
    
    lst_int = []
    lst_new = []

    for i in range(0,len(lst)):
        lst_int.append(int(lst[i]))
    
    length_list = len(lst_int)
    
    # print('lst',lst)
    # print('lst_int',lst_int)
    lst_new = lst_int.sort(reverse=True)
    print(lst_new)
    
    

# The main function
descending_order()

