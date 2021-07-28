# Medium

def find():
    data = [2,4,1,3,5]
    result = []
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] > data[j]:
                a = data[i]
                b = data[j]
                result.append(a)
                result.append(b)

    print(result)


def find_method2():
    data = [2,4,1,3,5]
    






find()
