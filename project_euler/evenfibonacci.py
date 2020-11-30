# Even Fibonacci Problems

def fib():
    sum_tot = 0
    number = int(input('Enter Number: '))
    i = 0
    arr_fib = [1,2]
    while i >= number-2:
        for j in arr_fib:
            sum_tot += j
        arr_fib.append(sum_tot)
        i += 1
    print(arr_fib)
    print(sum_tot)


fib()