import time

import json

print(time.time())

print(time.mktime(time.localtime()))

print(time.localtime())

print(time.localtime(time.time()))


print(time.strftime("%Y%m%d %X"))

print(time.strftime("%y%m%d %x",time.localtime()))

print(time.strftime("%a"))

print(time.strftime("%A"))

print(time.strftime("%B"))

print(time.strftime("%b"))

print(time.strftime("%c"))


t1 = time.time()

t2 = t1 + 10

print(time.ctime(t1))
print(time.ctime(t2))



result = time.strftime("%Y%m%d%H%M%S")

result_a = time.strftime("%Y%m%d%H%M%S")

print(result,"\n",result_a)

# res = ''.join(result)
#
# a = res.replace(":","")
#
# p = json.loads(a)
#
# print(type(p))
#
# print(time.localtime())




w = time.strftime("%Y%m%d%X")

print(w)
