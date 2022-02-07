from tkinter import Y


x = 0
y = 1

if y <= 100:
    for i in range(1,101):
        x=x+y
        print(x)
        y=y+1
    print("計算を終了する")
