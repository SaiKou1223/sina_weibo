import requests
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
for x in range(1,11):
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=2304135842225215_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page={}'.format(x)
    print(url)
    res = requests.get(url,headers=headers).json()
    time.sleep(2)
    weibo_list = res["data"]["cards"]
    for i in range(len(weibo_list)):
        try:
            text = weibo_list[i]["mblog"]["raw_text"]
            print(text)
        except:
            print("这条不是微博")