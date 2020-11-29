# Project Euler 
# Multiples of 3 and 5

def multiples():
    mul_array = []
    sum = 0
    n = int(input("Enter the Number"))
    for i in range (0,n):
        if i%3 == 0 or i%5 == 0:
            mul_array.append(i)
            sum += i
        else:
            continue
    
    print('Sum is the',sum)


if __name__ == "__main__":
    multiples()