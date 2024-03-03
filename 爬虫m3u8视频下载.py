import requests
import re
import json
from pprint import pprint
from tqdm import tqdm

def GetResponse(url):
    # 模拟浏览器
    headers = {
        # User-Agent 用户代理, 表示浏览器基本身份信息
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    return response


def GetVideo(ac):
    """获取M3U8 / 标题"""
    link = f'https://www.acfun.cn/v/ac{ac}'
    response = GetResponse(url=link)
    html = response.text
    """解析数据, 提取我们需要的数据内容: m3u8链接 / 视频标题 """
    title = re.findall('<h1 class="title"><span>(.*?)</span></h1>', html)[0]
    videoInfo = re.findall('window.pageInfo = window.videoInfo = (.*?);', html)[0]
    m3u8_url = json.loads(json.loads(videoInfo)['currentVideoInfo']['ksPlayJson'])['adaptationSet'][0]['representation'][0]['url']
    return title, m3u8_url


def Save(title, m3u8):
    """保存数据"""
    M3u8Data = GetResponse(url=m3u8).text
    # 解析数据, 提取ts链接
    ts_list = re.findall(',\n(.*?)\n#', M3u8Data)
    ts_name = '/'.join(m3u8.split('/')[:6])
    for ts in tqdm(ts_list):
        # https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/c3471e9635d5b851-b7141b506c6f33d5ec893077a0e6ea00-hls_720p_hevc_1.00008.ts?pkey=ABCCz5Cu3ahkPwMQJ7vUcwnTveE7QKf-IrU9C3Vu3xcZGCZagklTMAECcTcSvTumDB3nGkGiwLPszJOELJQ2OV3xM-3aemxTD_qIHpCbTuUD6VKoBgl--iwm-mPatYt7AvNP704PprZHpuu1G_gL3lUfrnYO8UMLfak1Txms9elnll-Ft14_sUK7ljCxiQGgeTHVx5NJ2dZlXilcGiTj_aq_abuAwCD2zCYvEJM18OPgfNAH2S8jEElcbSgr5GCcNog&safety_id=AAI4Rw8M7_NLcdv8CDQKCaMy
        ts_url = ts_name + '/' + ts
        ts_content = GetResponse(url=ts_url).content
        with open('video\\' + title + '.mp4', mode='ab') as f:
            f.write(ts_content)
    print(title, '视频保存成功')


def GetVideoID():
    """获取视频ID"""
    # 请求网址
    url = 'https://www.acfun.cn/u/29946310?quickViewId=ac-space-video-list&reqID=1&ajaxpipe=1&type=video&order=newest&page=2&pageSize=20&t=1709197853625'
    # 发送请求 + 获取数据
    html = GetResponse(url=url).text
    # 解析数据, 提取视频ID
    video_id_list = re.findall('"atomid.*?":.*?"(\d+).*?",', html)
    return video_id_list



if __name__ == '__main__':
    video_id_list = GetVideoID()
    # for循环遍历, 提取列表中id
    for video_id in video_id_list:
        title, m3u8_url = GetVideo(ac=video_id)
        Save(title=title, m3u8=m3u8_url)