from tkinter import *
import random
import time
import math

w = 800
h = 600
count = 0
miss = 0
color = "#FFFF00"
size = 50
time_start = 0
x = w/2
y = h/2
result_t = 0
result_a = 0

def draw_circle(size, color):
    global x
    global y
    
    canvas.create_arc(x-size/2, y-size/2, x+size/2, y+size/2, start=0, extent=359, style=CHORD, fill=color)

def on_click(event):
    global x
    global y
    global count
    global miss
    global time_start
    global result_t
    global result_a

    canvas.delete("all")

    if time_start == 0:
        time_start = time.time()

    if (size/2)*(size/2) >= (event.x-x)*(event.x-x) + (event.y-y)*(event.y-y):
        count = count + 1
        if count == i_count:
            result_t = round(time.time()-time_start, 3)
            result_a = round((count/(count+miss))*100, 3)
    else:
        miss = miss + 1

    if count >= i_count:
        canvas.create_text(10, 10, text=f"経過時間: {result_t}秒", anchor="w")
        canvas.create_text(10, 20, text=f"精度: {result_a}%", anchor="w")

    x = size/2 + math.floor(random.random()*(w-size))
    y = size/2 + math.floor(random.random()*(h-size))

    draw_circle(size, color)

while True:

    try:
        i_count = int(input("回数を入力 > "))
        break
    except:
        print("不正な値\n")

while True:

    try:
        i_size = int(input("大きさ(px)を入力 > "))
        size = i_size
        break
    except:
        print("不正な値\n")


tk = Tk()
canvas = Canvas(tk, width=w, height=h, bg="white")
canvas.pack()

draw_circle(size, color)

canvas.bind("<Button-1>", on_click)
