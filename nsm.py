from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Скачать деньги')
root.geometry('400x300')



def show_egassem(): 
    if ptica['state'] == 'disabled' and pri['state'] == 'disabled' and msgntr['textvariable'] != '' and msgntr['textvariable'] != '':
        messagebox.showinfo('Вывод средств', batonstr.get() + ' ' + kp.get() + ': ваши деньги успешно списаны ✔\nТип причности: ' + strint.get())
        minno = Button(text='Отменить дейтсвие', command=roscha)
        minno.place(relx=0.37, rely=0.9)

    else:
        messagebox.showerror('КРИТИЧЕСКАЯ ОШИБКА', 'Нажмите на эту кнопочку выше')
    

def pole():
    msgntr.destroy()
    msgntr2.destroy()

def roscha():
    messagebox.showinfo('Отмена', 'Ошибка, попробуйте еще раз')
    msgntr.destroy()
    msgntr2.destroy()
    maxno.destroy()
    imya.destroy()
    familiya.destroy()
    prinimayuschiy_baton.destroy()
    ptica.destroy()

def happycommand():
    happytext.set('Готов отдать душу взамен на денежки🤑')
    ptica.configure(state='disabled')

def prihozhaya():
    pril = priint.get()
    if pril == 1:
        strint.set('Артемова Мясорубка')
    elif pril == 2:
        strint.set('Красный Глаз')
    elif pril == 3:
        strint.set('Ножный Инструмент')
    elif pril == 4:
        strint.set('Недостаточное количество')
    pribaton.place(relx=0, rely=prel +0.01)


def prichnost():
    messagebox.showinfo('Тип причности', strint.get())
    pri.configure(state='disabled')

def antonin_artaud(event):
    avangard.after(60000, root.destroy())

def lepatron(event):
    root.configure(background="#FF0000")
    avangard.configure(text='Не в коем случае\nне нажимать\nправой кнопкой!')
    avangard.bind('<Button-3>', antonin_artaud)
    # donot = Label(text='(Нажимать только в случае\nнеурегулирования проблемы\nглобального консерватизма)')
    # donot.place(relx=0.5, rely=0.2)

def jewandlry(event):
    holoholst.move(kazanmo, 5, 5)
    holoholst.update()
def lokot(event):
    holoholst.move(kazanmo, -5, -5)
    holoholst.update()
def moscovien(event):
    holoholst.move(kazanmo, 5, -5)
    holoholst.update()
def hailoceania(event):
    holoholst.move(kazanmo, -5, 5)
    holoholst.update()
def leftmarch(event):
    holoholst.move(kazanmo, -5, 37)
    holoholst.update()
def mayakovskiy(event):
    holoholst.move(kazanmo, 50, 10)
    holoholst.update()
def mahakala(event):
    holoholst.move(kazanmo, 0, 5)
    holoholst.update()
def buddha(event):
    holoholst.move(kazanmo, 5, 0)
    holoholst.update()
batonstr = StringVar()
kp = StringVar()

msgntr = Entry(textvariable=batonstr)
msgntr.grid(row=1, column=2)

msgntr2 = Entry(textvariable=kp)
msgntr2.grid(row=2, column=2)


warisgood = IntVar()
happytext = StringVar()
happytext.set('Подтверждаю, что имя и фамилия введены верно')
ptica = Checkbutton(textvariable=happytext, offvalue=0, onvalue=1, variable=warisgood, command=happycommand)
ptica.place(relx=0, rely=0.14)

imya = Label(text='Ваше имя')
imya.grid(row=1, column=1)

familiya = Label(text='Ваша фамилия')
familiya.grid(row=2, column=1)

msgntr.insert(0, 'Имя')
msgntr2.insert(0, 'Фамилия')

maxno = Button(text='Отчистить все', command=pole)
maxno.place(relx=0.4, rely=0.8)

priint = IntVar()
strint = StringVar()
privarka = [('гожин Женя', 1), ('страстен к муравушке', 2), ('стаю к бомжам', 3), ('знаю холодост', 4)]
knopki = []
priqtion = Label(text='Я при...')
prel = 0.20
priqtion.place(rely=prel)
prel += 0.06
for prit, prival in privarka:
    pri = Radiobutton(text=prit, value=prival, variable=priint, command=prihozhaya)
    pri.place(relx=0, rely=prel)
    prel += 0.06

avangard = Button(text='Красный потоп')
avangard.bind('<Button-1>', lepatron)
avangard.place(relx=0.75, rely=0.113)
donot = Label(text='(Нажимать только в случае\nнеурегулирования проблемы\nглобального консерватизма)')
donot.place(relx=0.5, rely=0.2)

holoholst = Canvas(root, width=200, height=150)
holoholst.place(relx=0.5, rely=0.5)
kazanmo = holoholst.create_oval(50, 50, 80, 80,
                                outline="#5E4B14",
                                fill="#9357C7",
                                width=30)
enstein = Button()
wolfenstein = Button()
eidelstein = Button()
epstein = Button()
enstein.place(relx=0.5, rely=0.3)
wolfenstein.place(relx=0.55, rely=0.3)
eidelstein.place(relx=0.5, rely=0.33)
epstein.place(relx=0.55, rely=0.33)
root.bind('<Right>', jewandlry)
root.bind('<Down>', lokot)
root.bind('<Left>', moscovien)
root.bind('<Up>', hailoceania)
root.bind('<a>', leftmarch)
root.bind('<w>', leftmarch)
root.bind('<d>', leftmarch)
root.bind('<s>', leftmarch)
pribaton = Button(text='Я выбрал свой тип причности', command=prichnost)
prinimayuschiy_baton = Button(text='Подписать согласие\nна обработку персональных данных', command=show_egassem, 
                              background="#0A9E2C",  font=("Arial", 12, "italic"))
prinimayuschiy_baton.place(relx=0.5, rely=0.7, anchor='center')

root.mainloop()