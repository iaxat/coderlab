# Easy

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target and i<j:
                    result.append(i)
                    result.append(j)
                else:
                    continue

        # return result
        # print(result)

        # method 2
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return([hash_table[nums[i]], i])
            else:
                hash_table[target - nums[i]] = i


        # method 3
        nums_hash = {}
        for i, num in enumerate(nums):
            potentialMatch = target - num
            if potentialMatch in nums_hash:
                print([nums_hash[potentialMatch], i])
            nums_hash[num] = i


        # method 4
        for idx, val in enumerate(nums):
                if target - val in nums[idx + 1:]:
                    return [idx, nums[idx + 1:].index(target - val) + (idx + 1)]

        # method 5
        cache = {}
        for idx, n in enumerate(nums):
            cv = cache.get(target - n)
            if cv != None and cv != idx:
                return [cv, idx]
            cache[n] = idx
        return []


nums = [2,7,11,15]
target = 9
sol = Solution()
sol.twoSum(nums, target)