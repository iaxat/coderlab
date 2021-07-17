def reverse(input): 
    output = ""
    for index in range(len(input), 0):  
        output += input[index-1]
    print(output)

reverse('Hello')
