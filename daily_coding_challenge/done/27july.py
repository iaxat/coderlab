# Easy

def search_profit():
    data = [9,11,8,5,7,10]
    result = []
    for i in range(0,len(data)):
        for j in range(i,len(data)):
            result.append(data[j]-data[i])
    print(max(result))



search_profit()

