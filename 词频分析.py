import docx 
document = docx.Document( r"C:\Users\rgdfy\OneDrive - 南京大学\Documents\新建 Microsoft Word 文档.docx" )
#用相对目录好像总是CE所以写的是绝对目录
content = " ".join( [para.text for para in document.paragraphs])
len ( content)
#验证是否读取
import jieba
seg_list =jieba.cut (content,cut_all=False)
print(type(seg_list ))
# 过滤标点符号、无意义的单个字
seg_list = [
    word
    for word in seg_list
    if len (word) > 1
]
seg_list[:30]
from collections import Counter
counter = Counter(seg_list)
for key ,count in list (counter.items()) [:10 ]:
    print ( key ,count)
import pandas as pd
df = pd.DataFrame(list(counter.items( )), columns=[ "word","count" ] )
df.head()
df.sort_values( by="count", ascending=False,inplace=True)
df.head( )
df.to_csv('统计输出.csv',index=False)