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

    

    
# main function
if __name__ == "__main__":
    even_fib()
