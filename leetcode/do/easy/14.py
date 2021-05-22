class Solution:
    def longestCommonPrefix(self, strs):
        len_str = len(strs)
        temp_arr = []
        temp_dict = {}
        if len_str>0 and len_str<=200:
            for i in range(0,len_str):
                temp_len = len(strs[i])
                temp_dict[temp_len] = strs[i]
                min_key = min(temp_dict.keys())
                max_key = max(temp_dict.keys())
                one = temp_dict[min_key]
                two = temp_dict[max_key]
            for j in range(0,min_key):
                if one[j] == two[j]:
                    temp_arr.append(one[j])
                else:
                    continue
            temp_arr = "".join(temp_arr)
            if len(temp_arr) == 0:
                return ""
            else:
                print(temp_arr)
                return temp_arr


strs = ["flower","flow","flight"]
sol = Solution()
sol.longestCommonPrefix(strs)