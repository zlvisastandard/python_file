from multiprocessing import Pool

import time

import os

def work(num):
    print("hello word")
    for i in range(5):
        print("---pid=%s--%d---%d--"%(os.getpid(),i,num))
    time.sleep(2)

po = Pool(3)

for i in range(10):
    po.apply_async(work,(i,))

po.close()

po.join()

print("版本号")