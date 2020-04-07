# -*- coding: UTF-8 -*-
#для корректной работы вам нужно устаyовить библиотеку  easygui (pip install easygui)
import easygui as g


menu=g.buttonbox("                                 ВЫБЕРИТЕ  ФИГУРУ          ",
                    choices=["SQUARE","RECTANGLE","TRIANGLE","KEYSTONE"])


def main_k():
    p=a*4
    w=a*a
    return g.buttonbox(      "Периметр равен "+str(p) + "                                    Площадь равна "+str(w),
                                   choices=["RESTART","QUIT"])

def main_t():
    y = b + d + c
    r=(b*h)/2
    return g.msgbox(      "Периметр равен "+str(y) + "                                     Площадь равна "+str(r))

def main_r():
    o=(m+n)*2
    e=m*n
    return g.msgbox("Периметр равен " + str(o) + "                                     Площадь равна " + str(e))

if(menu=="SQUARE"):
    A= g.enterbox("Введите сторону квадрата")
    a=int(A)
    if a>0:
        main_k()
    else:
        g.msgbox("Квадрата с такой стороной не существует!!!")
        while a<0:
            A= g.enterbox("Попробуйте снова")
            a=int(A)
            if a>0:
                main_k()
elif (menu=="TRIANGLE"):
    B = g.enterbox("Введите первую сторону треугольника")
    b = int(B)
    D = g.enterbox("Введите вторую сторону треугольника")
    d = int(D)
    C = g.enterbox("Введите третью сторону треугольника")
    c = int(C)
    H = g.enterbox("Введите высоту треугольника")
    h = int(H)
    if b>0 and d>0 and c>0 and h>0:
        main_t ()
    else:
        g.msgbox("Треугольника с такой стороной или высотой не существует!!!")
        while b<0 or d<0 or c<0 or h<0:
            B = g.enterbox("Попробуйте снова, введите первую сторону треугольника")
            b = int(B)
            D = g.enterbox("Введите вторую сторону треугольника")
            d = int(D)
            C = g.enterbox("Введите третью сторону треугольника")
            c = int(C)
            H = g.enterbox("Введите высоту треугольника")
            h = int(H)
            if b > 0 and d > 0 and c > 0 and h > 0:
                main_t()
elif (menu=="RECTANGLE"):
    M=g.enterbox("Введите первую сторону прямоугольника")
    m=int(M)
    N=g.enterbox("Введите вторую ссторону прямоугольника")
    n=int(N)
    if m>0 and n>0:
        main_r()
    else:
        g.msgbox("Прямоугольника с такими сторонами не существует !!!")
        while m<0 or n<0:
            M = g.enterbox("Попробуйте снова, введите первую сторону прямоугольника")
            m = int(M)
            N = g.enterbox("Введите вторую ссторону прямоугольника")
            n = int(N)
            if m>0 and n>0:
                main_r()

