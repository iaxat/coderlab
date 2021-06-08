# Medium

class Solution:
    def myAtoi(self, s: str) -> int:
        results = 0
        stacks = []
        temp_arr = ''
        if s[0].isnumeric() == True:
            for i in range(len(s)):
                    if s[i] == ' ' and len(temp_arr)>=1:
                        stacks.append(temp_arr)
                        temp_arr = ''
                        continue

                    if s[i] == ' ' and len(temp_arr)<1:
                        continue

                    if s[i] == '-':
                        temp_arr += s[i]

                    if s[i].isnumeric():
                        temp_arr += s[i]
    
        stacks.append((temp_arr))
        results = max(stacks)
    
        # if results<-2**31:
        #     return -2**31
        # elif results>2**31-1:
        #     return 2**31-1
        return results

s = "words and 987"
sol = Solution()
sol.myAtoi(s)