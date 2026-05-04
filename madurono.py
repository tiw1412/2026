# class Venezuela:
    
#     tanker = 0

#     def __init__(self, name):
#         self.name = name
#         Venezuela.tanker += 1

#     def say_hail(self):
#         print(f'Hail {self.name}!')

#     @staticmethod
#     def pribil():
#         print(f'У Мадуро осталось {Venezuela.tanker} кораблика(-ов) со стиральным порошком')

#     def __del__(self):
#         Venezuela.tanker -= 1
#         if Venezuela.tanker != 0:
#             print(f'У Мадуро осталось {Venezuela.tanker} кораблика(-ов) со стиральным порошком')
#         else:
#             print('Флаг Венесуэлы 1813-1817 напоминает что-то🤔')


# caracas = Venezuela('guess who')
# caracas2 = Venezuela('Mariner')
# Venezuela.pribil()
# caracas.say_hail()
# caracas2.say_hail()

##

class SSchoolMember:

    number = 0
    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age
        print(f'В базе создан человек {self.name}')
    
    def tell(self):
        if self.nationality != 'русский':
            print('Ошибка, попробуйте позже')
        else:
            print(f'Имя: {self.name}')
            print(f'Возраст: {self.age}')
            print(f'Национальность: {self.nationality}')

class Tarant(SSchoolMember):
    lnumber = 0
    def __init__(self, name, nationality, age, yearsinjail):
        SSchoolMember.__init__(self, name, nationality, age)
        self.yrs = yearsinjail
        SSchoolMember.number += 1
        Tarant.lnumber += 1
        if self.nationality != 'русский':
            print(f'Челюдь под номером {SSchoolMember.number} не принят')
        else:
            print(f'Учитель {self.name} под номером {Tarant.lnumber} ({SSchoolMember.number}) и стажем {self.yrs} года (лет) принят')
    
    def tell(self):
        SSchoolMember.tell(self)
        print(f'ID {SSchoolMember.number}')

class Uchenik(SSchoolMember):

    lnumber = 0
    def __init__(self, name, nationality, age, schoolclass, wealth):
        SSchoolMember.__init__(self, name, nationality, age)
        self.sss = schoolclass
        self.icntb = wealth
        SSchoolMember.number += 1
        Uchenik.lnumber += 1
        if self.nationality != 'русский':
            print(f'Челюдь под номером {SSchoolMember.number} не принят')
        elif self.icntb == 'бедный':
            print('Нищету в школу не берем')
        else:
            print(f'Ученик {self.name} под номером {Uchenik.lnumber} ({SSchoolMember.number}), учащийся в {self.sss}-м классе принят')
    
    def tell(self):
        SSchoolMember.tell(self)
        print(f'ID {SSchoolMember.number}')

tesak = Tarant('Максим', 'русский', '39', '2')
vanya = Uchenik('Ваня', 'русский', '12', '7', 'богатый')
johncobil = Uchenik('Джон Кобил', 'таждик', '10', '4', 'бедный')
