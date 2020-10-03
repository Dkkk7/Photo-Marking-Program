#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from tkinter import IntVar

from PIL import Image, ImageTk
import os
import json
import sys
import datetime

sys.getdefaultencoding()
now_time = datetime.datetime.now()
now_time = str(now_time).replace(':', "_")

root = tk.Tk()
# root.geometry('430x650+40+30')
# lbPic = Frame(root)

root.title("example")

suffix = ('.jpg', '.bmp', '.png')
pics = [p for p in os.listdir('.') if p.endswith(suffix)]
current = -1
pic = ''

all_composition = {}
all_color = {}
all_subject = {}
all_light = {}
all_text = {}
all = {"Text": all_text, "Composition": all_composition,
       "Color": all_color, "Subject": all_subject, "Light": all_light}

# global all_composition


def changePic(flag):
    '''flag=-1表示上一个，flag=1表示下一个'''
    global current
    global pic
    new = current + flag
    if new < 0:
        tkinter.messagebox.showerror('', '这已经是第一张图片了')
    elif new >= len(pics):
        tkinter.messagebox.showerror('', '这已经是最后一张图片了')
    else:
        for i, (k, v) in enumerate(all_composition.items()):
            if i in range(0, 1):
                if sum(v) > 1:
                    tkinter.messagebox.showerror('', '请回到上一张/下一张，%s的Composition最多只能选一个属性≥▽≤' % k)
                elif sum(v) == 0:
                    tkinter.messagebox.showerror('', '请回到上一张/下一张，%s的Composition需要选一个属性=￣ω￣=' % k)
        for i, (k, v) in enumerate(all_color.items()):
            if i in range(0, 1):
                if sum(v) > 1:
                    tkinter.messagebox.showerror('', '请回到上一张/下一张，%s的Color最多只能选一个属性≥▽≤' % k)
                elif sum(v) == 0:
                    tkinter.messagebox.showerror('', '请回到上一张/下一张，%s的Color需要选一个属性=￣ω￣=' % k)
        for i, (k, v) in enumerate(all_subject.items()):
            if i in range(0, 1):
                if sum(v) > 1:
                    tkinter.messagebox.showerror('', '请回到上一张/下一张，%s的Subject最多只能选一个属性≥▽≤' % k)
                elif sum(v) == 0:
                    tkinter.messagebox.showerror('', '请回到上一张/下一张，%s的Subject需要选一个属性=￣ω￣=' % k)
        for i, (k, v) in enumerate(all_light.items()):
            if i in range(0, 1):
                if sum(v) > 1:
                    tkinter.messagebox.showerror('', '请回到上一张/下一张，%s的Light最多只能选一个属性≥▽≤' % k)
                elif sum(v) == 0:
                    tkinter.messagebox.showerror('', '请回到上一张/下一张，%s的Light需要选一个属性=￣ω￣=' % k)
        # 获取要切换的图片文件名
        pic = pics[new]
        all_composition[pic] = [0, 0, 0, 0, 0, 0]
        all_color[pic] = [0, 0, 0, 0, 0, 0]
        all_subject[pic] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        all_light[pic] = [0, 0, 0, 0, 0]
        all_text[pic] = ''
        # 创建Image对象并进行缩放
        img = Image.open(pic)
        w, h = img.size
        ratio = w / h
        if w >= 1000:
            new_w = 500
            new_h = int(new_w / ratio)
        elif h >= 1000:
            new_h = 500
            new_w = int(new_h * ratio)
        else:
            new_h = new_w = 500
        img = img.resize((new_w, new_h))
        # 创建PhotoImage对象，并设置Label组件图片
        im1 = ImageTk.PhotoImage(img)

        lbPic['image'] = im1
        lbPic.image = im1
        current = new

    # Composition, Color, Subject, Light选项
    Composition = tk.Label(root, text="构图(Composition)")
    Composition.pack()
    Composition.place(x=670, y=40)

    CheckVar11 = IntVar()
    CheckVar12 = IntVar()
    CheckVar13 = IntVar()
    CheckVar14 = IntVar()
    CheckVar15 = IntVar()
    CheckVar16 = IntVar()

    def AttendCheckVar11():
        # '^'代表异或
        all_composition[pic][0] = 1 ^ all_composition[pic][0]

    def AttendCheckVar12():
        all_composition[pic][1] = 1 ^ all_composition[pic][1]

    def AttendCheckVar13():
        all_composition[pic][2] = 1 ^ all_composition[pic][2]

    def AttendCheckVar14():
        all_composition[pic][3] = 1 ^ all_composition[pic][3]

    def AttendCheckVar15():
        all_composition[pic][4] = 1 ^ all_composition[pic][4]

    def AttendCheckVar16():
        all_composition[pic][5] = 1 ^ all_composition[pic][5]

    C11 = Checkbutton(root, text="中心构图(Center Composition)", variable=CheckVar11,
                      onvalue=1, offvalue=0, height=3, width=30, command=AttendCheckVar11)
    C12 = Checkbutton(root, text="对称构图(Symmetrical)", variable=CheckVar12,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar12)
    C13 = Checkbutton(root, text="三分线构图(The Rule of Thirds)", variable=CheckVar13,
                      onvalue=1, offvalue=0, height=3, width=30, command=AttendCheckVar13)
    C14 = Checkbutton(root, text="前景构图(Foreground Composition)", variable=CheckVar14,
                      onvalue=1, offvalue=0, height=3, width=30, command=AttendCheckVar14)
    C15 = Checkbutton(root, text="留白构图(Blank Space)", variable=CheckVar15,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar15)
    C16 = Checkbutton(root, text="其他(Others)", variable=CheckVar16,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar16)
    C11.pack()
    C11.place(x=650, y=60)
    C12.pack()
    C12.place(x=870, y=60)
    C13.pack()
    C13.place(x=1030, y=60)
    C14.pack()
    C14.place(x=665, y=100)
    C15.pack()
    C15.place(x=910, y=100)
    C16.pack()
    C16.place(x=1070, y=100)



    Color = tk.Label(root, text="色彩(Color)")
    Color.pack()
    Color.place(x=670, y=180)

    CheckVar21 = IntVar()
    CheckVar22 = IntVar()
    CheckVar23 = IntVar()
    CheckVar24 = IntVar()
    CheckVar25 = IntVar()
    CheckVar26 = IntVar()

    def AttendCheckVar21():
        all_color[pic][0] = 1 ^ all_color[pic][0]

    def AttendCheckVar22():
        all_color[pic][1] = 1 ^ all_color[pic][1]

    def AttendCheckVar23():
        all_color[pic][2] = 1 ^ all_color[pic][2]

    def AttendCheckVar24():
        all_color[pic][3] = 1 ^ all_color[pic][3]

    def AttendCheckVar25():
        all_color[pic][4] = 1 ^ all_color[pic][4]

    def AttendCheckVar26():
        all_color[pic][5] = 1 ^ all_color[pic][5]

    C21 = Checkbutton(root, text="单一颜色(Simple Color)", variable=CheckVar21,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar21)
    C22 = Checkbutton(root, text="邻近色(Similar Color)", variable=CheckVar22,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar22)
    C23 = Checkbutton(root, text="互补色(Complementary Colours)", variable=CheckVar23,
                      onvalue=1, offvalue=0, height=3, width=30, command=AttendCheckVar23)
    C24 = Checkbutton(root, text="暖色调(Warm Tone)", variable=CheckVar24,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar24)
    C25 = Checkbutton(root, text="冷色调(Cool Tone)", variable=CheckVar25,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar25)
    C26 = Checkbutton(root, text="其他(Others)", variable=CheckVar26,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar26)
    C21.pack()
    C21.place(x=665, y=200)
    C22.pack()
    C22.place(x=830, y=200)
    C23.pack()
    C23.place(x=1000, y=200)
    C24.pack()
    C24.place(x=655, y=240)
    C25.pack()
    C25.place(x=825, y=240)
    C26.pack()
    C26.place(x=975, y=240)



    Subject = tk.Label(root, text="取景与主题(Subject)")
    Subject.pack()
    Subject.place(x=670, y=320)

    CheckVar31 = IntVar()
    CheckVar32 = IntVar()
    CheckVar33 = IntVar()
    CheckVar34 = IntVar()
    CheckVar35 = IntVar()
    CheckVar36 = IntVar()
    CheckVar37 = IntVar()
    CheckVar38 = IntVar()
    CheckVar39 = IntVar()

    def AttendCheckVar31():
        all_subject[pic][0] = 1 ^ all_subject[pic][0]

    def AttendCheckVar32():
        all_subject[pic][1] = 1 ^ all_subject[pic][1]

    def AttendCheckVar33():
        all_subject[pic][2] = 1 ^ all_subject[pic][2]

    def AttendCheckVar34():
        all_subject[pic][3] = 1 ^ all_subject[pic][3]

    def AttendCheckVar35():
        all_subject[pic][4] = 1 ^ all_subject[pic][4]

    def AttendCheckVar36():
        all_subject[pic][5] = 1 ^ all_subject[pic][5]

    def AttendCheckVar37():
        all_subject[pic][6] = 1 ^ all_subject[pic][6]

    def AttendCheckVar38():
        all_subject[pic][7] = 1 ^ all_subject[pic][7]

    def AttendCheckVar39():
        all_subject[pic][8] = 1 ^ all_subject[pic][8]

    C31 = Checkbutton(root, text="动物(Animal)", variable=CheckVar31,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar31)
    C32 = Checkbutton(root, text="城市景观(Cityspace)", variable=CheckVar32,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar32)
    C33 = Checkbutton(root, text="人(Human)", variable=CheckVar33,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar33)
    C34 = Checkbutton(root, text="室内景观(Indoor Scene)", variable=CheckVar34,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar34)
    C35 = Checkbutton(root, text="风景(Landscape)", variable=CheckVar35,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar35)
    C36 = Checkbutton(root, text="夜景(Night)", variable=CheckVar36,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar36)
    C37 = Checkbutton(root, text="植物(Plant)", variable=CheckVar37,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar37)
    C38 = Checkbutton(root, text="静物(Still Life)", variable=CheckVar38,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar38)
    C39 = Checkbutton(root, text="其他(Others)", variable=CheckVar39,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar39)
    C31.pack()
    C31.place(x=635, y=340)
    C32.pack()
    C32.place(x=780, y=340)
    C33.pack()
    C33.place(x=930, y=340)
    C34.pack()
    C34.place(x=665, y=380)
    C35.pack()
    C35.place(x=830, y=380)
    C36.pack()
    C36.place(x=970, y=380)
    C37.pack()
    C37.place(x=630, y=420)
    C38.pack()
    C38.place(x=770, y=420)
    C39.pack()
    C39.place(x=910, y=420)

    Light = tk.Label(root, text="用光(Light)")
    Light.pack()
    Light.place(x=670, y=500)

    CheckVar41 = IntVar()
    CheckVar42 = IntVar()
    CheckVar43 = IntVar()
    CheckVar44 = IntVar()
    CheckVar45 = IntVar()

    def AttendCheckVar41():
        all_light[pic][0] = 1 ^ all_light[pic][0]

    def AttendCheckVar42():
        all_light[pic][1] = 1 ^ all_light[pic][1]

    def AttendCheckVar43():
        all_light[pic][2] = 1 ^ all_light[pic][2]

    def AttendCheckVar44():
        all_light[pic][3] = 1 ^ all_light[pic][3]

    def AttendCheckVar45():
        all_light[pic][4] = 1 ^ all_light[pic][4]

    C41 = Checkbutton(root, text="顺光(Frontlight)", variable=CheckVar41,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar41)
    C42 = Checkbutton(root, text="逆光(Backlight)", variable=CheckVar42,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar42)
    C43 = Checkbutton(root, text="侧光(Side Light)", variable=CheckVar43,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar43)
    C44 = Checkbutton(root, text="散射光(Scattered Light)", variable=CheckVar44,
                      onvalue=1, offvalue=0, height=3, width=30, command=AttendCheckVar44)
    C45 = Checkbutton(root, text="其他(Others)", variable=CheckVar45,
                      onvalue=1, offvalue=0, height=3, width=20, command=AttendCheckVar45)
    C41.pack()
    C41.place(x=643, y=520)
    C42.pack()
    C42.place(x=790, y=520)
    C43.pack()
    C43.place(x=940, y=520)
    C44.pack()
    C44.place(x=630, y=560)
    C45.pack()
    C45.place(x=870, y=560)

    entry = tk.Entry(root)
    entry.pack()
    entry.place(x=285, y=60)

    fontStyle = tkFont.Font(family="微软雅黑", size=15)
    text = tk.Label(root, text="请输入照片内容：", font=fontStyle)
    text.pack()
    text.place(x=120, y=53)

    def gettext():
        entry_text = entry.get()  # 获取文本框内容
        print(all_text)
        print(pic)
        all_text[pic] = entry_text

    save = Button(root, text="保存", command=gettext)
    save.pack()
    save.place(x=460, y=53)

    print(pic)
    print(all)
    json_str = json.dumps(all, indent=4, ensure_ascii=False)
    with open('all_attrs_%s.json' % str(now_time), 'w+') as json_file:
        json_file.write(json_str)

# “上一张”按钮
def btnPreClick():
    changePic(-1)
btnPre = tkinter.Button(root, text='上一张', command=btnPreClick)
btnPre.place(x=230, y=650, width=80, height=30)


# “下一张”按钮
def btnNextClick():
    changePic(1)
btnNext = tkinter.Button(root, text='下一张', command=btnNextClick)
btnNext.place(x=370, y=650, width=80, height=30)

lbPic = tk.Label(root, text='test')
lbPic.pack()
lbPic.place(x=100, y=100, width=500, height=500)

changePic(1)

root.mainloop()
