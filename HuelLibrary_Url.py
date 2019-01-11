"""
@Author: 罗申申
@Project: HuelLibraya
@Time: 12/29/2018
"""
import time
from HuelLibrary_Color import Color
#图书馆系统首页
library_index = 'https://wechat.laixuanzuo.com/index.php/reserve/index.html?f=wechat'
#图书馆系统使用规则
library_rule = 'https://wechat.laixuanzuo.com/index.php/center/rule.html'
#图书馆系统个人中心
library_center = 'https://wechat.laixuanzuo.com/index.php/center.html'
#图书馆系统礼物
library_gift = 'https://wechat.laixuanzuo.com/index.php/redbag/list.html'
#图书馆系统违规
library_mistake = 'https://wechat.laixuanzuo.com/index.php/center/mistake.html'
#图书馆系统排行
library_rank = 'https://wechat.laixuanzuo.com/index.php/center/rank.html'
#图书馆系统任务
library_task = 'https://wechat.laixuanzuo.com/index.php/usertask/index.html'
#图书馆系统道具
library_goods = 'https://wechat.laixuanzuo.com/index.php/goods/list.html'
#图书馆系统商店
library_shop = 'https://wechat.laixuanzuo.com/index.php/shop2/index.html'
#图书馆系统打印
library_print = 'https://wechat.laixuanzuo.com/ad_print.html'
#图书馆系统使用记录
library_used = 'https://wechat.laixuanzuo.com/index.php/center/uselog.html'
#图书馆系统监督占位
library_supervise = 'https://wechat.laixuanzuo.com/index.php/marknew/index.html'
#图书馆系统明日预约
library_tomorrow = 'https://wechat.laixuanzuo.com/index.php/prereserve/index.html'
#图书馆系统明日详细预约
library_advance = 'https://wechat.laixuanzuo.com/index.php/reserve/layoutApi/action=prereserve_event&libid='
#图书馆系统立即预约
library_now = 'https://wechat.laixuanzuo.com/index.php/reserve/get/libid='
def get_now_floor(index):

    flag = ''
    #二楼西区
    if str(index) == '20':
        flag = 10073
    #二楼东区
    elif str(index) == '21':
        flag = 10065
    #二楼电子阅览区西区
    elif str(index) == '22':
        flag = 10072
    #二楼电子阅览区东区
    elif str(index) == '23':
        flag = 10071
    #三楼西区
    elif str(index) == '30':
        flag = 10083
    #三楼中区
    elif str(index) == '31':
        flag = 10084
    #三楼东区
    elif str(index) == '32':
        flag = 10082
    #三楼西电子阅览
    elif str(index) == '33':
        flag = 10080
    #三楼东电子阅览
    elif str(index) == '34':
        flag = 10081
    # 四楼西区
    elif str(index) == '40':
        flag = 10087
    # 四楼中区
    elif str(index) == '41':
        flag = 10089
    # 四楼东区
    elif str(index) == '42':
        flag = 10088
    # 四楼西电子阅览
    elif str(index) == '43':
        flag = 10085
    # 四楼东电子阅览
    elif str(index) == '44':
        flag = 10086
    # 五楼西区
    elif str(index) == '50':
        flag = 10090
    # 五楼中区
    elif str(index) == '51':
        flag = 10092
    # 五楼东区
    elif str(index) == '52':
        flag = 10091
    #六楼北区
    elif str(index) == '60':
        flag = 11300
    # 六楼西区
    elif str(index) == '61':
        flag = 11019
    # 六楼中区
    elif str(index) == '62':
        flag = 11033
    # 六楼东区
    elif str(index) == '63':
        flag = 11040
    #七楼西区
    elif str(index) == '70':
        flag = 11054
    #七楼中区
    elif str(index) == '71':
        flag = 11061
    # 七楼东区
    elif str(index) == '72':
        flag = 11068
    # 八楼中区
    elif str(index) == '81':
        flag = 11131
    #八楼东区
    elif str(index) == '82':
        flag = 11096
    # 八楼东电子阅览区
    elif str(index) == '83':
        flag = 11138
    # 九楼西区
    elif str(index) == '90':
        flag = 11082
    # 九楼中区
    elif str(index) == '91':
        flag = 11103
    # 九楼东区
    elif str(index) == '92':
        flag = 11124
    else:
        clr = Color()
        clr.print_red_text("输入不合法！请继续输入：")
    library_url = 'https://wechat.laixuanzuo.com/index.php/reserve/layout/libid={}.html&{}'.format(str(flag),str(int(time.time())))
    return library_url,flag

def get_tomorrow_floor(index):
    flag = ''
    # 二楼西区
    if str(index) == '20':
        flag = 10073
    # 二楼东区
    elif str(index) == '21':
        flag = 10065
    # 二楼电子阅览区西区
    elif str(index) == '22':
        flag = 10072
    # 二楼电子阅览区东区
    elif str(index) == '23':
        flag = 10071
    # 三楼西区
    elif str(index) == '30':
        flag = 10083
    # 三楼中区
    elif str(index) == '31':
        flag = 10084
    # 三楼东区
    elif str(index) == '32':
        flag = 10082
    # 三楼西电子阅览
    elif str(index) == '33':
        flag = 10080
    # 三楼东电子阅览
    elif str(index) == '34':
        flag = 10081
    # 四楼西区
    elif str(index) == '40':
        flag = 10087
    # 四楼中区
    elif str(index) == '41':
        flag = 10089
    # 四楼东区
    elif str(index) == '42':
        flag = 10088
    # 四楼西电子阅览
    elif str(index) == '43':
        flag = 10085
    # 四楼东电子阅览
    elif str(index) == '44':
        flag = 10086
    # 五楼西区
    elif str(index) == '50':
        flag = 10090
    # 五楼中区
    elif str(index) == '51':
        flag = 10092
    # 五楼东区
    elif str(index) == '52':
        flag = 10091
    # 六楼北区
    elif str(index) == '60':
        flag = 11300
    # 六楼西区
    elif str(index) == '61':
        flag = 11019
    # 六楼中区
    elif str(index) == '62':
        flag = 11033
    # 六楼东区
    elif str(index) == '63':
        flag = 11040
    # 七楼西区
    elif str(index) == '70':
        flag = 11054
    # 七楼中区
    elif str(index) == '71':
        flag = 11061
    # 七楼东区
    elif str(index) == '72':
        flag = 11068
    # 八楼中区
    elif str(index) == '81':
        flag = 11131
    # 八楼东区
    elif str(index) == '82':
        flag = 11096
    # 八楼东电子阅览区
    elif str(index) == '83':
        flag = 11138
    # 九楼西区
    elif str(index) == '90':
        flag = 11082
    # 九楼中区
    elif str(index) == '91':
        flag = 11103
    # 九楼东区
    elif str(index) == '92':
        flag = 11124
    else:
        clr = Color()
        clr.print_red_text("输入不合法！请继续输入：")
    library_url = library_advance+"{}".format(str(flag))
    return library_url,flag
