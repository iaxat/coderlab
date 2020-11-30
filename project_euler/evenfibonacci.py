# Even Fibonacci Problems

def fib():
    sum = 0
    number = int(input('Enter Number: '))
    i = number
    arr_fib = [1,2]
    while i>= number-2:
        sum = sum(arr_fib)
        arr_fib.append(sum)
    print(arr_fib)


fib()