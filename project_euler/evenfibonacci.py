# Even Fibonacci

def even_fib():
    counter = 0
    number = int(input('The number for Fibonacci series'))
    n1,n2 = 1,2
    fib_arr = []


    while counter<=number:
        new = n1 + n2
        n1 = n2
        n2 = new

        counter += 1


    

    
# main function
if __name__ == "__main__":
    even_fib()