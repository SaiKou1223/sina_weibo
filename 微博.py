import requests
import lxml.etree
import pymongo

def run():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    url = 'https://s.weibo.com/top/summary'#热搜榜
    res = requests.get(url,headers=headers)
    soul = lxml.etree.HTML(res.text)
    items = soul.xpath('//div[@class="m-wrap"]/div[2]//td[@class="td-01 ranktop"]')
    xlist = []
    for item in items:
        num = item.xpath('./text()')[0]
        title = item.xpath('../td[@class="td-02"]/a/text()')[0]
        number = item.xpath('../td[@class="td-02"]/span/text()')[0]
        xlist.append({"序号":num,"关键词":title,"热度":number})
    return xlist

class Mongo():
    def __init__(self):
        self.client = pymongo.MongoClient()
        # 创建数据库
        self.db = self.client.weibo

    def add(self,item):
        return self.db.weibo.insert(item)

if __name__ == '__main__':
    m = Mongo()
    data = run()
    for item in data:
        m.add(item)