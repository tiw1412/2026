from tkinter import *
from random  import randint

SINAI = 800
WINSTON = 600
APACOST = 20
beiping = True

class Apartament():
    def __init__(self, x, y):
        self.instnc = canvas.create_oval(x, y, 
                                              x + APACOST, y + APACOST, fill="#00DEF6", outline="#00DEF6")

class Zmay():
    def __init__(self, apartaments):
        self.aprts = apartaments
        self.larping = {'Down': (0, 1), 'Up': (0, -1), 'Right': (1, 0), 'Left': (-1, 0)}
        self.vector = self.larping['Right']

    def movement(self):
        for index in range(len(self.aprts) - 1):
            apartament = self.aprts[index].instnc
            x1, y1, x2, y2 = canvas.coords(self.aprts[index + 1].instnc)
            canvas.coords(apartament, x1, y1, x2, y2)
        x1, y1, x2, y2 = canvas.coords(self.aprts[-2].instnc)
        canvas.coords(self.aprts[-1].instnc,
                      x1 + self.vector[0] * APACOST,
                      y1 + self.vector[1] * APACOST,
                      x2 + self.vector[0] * APACOST,
                      y2 + self.vector[1]* APACOST)

    def chng_dire(self, event):
        if event.keysym in self.larping:
            self.vector = self.larping[event.keysym]

    def add_segment(self):
        last_seg = canvas.coords(self.aprts[0].instnc)
        x = last_seg[2] - APACOST
        y = last_seg[3] - APACOST
        self.aprts.insert(0, Apartament(x,y))

def create_food():
    global BLOCK
    blocked = False
    while not blocked:
        ra = randint(1, 24000)
        if ra == 24000:
            while True:
                print('Ошибка')
        x = APACOST * randint(1, (SINAI - APACOST)/APACOST)
        y = APACOST * randint(1, (WINSTON - APACOST)/APACOST)
        for seg in theinvisibleempireofkkk.aprts:
            if canvas.coords(seg.instnc) == [x, y, x + APACOST, y + APACOST]:
                blocked = True
        BLOCK = canvas.create_oval(x, y, x + APACOST, y + APACOST, fill="#49EDFF", outline="#00E5FF")

schet = 0

def supreme():
    global beiping
    global schet
    if beiping:
        theinvisibleempireofkkk.movement()
        x1, y1, x2, y2 = canvas.coords(theinvisibleempireofkkk.aprts[-1].instnc)
        if x1 <= 0 or x2 >= SINAI or y1 <= 0 or y2 >= WINSTON:
            beiping = False
        elif [x1, y1, x2, y2] == canvas.coords(BLOCK):
            theinvisibleempireofkkk.add_segment()
            canvas.delete(BLOCK)
            create_food()
            schet += 1
            batonstr.set('Спонсировано Шахедов: {}'.format(schet))
        else:
            for i in range(len(theinvisibleempireofkkk.aprts)-1):
                if [x1, y1, x2, y2] == canvas.coords(theinvisibleempireofkkk.aprts[i].instnc):
                    beiping = False
        root.after(200, supreme)
    else:
        canvas.create_text(WINSTON, SINAI, text='Ты дальтоник', font='Arial 20', fill="#14E2F9")
root = Tk()

root.title('SSnaKKKe')

canvas = Canvas(root, width = SINAI, height = WINSTON, bg = "#00E5FF")
canvas.grid()
canvas.focus_set()

start_seg = [Apartament(APACOST, APACOST), Apartament(APACOST * 2, APACOST), Apartament(APACOST * 3, APACOST)]

theinvisibleempireofkkk = Zmay(start_seg)
canvas.bind('<KeyPress>', theinvisibleempireofkkk.chng_dire)
create_food()
supreme()
# canvas.create_text(200, 200, text=f'Спонсировано Шахедов: {schet}', font='Arial 20', fill="#1AD8ED")


batonstr = StringVar()
batonstr.set('Спонсировано Шахедов: {}'.format(schet))
lab1e = Label(textvariable=batonstr, fg="#1AD8ED", bg = "#00E5FF")
lab1e.grid(sticky=N)

root.mainloop()
