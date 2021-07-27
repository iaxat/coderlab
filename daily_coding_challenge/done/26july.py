# hard

class Solution():
    def __init__(self, data) -> None:
        self.data = data

    def find_sub(self):
        result = []
        len_data = len(self.data)
        for i in range(len_data):
            for j in range(i,len_data+1):
                temp_arr = self.data[i:j]
                if len(temp_arr) > 1:
                    if temp_arr == temp_arr[::-1] and len(result)<len(temp_arr):
                        result = temp_arr
        return result


data = 'aabcdcb'
sol = Solution(data)
print(sol.find_sub())
