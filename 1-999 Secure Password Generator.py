import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import random
import time
import os
小写 = True
大写 = True
数字 = True
符号 = True
严格 = True
main = tk.Tk()
符号表 = " !#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
def 小写字母():
    global 小写
    小写 = 1 - 小写
    小写按钮.configure(text=["禁","小"][小写])
def 大写字母():
    global 大写
    大写 = 1 - 大写
    大写按钮.configure(text=["禁","大"][大写])
def 数字命令():
    global 数字
    数字 = 1 - 数字
    数字按钮.configure(text=["禁","数"][数字])
def 符号命令():
    global 符号
    符号 = 1 - 符号
    符号按钮.configure(text=["禁","符"][符号])
def 生成(path:str|None):
    os.system("cls")
    n = 长度输入.get()#yes
    time_wait = 延迟.get()
    if(n == "" or not n.isdigit() or (time_wait != "" and not time_wait.isdigit()) or 大写 == 小写 == 数字 == 符号 == False):
        return
    if(time_wait == ""):
        time_wait = 0
    n = int(n)
    try:
        if(float(time_wait) < 0):
            return
        else:
            time_wait = float(time_wait)
    except BaseException:
        print("类型错误!请检查\"等待时间\"")
        return
    onlytype = False
    if(大写 + 小写 + 数字 + 符号 == 1):
        onlytype = True
    time.sleep(time_wait)#伪等待，别说了
    lasttype = 0
    out = ""
    for x in range(n):  # n长度
        while 1:  # 一直生成
            m = random.randint(0, 3)  # 随机类型
            if(m == lasttype and not onlytype):
                continue
            if (m == 0 and 小写):
                out += chr(97 + random.randint(0, 25))
                lasttype = 0
                break
            if (m == 1 and 大写):
                out += chr(65 + random.randint(0, 25))
                lasttype = 1
                break
            if (m == 2 and 数字):
                out += str(random.randint(0, 9))
                lasttype = 2
                break
            if (m == 3 and 符号):
                out += 符号表[random.randint(0, 31)]
                lasttype = 3
                break
    if(type(path) == str):
        open(path,'w',encoding='utf-8').write(out)
    else:
        print(out)
小写按钮 = tk.Button(master=main, text="小", command=小写字母)
小写按钮.grid(column=0, row=0)
大写按钮 = tk.Button(master=main, text="大", command=大写字母)
大写按钮.grid(column=1, row=0)
数字按钮 = tk.Button(master=main, text="数", command=数字命令)
数字按钮.grid(column=2, row=0)
符号按钮 = tk.Button(master=main, text="符", command=符号命令)
符号按钮.grid(column=3, row=0)
长度输入 = tk.Entry(master=main,width=10)
长度输入.grid(column=1, row=2, columnspan=3)
tk.Label(master=main, text="长").grid(column=0, row=2)
tk.Button(master=main, text="生", command=lambda:生成(None)).grid(column=1, row=3)
tk.Label(master=main, text="延").grid(column=2, row=3)
延迟 = tk.Entry(master=main,width=6)
延迟.grid(column=3, row=3)
保存按钮 = tk.Button(main,text="存",command=lambda:生成(asksaveasfilename()))
保存按钮.grid(column=0, row=3)
main.mainloop()