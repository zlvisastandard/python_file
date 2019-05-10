import configparser

import os

#当前的文件路径
prodir = os.path.split(os.path.realpath(__file__))[0]

#拼接配置文件的路径
config_path = os.path.join(prodir,"conf.ini")


#获取配置内的内容
conf = configparser.ConfigParser()
conf.read(config_path)

#获取url的value的值
print(conf.get("section1","url"))

#返回所有的section
print(conf.sections())

#返回section1中所有的key的值
print(conf.options("section1"))

#以元组的形式返回key与value的值
print(conf.items("section1"))


# #向section1中写入配置信息
# conf.set("section1","name","three")
# res = conf.get("section1","name")
# print(res)
# #实际写入配置文件中
# conf.write(open(config_path,"w+"))


# #向配置文件内写入section
# conf.add_section("scetion3")
# result = conf.sections()
# conf.write(open(config_path,"w+"))
# print(result)

for i in conf.options("section1"):
    print(i)