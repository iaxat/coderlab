# Medium

class Solution():
    def __init__(self,s,total_list) -> None:
        self.results = []
        self.s = s
        self.total_list = total_list

    def find_dict(self):
        self.trie_data = {}
        



total_list = ['dog', 'deer', 'deal']
s = 'de'
sol = Solution(s,total_list)
print(sol.find_dict())
