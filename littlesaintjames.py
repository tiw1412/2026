from tkinter import *
from tkinter import PhotoImage

root = Tk()
root.title('Ненависть к Эпштейну такая вынужденная')
root.geometry('500x500')

tomandjeffrey = Label(root, image=PhotoImage(file='C:\\Users\\bor\\Desktop\\icantbreathe.jpg'),
                      width=30, height=30)
# tomandjeffrey.place(relx=0.5, rely=0.5)
tomandjeffrey.pack()
root.mainloop()
