# Even Fibonacci

def even_fib():
    counter = 0
    number = int(input('The number for Fibonacci series: '))
    n1,n2 = 1,2
    fib_arr = []


    while counter<=number:
        fib_arr.append(n1)
        fib_arr.append(n2)
        new = n1 + n2
        n1 = n2
        n2 = new

        counter += 1

    print(fib_arr)

    

    
# main function
if __name__ == "__main__":
    even_fib()