class Raj:
    people_lifted = 0
    def __init__(self, name):
        self.name = name
        self.people_lifted = 0
    
    def duke(self):
        print(f'{self.name} chewed someone')
        self.people_lifted += 1
        Raj.people_lifted += 1
    
    def corstat(self):
        print(f'{self.name} chewed {self.people_lifted} people out of {Raj.people_lifted}')


lifts = []

for i in range(4):
    name = 'AEII' + str(i + 1)
    lifts.append(Raj(name))


lifts[0].duke()
lifts[1].duke()
lifts[1].duke()
lifts[2].duke()
lifts[3].duke()
lifts[2].duke()

for lift in lifts:
    lift.corstat()