from multiprocessing import Pool
import time
from multiprocessing import Process

import os

def work(num):
    print("hello word")
    for i in range(5):
        print("---pid=%s--%d---%d--"%(os.getpid(),i,num))
    time.sleep(2)

# po = Pool(12)
#
# for i in range(10):
#     po.apply_async(work,(i,))
#
# po.close()
#
# po.join()

for i in range(10):
    p = Process(target=work,args=(i,))
    p.start()
    # p.join()