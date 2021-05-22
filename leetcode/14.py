class Solution:
    def longestCommonPrefix(self, strs):
        len_str = len(strs)
        temp_dict = {}
        if len_str>0 and len_str<=200:
            for i in range(0,len_str):
                temp_len = len(strs[i])
                temp_dict[temp_len] = strs[i]
                min_key = min(temp_dict)
            # for j in min_key:
                


        print(temp_dict)


strs = ["flower","flow","flight"]
sol = Solution()
sol.longestCommonPrefix(strs)