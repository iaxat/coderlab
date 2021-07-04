# Grokking Algo Book
# Chapter 1

class Solution:
    def binary_search(self, whatsapp_uni, target):
        low = 0
        counter = 0
        high = len(whatsapp_uni) - 1
        while low <= high:
            mid = (low + high) / 2
            mid = int(mid)
            guess = whatsapp_uni[mid]
            if guess == target:
                print(counter)
                return mid
            if guess < target:
                low = mid + 1
            else:
                high = mid - 1
            counter += 1
        print(counter)
        return None


arr_temp = []
for i in range(1, 129):
    arr_temp.append(i)
whatsapp_uni = [1, 2, 3, 4, 5, 6, 7, 8]
target = 128
sol = Solution()
sol.binary_search(arr_temp, target)
