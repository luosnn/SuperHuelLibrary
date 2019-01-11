"""
@Author: 罗申申
@Project: HuelLibraya
@Time: 12/29/2018
"""
import time
from HuelLibrary_Color import Color
from HuelLibrary_Welcome import welcome
#社会学系同学自行修改，只修改这两处

welcome()
clr = Color()
clr.print_green_text_end("请输入你的微信ID：")
id = input()
clr.print_green_text_end("请输入你的座位纵坐标：")
x = input()
clr.print_green_text_end("请输入你的座位横坐标：")
y = input()
def get_wechat(g_id):
    if g_id =="":
        clr = Color()
        clr.print_red_text("非法ID,程序退出！！！")
        return
get_wechat(id)

Seat_info = {
    'X': int(x),
    "Y": int(y),
}

# 截至，不要再动了
Students_WeChatSessionID = {
    "wechatSESS_ID":str(id)
}

Browser = {
    'Connection': 'keep-alive',
    'Host': "wechat.laixuanzuo.com",
    'Referer':'https://wechat.laixuanzuo.com/index.php/reserve/layout/libid=10065.html&'+str(int(time.time())),
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
    'Cookie':'wechatSESS_ID='+str(id)+'; Hm_lvt_7838cef374eb966ae9ff502c68d6f098='+str(int(time.time()))+'; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098='+str(int(time.time()))+'; FROM_TYPE=weixin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400',
    'X-Requested-With': 'XMLHttpRequest',
}

Verification_Code = [
    'DTb3RP6HttnwDS',
    'Zm67%C3%86YF',
    'FMDDs4sBymznP',
    'CQ2w8Kx6QitBZh7',
    'fzaapfSpixhw',
    'wkzAYtS',
    '225Q5hp4',
    'dNZ6frcKnbted',
    '6F8an8GmKh2pjAN',
    '2WMpkYnmZ5=17',
    'cr3bjxZAJ7AMF3y',
    'iB7p8WNJifGM',
    'BRPMH5',
    'wJWrphQp',
    'GhBikixQsJEr',
    'm7J6fJ7KtXRZ',
    'nZNkM6irGdb',
    'zE446FmfEAkRzsi',
    'WYEGEY5hAD5',
    'ezYw3f',
    'Em6rya32Qs4p',
    'rwHHHapkJ',
    'rb5Eij4nKJi',
    'tz3JpJ',
    'aCAbA7XXEZ6',
    '5GfKr4dwk',
    'ZmhfjkBX2f',
    '8H7SBmmXNQN',
    'KKfixBstziEJjYj',
    'bWDSNmW',
    '225Q5hp4',
    'ezYw3f',
    '7NAp7c2Qc',
    'n5HHWTS',
    'MR5CzSmKs8aK',
    'dcsBzzizpiS6Y7f',
    'iQmkpd335',
    'Q3CXtGhwn',
    'nFDGYkYDfnca',
    'YKQh5M8fm8',
    'rJh5pd8Bi6tk2Jm',
    'A7hYcwdThpfXDs',
    'xdrbtN8M%C2%A5eJpm',
    'YbBWtysQw78mF4D',
    'Sn6iBrnQn',
    '7GxakmDpmxz',
    'fxmWAsRMwM',
    'RAFBQsSQ8PD',
    'HQsRKYa2Y',
    'RQTM52XnkdcpAKA',
    'QDc28PEmPeZhWcd',
    'GfrjAs',
    'BmQAzZzPxBsH7xX',
    'xdrbtN8M%C2%A5eJpm',
    'MR5CzSmKs8aK',
    'MERkHtxFzsZP',
    'MW53STa25jaSzf',
    'NSSJyYp53',
    'Sn6iBrnQn',
    'DeDM7aSKfmKDD8',
    'PQnjzYN7nEsD',
    'mRKtQBCiCenPS',
    'YS2AWje',
    'Q2WBATsSN',
    'Mf6wBQh7yhe',
    'BpW47kne',
    'WnjryCSEkiZF',
    'sECk8n',
    '3mDxm5cz7Sbk',
    'MRSmY8r3mEJe4',
    'p6XPNBBR',
    'sTKmM3nQBnQEx',
    'nAx8ekydKYs',
    'TKMGmdRcMmB7f',
    'mbjsGm',
    'p7amPiTBWMm',
    'YdNtiF',
    'i6R5FwWwbAyH',
    'QMss78iaxK',
    '3hpWAm3TzpDMK7b',
    'XSCF37jDYdz',
    'mc6hz6MN57ZX',
    '6ArCwESBD4',
    'fj7aHyJN',
    'AAywFjhHrN8ZP',
    'ZpksXrYTT',
    '5xNxN6252p7QGT',
    'GDi82CGxz',
    'nym5pzyS8sTzMp',
    'Rd7mhiBe',
]

floor_list = [
    20,21,22,23,30,31,32,33,34,40,41,42,43,44,50,51,52,60,61,62,63,70,71,72,81,82,83,84,90,91,92
]








