"""
@Author: 罗申申
@Project: HuelLibraya
@Time: 12/29/2018
"""
import time
from HuelLibrary_Network import network
from HuelLibrary_Color import Color
def cd_index(url):
    clr = Color()
    clr.print_blue_text("正在尝试进入河南财经政法大学图书馆来选座系统首页，请稍等...")
    try:
        result = network(url)
        if result.status_code == 200 and "河南财经政法大学" in str(result.text):
            clr = Color()
            clr.print_green_text("成功进入河南财经政法大学图书馆来选座系统首页！")
            return 'Success'
        else:
            clr = Color()
            clr.print_red_text("尝试进入河南财经政法大学图书馆来选座系统首页" + "失败，失败原因：" + str("返回值未包含指定字符"))
            return 'Error'
    except Exception as e:
        clr = Color()
        clr.print_red_text(str(type(e))+"尝试进入河南财经政法大学图书馆来选座系统失败，失败原因："+str(e))
        return 'Error'

def get_code():
    clr = Color()
    clr.print_green_text("操作提醒：")
    clr.print_green_text("请输入抢座系统下方提醒的下标索引(纯数字),按系统提示和自己选座楼层位置进行合法输入!")
    clr.print_green_text("图书馆楼层序列如下：")
    clr.print_green_text("进入图书馆第 '2' 层楼西区请输入：20")
    clr.print_green_text("进入图书馆第 '2' 层楼东区请输入：21")
    clr.print_green_text("进入图书馆第 '2' 层楼西电子阅览区请输入：22")
    clr.print_green_text("进入图书馆第 '2' 层楼东电子阅览区请输入：23")
    clr.print_green_text("进入图书馆第 '3' 层楼西区请输入：30")
    clr.print_green_text("进入图书馆第 '3' 层楼中区请输入：31")
    clr.print_green_text("进入图书馆第 '3' 层楼东区请输入：32")
    clr.print_green_text("进入图书馆第 '3' 层楼西电子阅览区请输入：33")
    clr.print_green_text("进入图书馆第 '3' 层楼东电子阅览区请输入：34")
    clr.print_green_text("进入图书馆第 '4' 层楼西区请输入：40")
    clr.print_green_text("进入图书馆第 '4' 层楼中区请输入：41")
    clr.print_green_text("进入图书馆第 '4' 层楼东区请输入：42")
    clr.print_green_text("进入图书馆第 '4' 层楼西电子阅览区请输入：43")
    clr.print_green_text("进入图书馆第 '4' 层楼东电子阅览区请输入：44")
    clr.print_green_text("进入图书馆第 '5' 层楼西区请输入：50")
    clr.print_green_text("进入图书馆第 '5' 层楼中区请输入：51")
    clr.print_green_text("进入图书馆第 '5' 层楼东区请输入：52")
    clr.print_green_text("进入图书馆第 '6' 层楼北区请输入：60")
    clr.print_green_text("进入图书馆第 '6' 层楼西区请输入：61")
    clr.print_green_text("进入图书馆第 '6' 层楼中区请输入：62")
    clr.print_green_text("进入图书馆第 '6' 层楼东区请输入：63")
    clr.print_green_text("进入图书馆第 '7' 层楼西区请输入：70")
    clr.print_green_text("进入图书馆第 '7' 层楼中区请输入：71")
    clr.print_green_text("进入图书馆第 '7' 层楼东区请输入：72")
    clr.print_green_text("进入图书馆第 '8' 层楼中区请输入：81")
    clr.print_green_text("进入图书馆第 '8' 层楼东区请输入：82")
    clr.print_green_text("进入图书馆第 '8' 层楼西电子阅览室请输入：83")
    clr.print_green_text("进入图书馆第 '8' 层楼东电子阅览室请输入：84")
    clr.print_green_text("进入图书馆第 '9' 层楼西区请输入：90")
    clr.print_green_text("进入图书馆第 '9' 层楼中区请输入：91")
    clr.print_green_text("进入图书馆第 '9' 层楼东区请输入：92")
    code = input()
    return code

def cd_floor(url,code):

    floor = int(code) // 10
    try:
        result = network(url)
        if result.status_code == 200 and "座位选择" in str(result.text):
            clr = Color()
            clr.print_green_text("成功进入河南财经政法大学图书馆来选座系统第"+str(floor)+"层")
        else:
            clr = Color()
            clr.print_red_text("尝试进入河南财经政法大学图书馆来选座系统第" + str(floor) + "层" + "失败，失败原因：" + str("返回值未包含指定字符"))

            return
    except Exception as e:
        clr = Color()
        clr.print_red_text(str(type(e))+"尝试进入河南财经政法大学图书馆来选座系统第"+str(floor)+"层"+"失败，失败原因："+str(e))
        return

def book(url):
    try:
        result = network(url)
        return result
    except Exception as e:
        clr = Color()
        clr.print_red_text(str(type(e)) + "Error 尝试选座失败，失败原因：" + str(e))
        return 'Error'

def reserve(url):
    try:
        result = network(url)
        return result
    except Exception as e:
        clr = Color()
        clr.print_red_text(str(type(e)) + "Error 尝试选座失败，失败原因：" + str(e))
        return
