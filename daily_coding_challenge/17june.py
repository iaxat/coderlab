# Medium

from typing import Dict


class Solution():

    def __init__(self) -> None:
        dict_alpha = {}
        for i in range(1,27):
            dict_alpha[i] = chr(97+i)
        
        print(dict_alpha)
        self.dict_alpha = dict_alpha

    # def fb_mapping(self):


sol = Solution()
print(sol.dict_alpha)
