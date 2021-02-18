# Sliding Window
# Fixed Window

class Sliding():
    def __init__(self, window_size, arr) -> None:
        self.window_size = window_size
        self.arr = arr
        self.size = len(arr)

    def make_window(self,window_size,arr):
        self.windows = []
        for i in self.size:
            for j in self.size:
                if j-i+1 == self.window_size:
                    break
        self.windows.append(i)
        self.windows.append(j)

        return self.windows

    def find_max(self,window_sum_arr):
        print('find max')
        max_max = 0

        print('max is ', max_max)
    
    def find_min(self,window_sum_arr):
        print('find min')

    def find_sum(self,make_window):
        window_sum = 0
        window_sum_arr = []
        i = make_window[0]
        j = make_window[1]

        while j<=self.size-1:
            calculate_win = j-i+1
            now = i

            window_sum = self.arr[now] + self.arr[now+]

            i+=1
            j+=1
            
        window_sum_arr.append(window_sum)

        return window_sum_arr

    def slide_karo(self):
        print('slide karo bhai')
        make_window = self.make_window(self.window_size,self.arr)
        sum_array = self.find_sum(make_window)
        self.find_max(sum_array)



window_size = 3
arr = [2,5,1,8,2,9,1]

slide = Sliding(window_size,arr)
slide.slide_karo()