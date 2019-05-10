from quanqudao_test.common import Com_fanc

import json
import requests
import hashlib
import time

res = Com_fanc()

res.Get_send_data(765700141)



#查询
# data = {"merchant_id":"76570014","timestamp":res.TimesTamp(),"biz_type":"wx.query","version":"2.0","biz_content":{"trade_no":"1604155652222654323"},"sign_type":"MD5"}
# timestamp = data["timestamp"]
# data = json.dumps(data)
# sign = res.Dd5Sign(data,timestamp)
# data = {"data":data,"sign":sign}
# response = res.Send_Post(data)
# print(response)


#下单
# data = {"merchant_id":"86570006","timestamp":"20170809115952","biz_type":"wx.prepay","version":"2.0","biz_content":{"trade_no":"prepay_test_1_1","attach":"123","total_amount":"0.01","notify_url":"http://allpaytest.visastandards.com/test/ReciveNotiy","sub_appid":"wx7a2dd3787cdbff8f","time_expire":"20091227091010","body":"1234"},"sign_type":"md5"}
# data = json.dumps(data)
# md5_file = hashlib.md5()
# md5_file.update((data + "&" + "20170809115952" + "9b389216c3c55a7c535510b33b9e6ea5").encode("utf-8"))
# sign = md5_file.hexdigest()
# data = {"data":data,"sign":sign}
# response = requests.post(url=url,data=data).json()
# res = (json.loads(response["data"]))["biz_content"]["qr_code"]
# print(res)

