import tkinter
from math import *
import random as rnd
import time
from tkinter import Scale

window = tkinter.Tk()
window.title('Tkinter')
window.geometry('800x800')

x = 0.0
y = 0.0
n = 0.0
xn = 0.0
yn = 0.0
R = 2
C = 60
N = 20000
C1 = 1 # сужение листьев
C2 = 1 # высота
C3 = 1 # ширина


def gen(x, y, n):
    """Асплениум"""
    while n > 0:
        r = rnd.random()
        if r < 0.01:
            xn = 0.0
            yn = 0.16 * y
        elif r < 0.86:
            xn = C1 * 0.85 * x + C3 * 0.04 * y
            yn = C1 * -0.04 * x + 0.85 * y + C2 * 1.6
        elif r < 0.93:
            xn = C1 * 0.2 * x - C3 * 0.26 * y
            yn = C1 * 0.23 * x + 0.22 * y + C2 * 1.6
        else:
            xn = C1 * -0.15 * x + C3 * 0.28 * y
            yn = C1 * 0.26 * x + 0.24 * y + C2 * 0.44
        n -= 1
        x = xn
        y = yn
        yield (xn, yn)
        

def gen2(x, y, n):
    """Телиптерисовый"""
    while n > 0:
        r = rnd.random()
        if r < 0.02:
            xn = 0.0
            yn = 0.25 * y
        elif r < 0.86:
            xn = C1 * 0.95 * x + C3 * 0.005 * y
            yn = C1 * -0.005 * x + 0.93 * y + C2 * 0.5
        elif r < 0.93:
            xn = C1 * 0.035 * x - C3 * 0.2 * y
            yn = C1 * 0.16 * x + 0.04 * y + C2 * 0.02
        else:
            xn = C1 * -0.04 * x + C3 * 0.2 * y
            yn = C1 * 0.16 * x + 0.04 * y + C2 * 0.12
        n -= 1
        x = xn
        y = yn
        yield (xn, yn)
        
        
def gen3(x, y, n):
    """жесть какая-то"""
    while n > 0:
        r = rnd.random()
        if r < 0.02:
            xn = 0.0
            yn = 0.25 * y
        elif r < 0.86:
            xn = C1 * 0.85 * x + C3 * 0.04 * y
            yn = C1 * -0.04 * x + 0.85 * y + C2 * 1.6
        elif r < 0.93:
            xn = C1 * 0.035 * x - C3 * 0.2 * y
            yn = C1 * 0.16 * x + 0.04 * y + C2 * 0.02
        else:
            xn = C1 * -0.04 * x + C3 * 0.2 * y
            yn = C1 * 0.16 * x + 0.04 * y + C2 * 0.12
        n -= 1
        x = xn
        y = yn
        yield (xn, yn)


gen_lst = [gen, gen2, gen3]

gen_current = 0

last = [C, C1, C2, C3, gen_current]

def C_scale_command(event):
    global C
    C = C_scale.get()

c = tkinter.Canvas(width=800, height=800)
C_scale = Scale(window, from_=10, to=100, label='Размер', orient='horizontal', command=C_scale_command)
C_scale.set(C)
C_scale.place(x=0, y=2)

def C1_scale_command(event):
    global C1
    C1 = C1_scale.get() / 100

C1_scale = Scale(window, from_=10, to=100, label='Ширина листьев', orient='horizontal', command=C1_scale_command)
C1_scale.set(C1 * 100)
C1_scale.place(x=105, y=2)

def C2_scale_command(event):
    global C2
    C2 = C2_scale.get() / 100

C2_scale = Scale(window, from_=10, to=200, label="Высота", orient='horizontal', command=C2_scale_command)
C2_scale.set(C2 * 100)
C2_scale.place(x=210, y=2)

def C3_scale_command(event):
    global C3
    C3 = C3_scale.get() / 100

C3_scale = Scale(window, from_=10, to=200, label="Ширина", orient='horizontal', command=C3_scale_command)
C3_scale.set(C3 * 100)
C3_scale.place(x=315, y=2)

def change_gen():
    global gen_current
    gen_current = (gen_current + 1) % len(gen_lst)
    b1.config(text=f'Модель: {gen_lst[gen_current].__doc__}')

b1 = tkinter.Button(window, text=f'Модель: {gen_lst[gen_current].__doc__}', width=50, height=3, command=change_gen)
b1.place(x=420, y=2)


def gen(x, y, n):
    """Обычный"""
    while n > 0:
        r = rnd.random()
        if r < 0.01:
            xn = 0.0
            yn = 0.16 * y
        elif r < 0.86:
            xn = C1 * 0.85 * x + C3 * 0.04 * y
            yn = C1 * -0.04 * x + 0.85 * y + C2 * 1.6
        elif r < 0.93:
            xn = C1 * 0.2 * x - C3 * 0.26 * y
            yn = C1 * 0.23 * x + 0.22 * y + C2 * 1.6
        else:
            xn = C1 * -0.15 * x + C3 * 0.28 * y
            yn = C1 * 0.26 * x + 0.24 * y + C2 * 0.44
        n -= 1
        x = xn
        y = yn
        yield (xn, yn)
        

def gen2(x, y, n):
    """Мутированный"""
    while n > 0:
        r = rnd.random()
        if r < 0.02:
            xn = 0.0
            yn = 0.25 * y
        elif r < 0.86:
            xn = C1 * 0.95 * x + C3 * 0.005 * y
            yn = C1 * -0.005 * x + 0.93 * y + C2 * 0.5
        elif r < 0.93:
            xn = C1 * 0.035 * x - C3 * 0.2 * y
            yn = C1 * 0.16 * x + 0.04 * y + C2 * 0.02
        else:
            xn = C1 * -0.04 * x + C3 * 0.2 * y
            yn = C1 * 0.16 * x + 0.04 * y + C2 * 0.12
        n -= 1
        x = xn
        y = yn
        yield (xn, yn)
    

def create(n):
    r = rnd.random()
    lst = list(gen_lst[gen_current](0, 0, n))
    return lst


def show(i, lst):
    if i < len(lst):
        xn = lst[i][0]
        yn = lst[i][1]
        c.create_oval((C+30) * xn + 400, -C * yn + 800, (C+30) * xn + R + 400, -C * yn + R + 800, fill='black')
        c.pack()
        i += 1
        window.after(1, lambda: show(i, lst))
    else:
        return
    
    
def show_all(lst):
    for i in lst:
        xn = i[0]
        yn = i[1]
        c.create_oval(2 * C * xn + 400, -C * yn + 800, 2 * C * xn + R + 400, -C * yn + R + 800, fill='black')
        c.pack()
        
        
def clear():
    c.delete('all')

    
def main(i, lst):
    global last, C
    if last != [C, C1, C2, C3, gen_current]:
        clear()
        last = [C, C1, C2, C3, gen_current]
        lst = create(N)
        i = 0
    if i < len(lst):
        xn = lst[i][0]
        yn = lst[i][1]
        c.create_oval((C+30) * xn + 400, -C * yn + 800, (C+30) * xn + R + 400, -C * yn + R + 800, fill='black')
        c.pack()
        i += 1
    window.after(1, lambda: main(i, lst))
    
    
main(0, create(N))
    
window.mainloop()

