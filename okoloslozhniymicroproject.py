from random import shuffle as shf

class Map():
    rnd = []
    def __init__(self, price, navalniy):
        self.prc = price
        self.nvl = navalniy
    
    def donethngs(self):
        if self.prc in 'TJQK':
            return 10
        else:
            return ' A23456789'.index(self.prc)

    # def otherwaybtw(self):
    #     for i in range(13):
    #         self.rnd.append(i)
    #     if (self.rnd).index > 8:
    #         return 10
    #     else:
    #         return (self.rnd).index + 2
            
    
    def get_rank(self):
        return self.prc
    
    def __str__(self):
        return f'{self.prc}{self.nvl}'
    
class Hand():
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        result = 0
        aces = 0

        for card in self.cards:
            if card.get_rank() == 'A' and aces < 5:
                aces += 1
                q = int(input('1/11 '))
                if q == 11 and aces < 2:
                    result += 11
                if q == 11 and aces > 1:
                    q = input('Хотите перевести тузы в единички? ')
                    if q == 'да':
                        result -= 11
                        result += aces
                    else:
                        print('Моя собака играет лучше тебя')
                if q == 1:
                    result + aces
            else:
                result += card.donethngs()
        print(result)
        return result
    def __str__(self):
        text = f'{self.name} contains:\n'
        for card in self.cards:
            text += str(card)
        text += f'\nHand value: {str(self.get_value())}'
        return text


class Deck():
    def __init__(self):
        ranks = '23456789TJQKA'
        nvl = 'HDNW'
        self.cards = [Map(r, n) for r in ranks for n in nvl]
        shf(self.cards)

    def dlcrd(self):
        return self.cards.pop()


def nega():
    
    d = Deck()
    ph = Hand('Player')
    dh = Hand('Dealer')
    ph.add_card(d.dlcrd())
    ph.add_card(d.dlcrd())
    dh.add_card(d.dlcrd())
    print(ph)
    print('--')
    print(dh)
    igm = True

    while ph.get_value() < 21 and igm == True:
        ans = input('Hit/ler? {h/s}')
        if ans == 'h':
            ph.add_card(d.dlcrd())
            print('Игрок: ', ph)
            print('--')
            if ph.get_value() > 21:
                igm = False
                print('Моя собака играет лучше тебя')
        else:
            print('You stand')
            break


    while dh.get_value() < 17 and igm == True:
        if dh.get_value() < 17:
            dh.add_card(d.dlcrd())
            print('Дил: ',dh)
            if dh.get_value()> 21:
                igm = False
                print('Игрок выиграл')
        else:
            break

    if igm == False:
        if dh.get_value() > ph.get_value():
            'Продай свою собаку чтобы расплатиться с долгами'
        else:
            'Ты победил'

nega()


# card = Map('A', 'H')
# card2 = Map('A', 'R')
# hand = Hand('Friedn')
# hand.add_card(card)
# hand.add_card(card2)
# hand.get_value()
# print(card)