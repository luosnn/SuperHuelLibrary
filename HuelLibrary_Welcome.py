"""
@Author: 罗申申
@Project: HuelLibraya
@Time: 12/29/2018
"""
from HuelLibrary_Color import Color
def welcome():
    clr = Color()
    introduce = '''
    \t\t\t\t河南财经政法大学图书馆来选座自动化系统 v2.1.0 
    '''
    clr.print_red_text_with_blue_bg("*-"*50)
    clr.print_green_text(introduce)
    clr.print_blue_text("\t\t\t\t------Notice：© 版权系下方作者所有，除社会学系指定人群外未授权严禁使用，产生的任何后果都与作者无关！")
    clr.print_blue_text("\t\t\t\t\t\t\t"+"请尊重开发者权利，未经允许不得私自传播该软件!!!")
    clr.print_blue_text("\t\t\t\t------Author：Tech申申 / WeiBo：https://weibo.com/u/5585212629")
    clr.print_red_text_with_blue_bg("*-" * 50)