import random
import math


counter_count = []
counts = 0

def print_factors(x):
    arr = []
    for i in range(1, x + 1):
       if x % i == 0:
           arr.append(i)
    print("Factors: ", "of", x,"is :", arr)
    return arr


def flunky(i):
    arr_factor = print_factors(i)
    rand_int = []
    sum_total = 0
    for k in range(0,len(arr_factor)):
        random.seed(arr_factor[k])
        rand_int.append(random.randint(0,i))
    print("Random Number", rand_int)
    for j in (0,len(rand_int)-1):
        sum_total +=  rand_int[j]
    if sum_total == i:
        print(i,"is a funky numer @@@@@@########@@@@")
        counter_count.append(i)
        
for i in range(1,50):
    flunky(i)
    # print("Number of flunky number is", counts)
    print("Numbers are", counter_count)