#
# def write_to_file(filename, txt):
#     with open(filename, 'a') as file_object:
#         s = file_object.write(txt)
#
# if __name__ == '__main__':
#     write_to_file('/Users/zhangliang/test/file.text', 'Hello World !!!')


# import time
#
# print('Press ENTER to begin, Press Ctrl + C to stop')
# while True:
#     try:
#         input() # For ENTER. Use raw_input() if you are running python 2.x instead of input()
#         starttime = time.time()
#         print('Started')
#         while True:
#             print('Time Elapsed: ', round(time.time() - starttime, 0), 'secs', end="\r")
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print('Stopped')
#         endtime = time.time()
#         print('Total Time:', round(endtime - starttime, 2),'secs')
#         break


import re
import requests

temp = 'http://wufazhuce.com/one/'
count = 1
for i in range(14, 1580):
    url = temp + str(i)
    page = requests.get(url).text
    reg = re.compile('<img src="(http://.*?)" alt="" />')
    img_url = re.findall(reg, page)
    if img_url != []:
        with open('./{}.jpg'.format(count), 'wb') as file:
            try:
                img_data = requests.get(img_url[0]).content
                file.write(img_data)
                count += 1
            except:
                pass
print('OK!')
