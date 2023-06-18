import tkinter as tk
import random
import sys
import time
import os
#with  open('sample1.txt') as f:
    
小写 = True
大写 = True
数字 = True
符号 = True
main = tk.Tk()
符号表 = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
def 小写字母():
    global 小写
    global 小写按钮
    小写 = 1 - 小写
    小写按钮.configure(text=小写)
def 大写字母():
    global 大写
    global 大写按钮
    大写 = 1 - 大写
    大写按钮.configure(text=大写)
def 数字命令():
    global 数字
    global 数字按钮
    数字 = 1 - 数字
    数字按钮.configure(text=数字)
def 符号命令():
    global 符号
    global 符号按钮
    符号 = 1 - 符号
    符号按钮.configure(text=符号)
def 生成():
    os.system("cls")
    sys.stdout.flush()
    n = 长度输入.get()
    try:
        if(n == ""):
            return
        try:
             n = int(n)
        except BaseException:
            print("类型错误!请检查\"次数\"")
            return
        time_wait = 延迟.get()
        if(time_wait == ""):
            time_wait = 0
        try:
            if(float(time_wait) < 0):
                return
            else:
                time_wait = float(time_wait)
        except BaseException:
            print("类型错误!请检查\"等待时间\"")
            return
        if(大写 == 小写 == 数字 == 符号 == False):
            return
        lasttype = 0
        onlytype = False
        onlytype2 = -1
        if(大写 + 小写 + 数字 + 符号 == 1):
            onlytype = True
            if(大写):
                onlytype2 = 0
            if(小写):
                onlytype2 = 1
            if(数字):
                onlytype2 = 2
            if(符号):
                onlytype2 = 3
        for i in range(n):  # n长度
            time.sleep(time_wait)#伪等待，别说了
            breakN = True
            while (breakN):  # 一直生成
                m = random.randint(0, 3)  # 随机类型
                if(m == lasttype and not onlytype):
                    continue
                if (m == 0 and 小写 == True):
                    print(chr(97 + random.randint(0, 25)),end="")
                    breakN = False
                    lasttype = 0
                if (m == 1 and 大写 == True):
                    print(chr(65 + random.randint(0, 25)),end="")
                    breakN = False
                    lasttype = 1
                if (m == 2 and 数字 == True):
                    print(chr(48 + random.randint(0, 9)),end="")
                    breakN = False
                    lasttype = 2
                if (m == 3 and 符号 == True):
                    print(符号表[random.randint(0, 31)],end="")
                    breakN = False
                    lasttype = 3
                sys.stdout.flush()
    except BaseException as ERR:
        print("ERROR!information={}".format(ERR))
        return


  # rgb(123,182,192)
# row = 行,column = 列
tk.Label(master=main, text="密码中包含:").grid(column=0, row=0)
tk.Label(master=main, text="小写字母").grid(column=0, row=1)
小写按钮 = tk.Button(master=main, text=小写, command=小写字母)
小写按钮.grid(column=1, row=1)
tk.Label(master=main, text="大写字母").grid(column=2, row=1)
大写按钮 = tk.Button(master=main, text=小写, command=大写字母)
大写按钮.grid(column=3, row=1)
tk.Label(master=main, text="数字").grid(column=0, row=2)
数字按钮 = tk.Button(master=main, text=数字, command=数字命令)
数字按钮.grid(column=1, row=2)
tk.Label(master=main, text="符号").grid(column=2, row=2)
符号按钮 = tk.Button(master=main, text=符号, command=符号命令)
符号按钮.grid(column=3, row=2)
长度输入 = tk.Entry(master=main)
长度输入.grid(column=1, row=3, columnspan=3)
tk.Label(master=main, text="长度").grid(column=0, row=3)
生成按钮 = tk.Button(master=main, text="生成", command=生成)
生成按钮.grid(column=1, row=4)
tk.Label(master=main, text="延迟(s)→").grid(column=2, row=4)
延迟 = tk.Entry(master=main,width=6)
延迟.grid(column=3, row=4)
main.mainloop()