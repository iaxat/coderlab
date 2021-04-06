class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        counter = 0
        for i in items:
            if ruleKey == 'color':
                item_key = 1
            if ruleKey == 'type':
                item_key = 0
            if ruleKey == 'name':
                item_key = 2
            if ruleValue == i[item_key]:
                counter += 1
        print(counter)


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
sol = Solution()
sol.countMatches(items, ruleKey, ruleValue)