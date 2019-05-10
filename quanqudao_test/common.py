import time
import hashlib
import requests
import configparser
import os
import sys
import json
import random

prodir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(prodir,"conf.ini")
config = configparser.ConfigParser()
config.read(config_path)

class Com_fanc(object):
    def __init__(self):
        self.url = config.get("section_url","url")

    def Get_send_data(self,merchant):
        data = self.Main_send(merchant)

        sign = self.Dd5Sign(data,merchant)
        data = {"data":data,"sign":sign}
        print(self.Send_Post(data))

    def Main_send(self,merchant):
        merchant = int(merchant)
        if merchant == 76570014:
            data = {"merchant_id":config.get("section_pingan","merchant"),"timestamp":self.TimesTamp(),"biz_type":"wx.query","version":"2.0","biz_content":{"trade_no":"1604155652222654323"},"sign_type":"MD5"}
            data = json.dumps(data)
            return data

        elif merchant == 86570006:
            data = {"merchant_id":config.get("section_swift","merchant"),"timestamp":self.TimesTamp(),"biz_type":"wx.prepay","version":"2.0","biz_content":{"trade_no":self.Random_num(),"attach":"123","total_amount":"0.01","notify_url":"http://allpaytest.visastandards.com/test/ReciveNotiy","sub_appid":"wx7a2dd3787cdbff8f","time_expire":"20091227091010","body":"1234"},"sign_type":"md5"}
            data = json.dumps(data)
            return data

        else:
            print("输入错误。")
            sys.exit()

    def TimesTamp(self):
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        return timestamp

    def Dd5Sign(self,data,merchant):
        md5_file = hashlib.md5()
        md5_file.update((data + "&" + self.TimesTamp() + config.get("section_pingan","token")).encode("utf-8"))
        sign = md5_file.hexdigest()
        return sign

    def Random_num(self):
        time_str = time.strftime("%Y%m%d%H%M%S",time.localtime())
        str = ""
        for i in range(6):
            ch = chr(random.randrange(ord("0"),ord("9")))
            str +=ch
        res_random = time_str + str
        return res_random

    def Send_Post(self,data):
        response = requests.post(url=self.url,data=data).json()
        return json.dumps(response,indent=2,sort_keys=True,ensure_ascii=False)

if __name__ == '__main__':
    res = Com_fanc()
    # res.Get_send_data(76570014)
    # res.Get_send_data(86570006)
    print(res.Random_num())