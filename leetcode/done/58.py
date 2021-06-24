# Easy

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # len_result = 0
        # s = s.split(' ')
        # a = True
        # while a==True and s:
        #     temp_s = s[-1]
        #     if temp_s == ' ' or temp_s == '':
        #         s.pop(-1)
        #     else:
        #         len_result = len(temp_s)
        #         a = False
        # return(len_result)

        # len_final = 0
        # counter = len(s)
        # while counter > 0:
        #     counter -= 1
        #     if s[counter] != ' ':
        #         len_final+=1
        #     elif len_final>0:
        #         # return len_final
        #         break
        # return len_final

        if not s or s.isspace():
            return 0
        else:
            return len(s.split()[-1])




s = "hello, world          "
sol = Solution()
print(sol.lengthOfLastWord(s))
