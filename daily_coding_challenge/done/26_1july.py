# Easy
x = [-6, 0, 2, 40]

def sol():
    return [x[i] for i in range(0,len(x)) if i == x[i]][0]
print(sol())
