# Medium

import os
import sched
import time

class Solution():
    def job_schedule(self,n,f):
        time.sleep(n)
        return f


n = 0.5
def pr():
    return print('')
f = pr()
sol = Solution()
sol.job_schedule(n,f)
