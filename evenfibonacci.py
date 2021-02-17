# Even Fibonacci

def even_fib():
    counter = 1
    number = int(input('The number for Fibonacci series: '))
    n1,n2 = 1,2
    fib_arr = []
    sum = 0


    while counter<=number:
        counter += 1
        fib_arr.append(n1)
        new = n1 + n2
        n1 = n2
        n2 = new
        

    print(fib_arr)

    for i in fib_arr:
        sum += i
    
    print(sum)
    

def reverse_fib():
    sum = 4000000
    new = 0
    add_tot = 0
    n1,n2 = 1,2
    rev_fib_arr = [1,2]

    while new <= sum:
        new = n1 + n2
        n1 = n2
        if n2 % 2 == 0:
            add_tot += n2
        n2 = new
        rev_fib_arr.append(new)


    print(add_tot)


# main function
if __name__ == "__main__":
    even_fib()
    reverse_fib()
