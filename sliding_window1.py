# Sliding Window
# Problem 1
# 
# Fixed Window


class Sliding:
    def __init__(self, window_size, arr) -> None:
        self.window_size = window_size
        self.arr = arr
        self.size = len(arr)



    def make_window_index(self, window_size, arr):
        windows = []
        print(arr)
        i = 0
        while window_size>=1:
            windows.append(i)
            window_size -= 1
            i+=1

        # for i in (0,self.size):
        #     for j in (0, self.size):
        #         if j - i + 1 == self.window_size:
        #             print('\ndone done done\n')
        #             windows.append(i)
        #             windows.append(j)
        #             break
        #         else:
        #             pass
        
        print(windows)
        print(len(windows))

        return windows

    def find_max(self, window_sum_arr):
        print("find max")
        max_max = max(window_sum_arr)
        print("max is ", max_max)
        return max_max

    def find_min(self, window_sum_arr):
        print("find min")
        min_min = min(window_sum_arr)
        print('min is ', min_min)
        return min_min

    def find_sum(self, make_window):
        window_sum = 0
        k = 0
        window_sum_arr = []

        i = make_window[0]
        j = make_window[-1]

        # print('i is ', i)
        # print('j is ', j)

        while j<=self.size:
            new_arr = self.arr[i:j+1]
            print(new_arr)
            window_sum = sum(new_arr)
            print('window sum: ', window_sum)
            i += 1
            j += 1
            window_sum_arr.append(window_sum)
        
        print(window_sum_arr)

        # while j <= self.size - 1:
        #     calculate_win = j - i
        #     now = i
            
        #     while calculate_win > 0:
        #         window_sum = window_sum = self.arr[now] + self.arr[now + calculate_win]
        #         calculate_win -= 1
        #         i += 1
        #         j += 1
        #     print(window_sum)

        # window_sum_arr.append(window_sum)
        # print(window_sum_arr)

        return window_sum_arr


    def slide_karo(self):
        print("slide karo bhai")
        window_index_ = self.make_window_index(self.window_size, self.arr)
        sum_array = self.find_sum(window_index_)
        self.find_max(sum_array)


window_size = 3
arr = [2, 5, 1, 8, 2, 9, 1]

slide = Sliding(window_size, arr)
slide.slide_karo()

# done