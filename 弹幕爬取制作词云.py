import requests
import re
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=1450292993'
#请求头
headers ={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
print(response.text)
content_list = re.findall('<d p=".*?">(.*?)</d>',response.text)
print(content_list)
for content in content_list:
    with open('danmu.txt',mode='a',encoding='utf-8') as f:
        f.write(content)
        f.write('\n')
    print(content)
 #词云
import jieba
import wordcloud
f = open('danmu.txt',encoding='utf-8')
txt= f.read()
print(txt)
string=' '.join(jieba.lcut(txt))
print(string)
wc=wordcloud.WordCloud(
    width=1400,
    height=1400,
    background_color='white',
    font_path='msyh.ttc',
    scale=15,
)
wc.generate(string)
wc.to_file('ciyun.png')