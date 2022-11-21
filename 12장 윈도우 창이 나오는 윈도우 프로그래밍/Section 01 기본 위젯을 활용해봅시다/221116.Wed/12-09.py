from tkinter import *
window = Tk()
window.geometry("400x400")
window.title("애완동물 선택 하기")


def myFunc():
    if var.get() == 1:
        labelImage.configure(image=photo1)
    elif var.get() == 2:
        labelImage.configure(image=photo2)
    else:
        labelImage.configure(image=photo3)


labelText = Label(window, text="좋아하는 동물 투표", fg="blue", font=("궁서체", 20))

var = IntVar()
rb1 = Radiobutton(window, text="강아지", variable=var, value=1)
rb2 = Radiobutton(window, text="고양이", variable=var, value=2)
rb3 = Radiobutton(window, text="토끼", variable=var, value=3)
buttonOK = Button(window, text="사진 보기", command=myFunc)

photo1 = PhotoImage(file="C:/Users/USER/Desktop/dog.gif")
photo2 = PhotoImage(file="C:/Users/USER/Desktop/cat.gif")
photo3 = PhotoImage(file="C:/Users/USER/Desktop/rabbit.gif")

labelImage = Label(window, width=200, height=200, bg="yellow", image=None)

labelText.pack(padx=5, pady=5)
rb1.pack(padx=5, pady=5)
rb2.pack(padx=5, pady=5)
rb3.pack(padx=5, pady=5)
buttonOK.pack(padx=5, pady=5)
labelImage.pack(padx=5, pady=5)

window.mainloop()
