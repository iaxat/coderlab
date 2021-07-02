# Easy

class Classroom():
    def __init__(self, arr_time) -> None:
        self.arr_time = arr_time

    def timing(self) -> int:
        results = 0
        final_dict = {}
        for i in range(0,len(arr_time)):
            final_dict[i] = arr_time[i]
        print(final_dict)
        

        return results

arr_time = [(30, 75), (0, 50), (60, 150)]
sol = Classroom(arr_time)
print(sol.timing())
