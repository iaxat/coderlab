# Medium

class Solution():

    def __init__(self,s) -> None:
        dict_alpha = {}
        self.s = s
        for i in range(1,27):
            dict_alpha[i] = chr(96+i)
        self.dict_alpha = dict_alpha

    def fb_mapping(self):
        arr_s = []
        results = []
        stacks_i = []
        counter = 1
        stacks_i1 = []
        for nums in s:
            arr_s.append(int(nums))
        print(self.dict_alpha)
        if arr_s[0] != 0 and len(arr_s)!=0:
            len_arr_s = len(arr_s)
            for i in range(len_arr_s):
                if arr_s[i] >0 and arr_s[i]<27:
                    # case 1 - check i individual
                    if arr_s[i] in self.dict_alpha.keys() and counter == 1:
                        stacks_i.append(self.dict_alpha[arr_s[i]])
                    else:
                        counter = 0

                    # # case 2 - check i and i+1
                    if i+1<len_arr_s and :
                        stacks_i1.append(self.dict_alpha[arr_s[i]])
                        print(stacks_i1)
                        stacks_i1.append(self.dict_alpha[arr_s[i+1]])
        print(stacks_i)

s = '111'
sol = Solution(s)
sol.fb_mapping()
