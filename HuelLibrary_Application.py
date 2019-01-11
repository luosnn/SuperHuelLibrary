"""
@Author: 罗申申
@Project: HuelLibraya
@Time: 12/29/2018 14:00
"""
import time
import threading
from HuelLibrary_Time import time_for_reserve
from HuelLibrary_Color import Color
from HuelLibrary_Config import floor_list, Verification_Code,Seat_info
from HuelLibrary_Url import library_index, get_now_floor,library_now,get_tomorrow_floor
from HuelLibrary_Floor import cd_index,get_code,cd_floor,book,reserve

if __name__ == "__main__":

    def work_one():
       for i in Verification_Code[:len(Verification_Code)//2+1]:
            try:
                book(url + i + '=' + '{},{}'.format(x, y) + '&yzm=')
            except Exception:
                break
    def work_two():
        for i in Verification_Code[len(Verification_Code)//2+1:]:
            try:
                book(url + i + '=' + '{},{}'.format(x, y) + '&yzm=')
            except Exception:
                break

    result_str = cd_index(library_index)
    if result_str == 'Error':
        clr = Color()
        clr.print_red_text("登录失败，退出程序,原因：错误程度严重，配置出错！！！！！！")
        clr.print_red_text("程序在 10 秒之后退出，重新检查再试!")
        time.sleep(10)
        pass
    else:
        clr = Color()
        clr.print_green_text_end("输入 '0' 立即选座 <--------------------------> 输入 '1' 明天预选座:")
        select = input()
        if select == '0':
            code = get_code()
            while True:
                if int(code) in floor_list:
                    break
                else:
                    clr = Color()
                    clr.print_red_text("严重警告：输入不合法，请继续重新输入！或者退出系统！\n")
                    code = input()
            result_list = get_now_floor(code)
            cd_floor(result_list[0],code)
            url = library_now+str(result_list[1])+'&'
            x = Seat_info.get("X")
            y = Seat_info.get("Y")
            clr = Color()
            clr.print_green_text("正在尝试选座，请稍等...")
            start = time.time()
            threads = []
            t1 = threading.Thread(target=work_one())
            threads.append(t1)
            t2 = threading.Thread(target=work_two())
            threads.append(t2)
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            end = time.time()
            used = end - start
            string = book(url + Verification_Code[9] + '=' + '{},{}'.format(x, y) + '&yzm=')
            if "该座位已经被人预定了" in string.text:
                clr = Color()
                clr.print_red_text("该座位已经被人预定,选座失败！")
                clr.print_red_text("用时：" + str(used) + "秒")
                time.sleep(10)
            elif "您已经预定了座位" in string.text or "参数不正确" in string.text:
                clr = Color()
                clr.print_green_text("OK 成功预选座位！")
                clr.print_red_text("用时：" + str(used) + "秒")
                time.sleep(10)
            elif "退选或自动释放座位 1 分钟内不可选座" in string.text:
                clr = Color()
                clr.print_green_text("退选或自动释放座位 1 分钟内不可选座!")
                clr.print_red_text("用时：" + str(used) + "秒")
                time.sleep(10)
            else:
                clr.print_red_text("选座失败")
                clr.print_red_text("用时：" + str(used) + "秒")
                time.sleep(10)

        else:
            code = get_code()
            while True:
                if int(code) in floor_list:
                    break
                else:
                    clr = Color()
                    clr.print_red_text("严重警告：输入不合法，请继续重新输入！或者退出系统！\n")
                    code = input()
            result = get_tomorrow_floor(code)
            tomorrow_index = result[0]
            flag = result[1]
            state = time_for_reserve()
            if state:
                cd_floor(tomorrow_index,flag)
                x = Seat_info.get("X")
                y = Seat_info.get("Y")
                clr = Color()
                clr.print_green_text("正在尝试选座，请稍等...")
                index = 0
                start = time.time()
                while True:
                    goal = "https://wechat.laixuanzuo.com/index.php/prereserve/save/libid={}&".format(
                            flag) + Verification_Code[index] + '=' + '{},{}'.format(x, y) + '&yzm='
                    try:
                        rsp = reserve(goal)
                        index += 1
                    except Exception:
                        break
                end = time.time()
                used = end - start
                string = book("https://wechat.laixuanzuo.com/index.php/prereserve/save/libid={}&".format(
                            flag) + Verification_Code[9] + '=' + '{},{}'.format(x, y) + '&yzm=')
                if "该座位已经被人预定了" in string.text:
                    clr = Color()
                    clr.print_red_text("该座位已经被人预定,选座失败！")
                    clr.print_red_text("用时：" + str(used) + "秒")
                    time.sleep(10)
                elif "您已经预定了座位" in string.text or "参数不正确" in string.text:
                    clr = Color()
                    clr.print_green_text("OK 成功预选座位！")
                    clr.print_red_text("用时：" + str(used) + "秒")
                    time.sleep(10)
                elif "退选或自动释放座位 1 分钟内不可选座" in string.text:
                    clr = Color()
                    clr.print_green_text("退选或自动释放座位 1 分钟内不可选座!")
                    clr.print_red_text("用时：" + str(used) + "秒")
                    time.sleep(10)
                else:
                    clr.print_red_text("选座失败")
                    clr.print_red_text("用时：" + str(used) + "秒")
                    time.sleep(10)