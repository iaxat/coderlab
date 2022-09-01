nested_dict = {
    'a' : [0,0,0],
    'b' : {
        'c' : [0,0,0],
        'd' : {
            'e' : [0,1,1],
            'f' : {
                'l' : [0,2,1],
                'j' : {
                    'h' : [0,2,2]
                }
            }
        }
    }
}

def rec(nested_dict, i, new_dict, data):
    data += i
    print(i)
    print(nested_dict)
    if isinstance(nested_dict[i], list):
        new_dict[data] = nested_dict[i]

    else:
        for j in nested_dict[i].keys():
            rec(nested_dict[i], j, new_dict, data)


if __name__ == '__main__':
    new_dict = {}
    for i in nested_dict.keys():
        data = ''
        rec(nested_dict, i, new_dict, data)
