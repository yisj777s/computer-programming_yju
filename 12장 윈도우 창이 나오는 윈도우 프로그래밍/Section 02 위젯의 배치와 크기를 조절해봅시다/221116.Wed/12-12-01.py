from tkinter import *
# 변수 선언 부분
btnList = [""]*9
fnameList = ["eclair.gif", "froyo.gif", "gingerbread.gif", "honeycomb.gif",
             "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif"]
photoList = [None]*9
i, k, num = 0, 0, 0

# 메인 코드 부분
window = Tk()
window.title("그림 퍼즐")
window.geometry("210x210")

for i in range(0, 9):
    photoList[i] = PhotoImage(file="C:/12장 실습 예제 이미지/"+fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].grid(column=k, row=i)
        num += 1

window.mainloop()
