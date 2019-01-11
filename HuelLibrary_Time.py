"""
@Author: 罗申申
@Project: HuelLibraya
@Time: 12/29/2018
"""
import time
from HuelLibrary_Color import Color

def time_for_reserve():
    now = time.strftime("%H%M%S", time.localtime())
    if int(now) - int("194950") > 0 and int(now)<int(235959) :
        return True
    else:
        clr = Color()
        clr.print_green_text('当前时间：' + time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()) + "\t还未到图书馆开放预选明日座位时间(19:50)，系统会隔 1 秒监听一次")
        time.sleep(1)
        time_for_reserve()