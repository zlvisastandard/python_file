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

list_trade_no = []
swift_refund_id = []

class Com_fanc(object):
    def __init__(self):
        self.url = config.get("section_url","url")

    #程序的主入口
    def Get_send_data(self,section,specy):
        data = self.Main_send(section,specy)
        sign = self.Dd5Sign(section,data)
        data = {"data":data,"sign":sign}
        print(self.Send_Post(data))
        if  "prepay" in specy:
            res_query = self.Swift_query()
            print(res_query)
            if res_query is not None:
                res_refund = self.Swift_refund()
                print(res_refund)
                if res_refund is not  None:
                    print(self.Swift_refundquery())
        else:
            pass

    #判断支付渠道
    def Main_send(self,section,specy):
        if section == "section_pingan":
            list = ["query","jspay"]
            if specy == list[0]:
                data = {"merchant_id":config.get(section,"merchant"),"timestamp":self.TimesTamp(),"biz_type":"wx.query","version":"2.0","biz_content":{"trade_no":"1604155652222654323"},"sign_type":"MD5"}
                data = json.dumps(data)
                return data
            elif specy == list[1]:
                data = {"biz_type":"wx.jspay","merchant_id":config.get(section,"merchant"),"timestamp":self.TimesTamp(),"biz_content":{"time_expire":"20190314123002","total_amount":"0.01","openid":"on8bi1HfC5JAoRGFpEy","trade_no":self.Random_num(),"body":"美食买手订单","sub_appid":"wx709fe1ded6b1b41f","notify_url":"https://wx.51bushou.com/ygg-hqbs/order/pay/yzWxCallback","type":"0"},"sign_type":"MD5"}
                data = json.dumps(data)
                return data
            else:
                print("pingan渠道的功能输入错误。")
        elif section == "section_swift":
            # list = ["prepay","jspay"]
            if specy == "prepay":
                data = {"merchant_id":config.get(section,"merchant"),"timestamp":self.TimesTamp(),"biz_type":"wx.prepay","version":"2.0","biz_content":{"trade_no":self.Random_num(),"attach":"123","total_amount":"0.01","notify_url":"http://allpaytest.visastandards.com/test/ReciveNotiy","sub_appid":"wx7a2dd3787cdbff8f","time_expire":"20091227091010","body":"1234"},"sign_type":"md5"}
                trand = data["biz_content"]
                trand_no = trand["trade_no"]
                list_trade_no.append(trand_no)
                data = json.dumps(data)
                return data
            elif specy == "jspay":
                data = {"merchant_id":config.get(section,"merchant"),"timestamp":self.TimesTamp(),"biz_type":"wx.jspay","biz_content":{"time_expire":"20190314123002","trade_no":self.Random_num(),"total_amount":"0.01","body":"顺网科技网吧消费","notify_url":"http://allpaytest.visastandards.com/test/ReciveNotiy","attach":"123","sub_appid":"wxa5efc0d53aca0adc","openid":"ov6ggw-i2oXqyZr9z-EIayo-3v6E","mch_create_ip":"122.224.184.251","type":"0"},"sign_type":"MD5"}
                data = json.dumps(data)
                return data
            else:
                print("swift渠道的功能输入错误。")
                sys.exit()
        else:
            print("支付渠道输入错误。")
            sys.exit()

    #当swift有查询时，获取trade_no，调取查询
    def Swift_query(self):
        res = input("请输入query_go:")
        if res == "go":
            result = ''.join(list_trade_no)
            data = {"merchant_id":config.get("section_swift","merchant"),"timestamp":self.TimesTamp(),"biz_type":"wx.query","biz_content":{"trade_no":result},"sign_type":"MD5"}
            data = json.dumps(data)
            sign = self.Dd5Sign("section_swift", data)
            data = {"data":data,"sign":sign}
            response = requests.post(url=self.url,data=data).json()
            return json.dumps(response,indent=2,sort_keys=True,ensure_ascii=False)
        else:
            return "输入的继续程序命令错误。。。"

    #当swift的退款
    def Swift_refund(self):
        res = input("请输入refun_go:")
        if res == "go":
            result = ''.join(list_trade_no)
            data = {"merchant_id":config.get("section_swift","merchant"),"timestamp":self.TimesTamp(),"biz_type":"wx.refund","version":"2.0","biz_content":{"trade_no":result,"out_refund_no":self.Random_num()+"1","refund_amount":"0.01","notify_url":"http://allpaytest.visastandards.com/test/ReciveNotiy"},"sign_type":"MD5"}
            data = json.dumps(data)
            sign = self.Dd5Sign("section_swift",data)
            data = {"data":data,"sign":sign}
            response = requests.post(url=self.url,data=data).json()
            try:
                result = response["data"]
                resu = json.loads(result)
                resul = resu["biz_content"]
                result_end = resul["refund_id"]
                swift_refund_id.append(result_end)
            except KeyError as e:
                print(e)
            return json.dumps(response,indent=2,sort_keys=True,ensure_ascii=False)

    #swift的退款查询
    def Swift_refundquery(self):
        res = input("请输入refun_go:")
        if res == "go":
            result_no = ''.join(list_trade_no)
            refund_id = ''.join(swift_refund_id)
            data = {"merchant_id":config.get("section_swift","merchant"),"timestamp":self.TimesTamp(),"biz_type":"wx.refundquery","biz_content":{"trade_no":result_no,"refund_id":refund_id},"sign_type":"MD5"}
            data = json.dumps(data)
            sign = self.Dd5Sign("section_swift",data)
            data = {"data":data,"sign":sign}
            response = requests.post(url=self.url,data=data).json()
            return json.dumps(response, indent=2, sort_keys=True, ensure_ascii=False)

    #生成时间戳
    def TimesTamp(self):
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        return timestamp

    #签名加密
    def Dd5Sign(self,section,data):
        md5_file = hashlib.md5()
        if section == "section_pingan":
            md5_file.update((data + "&" + self.TimesTamp() + config.get(section,"token")).encode("utf-8"))
        elif section == "section_swift":
            md5_file.update((data + "&" + self.TimesTamp() + config.get(section,"token")).encode("utf-8"))
        else:
            pass
        sign = md5_file.hexdigest()
        return sign

    #生成订单随机数
    def Random_num(self):
        time_str = time.strftime("%Y%m%d%H%M%S",time.localtime())
        str = ""
        for i in range(6):
            ch = chr(random.randrange(ord("0"),ord("9")))
            str +=ch
        res_random = time_str + str
        return res_random

    #发送请求
    def Send_Post(self,data):
        response = requests.post(url=self.url,data=data).json()
        res = response["data"]
        res = json.loads(res)
        if res["biz_type"] == "wx.prepay":
            result = res["biz_content"]["qr_code"]
            print(result)
        return json.dumps(response,indent=2,sort_keys=True,ensure_ascii=False)

if __name__ == '__main__':
    res = Com_fanc()
    # res.Get_send_data("section_swift")
    # res.Get_send_data("section_pingan","jspay")
    list = ["prepay"]
    for i in list:
        res.Get_send_data("section_swift",i)