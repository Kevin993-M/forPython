import requests
import json
url = 'https://movie.douban.com/j/chart/top_list'
params = {'type':'25','interval_id': '100:90'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'}

response = requests.get(url = url ,params=params,headers= headers)
content = response.json()
for i in content:
    print(json.dumps(i,indent=4,ensure_ascii=False,separators=(',',':')))
    break
with open('豆瓣电影动画排行榜.txt','w',encoding ='utf-8') as fp:
    for i in content:
        title = i['title']
        score = i['score']
        fp.write(title + ' ' + score + '\n')

