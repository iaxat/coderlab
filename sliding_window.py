# Sliding Window
# Fixed Window


class Sliding:
    def __init__(self, window_size, arr) -> None:
        self.window_size = window_size
        self.arr = arr
        self.size = len(arr)

    def make_window(self, window_size, arr):
        windows = []
        i = 0
        for j in (0, self.size):
            if j - i + 1 == self.window_size:
                break
        windows.append(0)
        windows.append(j)
        print(windows)
        return windows

    def find_max(self, window_sum_arr):
        print("find max")
        max_max = 0

        print("max is ", max_max)

    def find_min(self, window_sum_arr):
        print("find min")

    def find_sum(self, make_window):
        window_sum = 0
        window_sum_arr = []
        i = make_window[0]
        j = make_window[1]

        while j <= self.size - 1:
            calculate_win = j - i
            now = i
            window_sum = self.arr[now]
            while calculate_win > 0:
                window_sum = self.arr[now + calculate_win]
                calculate_win -= 1
                i += 1
                j += 1
            print(window_sum)

        window_sum_arr.append(window_sum)
        print(window_sum_arr)

        return window_sum_arr

    def slide_karo(self):
        print("slide karo bhai")
        make_window = self.make_window(self.window_size, self.arr)
        sum_array = self.find_sum(make_window)
        self.find_max(sum_array)


window_size = 3
arr = [2, 5, 1, 8, 2, 9, 1]

slide = Sliding(window_size, arr)
slide.slide_karo()
