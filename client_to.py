import requests
import json

def get_result():
    url = "http://127.0.0.1:50001/nlp/words"
    data = {"word1":"番茄","word2":"西红柿"}
    data_json = json.dumps(data) # 将字典转为Json格式的字符串，因为request库再发送请求时候，需要字符串格式的数据
    response = requests.post(url,data=data_json) # 发送POST请求
    print(response.json()) # 打印响应内容，

if __name__=="__main__":
    get_result()