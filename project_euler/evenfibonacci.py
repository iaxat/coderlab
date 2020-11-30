# Even Fibonacci Problems

def fib():
    sum_tot = 0
    number = int(input('Enter Number: '))
    i = 0
   
    arr_fib = [1,2]
    
    while i != number-2:
        l = 2
        while l != 0:
            l = l-1
            sum_tot = arr_fib[-1] + arr_fib[-2]
            arr_fib.append(sum_tot)
        i += 1
    
    print(arr_fib)
    print(len(arr_fib))


fib()