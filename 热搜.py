import requests
import lxml.etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
url = 'https://s.weibo.com/top/summary'#热搜榜
url_yw = 'https://s.weibo.com/top/summary?cate=socialevent'#要闻榜
res = requests.get(url,headers=headers)
soul = lxml.etree.HTML(res.text)
items = soul.xpath('//div[@class="m-wrap"]/div[2]//td[@class="td-01 ranktop"]')
for item in items:
    num = item.xpath('./text()')[0]
    title = item.xpath('../td[@class="td-02"]/a/text()')[0]
    number = item.xpath('../td[@class="td-02"]/span/text()')[0]
    print("序号:",num,"关键词:",title,"热度:",number)
#热搜
#---------------------------------------------------------------------------------------------------------
res_yw = requests.get(url_yw,headers=headers)
soul = lxml.etree.HTML(res_yw.text)
items_yw = soul.xpath('//div[@class="m-wrap"]/div[2]//a')
for item_yw in items_yw:
    title_yw = item_yw.xpath('./text()')[0]
    print(title_yw)
#要闻
#---------------------------------------------------------------------------------------------------------