import koten as ktn
import telebot
import random
import time

bot = telebot.TeleBot(ktn.config['token'])


class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.countofpets = 0
        self.pets = {}
    
    def writepets(self):
        lisst = []
        for i in self.pets.values():
            lisst.append(i.name)
        return lisst


class Pets:
    def __init__(self, name, classs):
        self.name = name
        self.classs = classs
        self.iq = float(20)
        self.will = 3
        self.hunger = 10
        self.lucky = 1
        self.score = 0
        self.health = 100
        self.iqlvl = 1
        self.iqstrike = 0
        self.willcount = 0
        self.timeofcreation = time.time()
        self.lasteating = time.time()
    
    def update_score(self):
        self.score = (self.iq * 3 + self.will * 2 - self.hunger * 5 + self.lucky * 2)/(50*(2/self.health))
        return self.score
    
    def scorechecker(self, user, cp):
        if self.score < 1:
            ot = 'Вы не смогли усмотреть за вашим питомцем. Его забрали в приют. Попробуйте снова'
            del user.pets[cp]
            user.countofpets -= 1
            return ot

    def willminuser(self):
        willminus = 0
        print(self.timeofcreation)
        print(int(time.time()))
        nowtime = time.time()
        if (int(nowtime - self.timeofcreation) // 60) > 0:
            bfrzero = (int(nowtime - self.timeofcreation) // 60)
            willminus = -1
            if self.will < 0:
                willminus = 0
                if bfrzero > 0 and bfrzero - (int(nowtime - self.timeofcreation) // 60) <= 0:
                    self.will += 1
            self.timeofcreation += bfrzero * 60
        print(self.will)
        print(self.willcount)
        return willminus
    
    def hungerpluser(self):
        print(self.lasteating)
        print(int(time.time()))
        nowtime = time.time()
        if (int(nowtime - self.lasteating) // 3600) > 0:
            self.hunger += (int(nowtime - self.lasteating) // 3600)
            self.lasteating += int((nowtime - self.lasteating))
            if self.hunger > 48:
                self.health -= 35
                if self.health < 1:
                    self.score = 0
        return (int(nowtime - self.lasteating) // 3600)

users = {}

def userchecker(func):
    def wrap(*args, **kargs):
        if args[0].from_user.id not in users.keys():
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True,
                                               one_time_keyboard = True)
            key_start = telebot.types.KeyboardButton('/reg')
            markup.add(key_start)
            bot.send_message(args[0].chat.id, 'Пожалуйста, зарегестрируйтесь', parse_mode='html', reply_markup=markup)
            return None
        return func(*args, **kargs)
    return wrap

def petchecker(func):
    def wrap(*args, **kargs):
        if users[args[0].from_user.id].countofpets == 0:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True,
                                               one_time_keyboard = True)
            key_start = telebot.types.KeyboardButton('/createapet')
            markup.add(key_start)
            bot.send_message(args[0].chat.id, 'У вас нет питомцев! Создайте нового с помощью /createapet', parse_mode='html', reply_markup=markup)
            return None
        return func(*args, **kargs)
    return wrap

def willchecker(nowawill, ttlwill):
    if nowawill > ttlwill:
        out_text = 'Ваш питомец устал. Потренируйте его волю.'
        return out_text
    else:
        return False

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.from_user.id not in users.keys():
        listreg = [telebot.types.BotCommand('/reg', 'Регистрация')]
        out_text = 'Добро пожаловать! Зарегистрируйтесь для продолжения'
        bot.send_message(message.chat.id, out_text, parse_mode='html')
        bot.set_my_commands(listreg, scope=telebot.types.BotCommandScopeChat(message.chat.id))
    else:
        out_text = 'С возвращением!'
        bot.send_message(message.chat.id, out_text, parse_mode='html')


@bot.message_handler(commands=['reg'])
def reguser(message):
    users[message.from_user.id] = User(id=message.from_user.id, username = message.from_user.username)
    bot.delete_my_commands(scope=telebot.types.BotCommandScopeChat(message.chat.id))
    out_text = 'Успешно! Напишите /info для списка комманд'
    bot.send_message(message.chat.id, out_text, parse_mode='html')



@bot.message_handler(commands=['info'])
def infuser(message):
    out_text = 'Это бот-бурмалдот для создания питомцев. Начните с помощью /createapet. /upgradeiq - усиление мозга, /eat - покушать, /getlucky - испытать удачу, /mypets - посмотреть питомцев, /createapet - создать питомца'
    bot.send_message(message.chat.id, out_text, parse_mode='html')

@bot.message_handler(commands=['createapet'])
@userchecker
def create_a_pet(message):
    out_text = 'Кто есть ваш питомец?'
    bot.send_message(message.chat.id, out_text, parse_mode='html')
    bot.register_next_step_handler(message, naming)

def naming(message):
    classs = str(message.text)
    out_text = f'Неплохая биологическая единица - <b>{message.text}</b>! Как зовут вашего питомца?'
    bot.send_message(message.chat.id, out_text, parse_mode='html')
    bot.register_next_step_handler(message, finalofnaming, classs)

def finalofnaming(message, classs):
    out_text = f'Прекрасное имя, <b>{message.text}</b>. Посмотреть питомца можно с помощью /mypets'
    bot.send_message(message.chat.id, out_text, parse_mode='html')
    users[message.from_user.id].pets[str(users[message.from_user.id].countofpets)] = Pets(message.text, classs)
    users[message.from_user.id].countofpets += 1

@bot.message_handler(commands=['mypets'])
@userchecker
def mypets(message):
    out_text = f'Всего у вас {users[message.from_user.id].countofpets} питомцев: {users[message.from_user.id].writepets()}'

    bot.send_message(message.chat.id, out_text, parse_mode='html')


@bot.message_handler(commands=['upgradeiq'])
@userchecker
def upgradeiq(message):
    out_text = f'Какого из питомцев вы хотите накормить гранитом науки?'
    choise = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    for i in users[message.from_user.id].writepets():
        choise.add(i)
    bot.send_message(message.chat.id, out_text, parse_mode='html', reply_markup=choise)
    bot.register_next_step_handler(message, upgradeiqpart2)

@petchecker
def upgradeiqpart2(message):
    petname = message.text
    for i in users[message.from_user.id].pets.items():
        if petname == i[1].name:
            chosenpet = i[0]
            break
    if petname == i[1].name:
        out_text = f'Выбран питомец {petname}'
        bot.send_message(message.chat.id, out_text, parse_mode='html')
        if users[message.from_user.id].pets[chosenpet].iqlvl == 1:
            first = random.randint(0, 1000)
            second = random.randint(0, 1000)
            yorn = random.choice(['+', '-'])
            if yorn == '+':
                trve = first + second
            else:
                trve = first - second
            yorntext = str(first) + yorn + str(second)

        if users[message.from_user.id].pets[chosenpet].iqlvl == 2:
            first = random.randint(0, 10000)
            second = random.randint(0, 10000)
            yorn = random.choice(['+', '-', '*'])
            if yorn == '+':
                trve = first + second
            elif yorn == '-':
                trve = first - second
            elif yorn == '*':
                trve = first * second
            yorntext = str(first) + yorn + str(second)

        if users[message.from_user.id].pets[chosenpet].iqlvl == 3:
            first = random.randint(0, 100000)
            second = random.randint(1, 100000)
            yorn = random.choice(['+', '-', '*', '/'])
            if yorn == '+':
                trve = first + second
            if yorn == '-':
                trve = first - second
            if yorn == '*':
                trve = first * second
            if yorn == '/':
                trve = first // second
            yorntext = str(first) + yorn + str(second)

        out_text = f'Помогите <b>{users[message.from_user.id].pets[chosenpet].name}</b> решить уравнение: <b>{yorntext}</b>. Округляйте до целых'
        bot.register_next_step_handler(message, upgradeiqpart4, trve, chosenpet)
        bot.send_message(message.chat.id, out_text, parse_mode='html', reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        out_text = 'Такого питомца у вас нет. Но вы всегда можете создать его!'
        bot.send_message(message.chat.id, out_text, parse_mode='html')

def upgradeiqpart4(message, trve, chosenpet):
    users[message.from_user.id].pets[chosenpet].hungerpluser()
    users[message.from_user.id].pets[chosenpet].willcount += 1
    users[message.from_user.id].pets[chosenpet].willcount += users[message.from_user.id].pets[chosenpet].willminuser()
    nul = 'Ваш питомец устал. Потренируйте его волю.'
    print(users[message.from_user.id].pets[chosenpet].willcount)
    if willchecker(users[message.from_user.id].pets[chosenpet].willcount, users[message.from_user.id].pets[chosenpet].will) == nul:
        bot.send_message(message.chat.id, willchecker(users[message.from_user.id].pets[chosenpet].willcount, users[message.from_user.id].pets[chosenpet].will), parse_mode='html')
    else:
        if message.text == str(trve):
            out_text = 'Правильно, питомцу добавлено 0,01 очко IQ, продолжайте не ошибаться, чтобы прокачать питомца!'
            users[message.from_user.id].pets[chosenpet].iqstrike += 1
            if users[message.from_user.id].pets[chosenpet].iqstrike >= 30 and users[message.from_user.id].pets[chosenpet].iqlvl != 3:
                users[message.from_user.id].pets[chosenpet].iqstrike = 0
                users[message.from_user.id].pets[chosenpet].iqlvl += 1
        else:
            out_text = f'Неверно! Серия ответов сброшена, но ваш питомец все равно получил 0,01 очко IQ. Правильный ответ был: {trve}'
            users[message.from_user.id].pets[chosenpet].iqstrike = 0
        bot.send_message(message.chat.id, out_text, parse_mode='html')
        users[message.from_user.id].pets[chosenpet].iq += 0.01
    users[message.from_user.id].pets[chosenpet].update_score()
    nnn = users[message.from_user.id].pets[chosenpet].scorechecker(users[message.from_user.id], chosenpet)
    if nnn:
        bot.send_message(message.chat.id, nnn, parse_mode='html', reply_markup=telebot.types.ReplyKeyboardRemove())



@bot.message_handler(commands=['eat'])
@userchecker
def eatpet1(message):
    out_text = f'Какого из питомцев вы хотите накормить?'
    choise = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    for i in users[message.from_user.id].writepets():
        choise.add(i)
    bot.send_message(message.chat.id, out_text, parse_mode='html', reply_markup=choise)
    bot.register_next_step_handler(message, eatpet2)

@petchecker
def eatpet2(message):
    petname = message.text
    for i in users[message.from_user.id].pets.items():
        if petname == i[1].name:
            chosenpet = i[0]
            break
    if petname == i[1].name:
        out_text = f'Выбран питомец {petname}'
        bot.send_message(message.chat.id, out_text, parse_mode='html')
        if users[message.from_user.id].pets[chosenpet].hunger != 0:
            choise = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
            meat = '🍖ПОКОРМИТЬ'
            water = '💧ПОПОИТЬ'
            choise.add(meat, water)
            out_text = 'Что вы хотите сделать с питомцем?'
            bot.send_message(message.chat.id, out_text, parse_mode='html', reply_markup=choise)
            bot.register_next_step_handler(message, eatpet4, chosenpet)
        else:
            out_text = 'Ваш питомец не голоден, приходите позже'
            bot.send_message(message.chat.id, out_text, parse_mode='html')

    else:
        out_text = 'Такого питомца у вас нет. Но вы всегда можете создать его!'
        bot.send_message(message.chat.id, out_text, parse_mode='html')



def eatpet4(message, chosenpet):
    users[message.from_user.id].pets[chosenpet].hungerpluser()
    users[message.from_user.id].pets[chosenpet].willcount += 1
    users[message.from_user.id].pets[chosenpet].willcount += users[message.from_user.id].pets[chosenpet].willminuser()
    nul = 'Ваш питомец устал. Потренируйте его волю.'
    if willchecker(users[message.from_user.id].pets[chosenpet].willcount, users[message.from_user.id].pets[chosenpet].will) == nul:
        bot.send_message(message.chat.id, willchecker(users[message.from_user.id].pets[chosenpet].willcount, users[message.from_user.id].pets[chosenpet].will), parse_mode='html')
    else:
        if message.text == '🍖ПОКОРМИТЬ':
            users[message.from_user.id].pets[chosenpet].hunger -= 10
            if users[message.from_user.id].pets[chosenpet].hunger < 0:
                users[message.from_user.id].pets[chosenpet].hunger = 0
            out_text = 'Питомец хорошо покушал! Голод ему нипочем'
        elif message.text == '💧ПОПОИТЬ':
            users[message.from_user.id].pets[chosenpet].hunger -= 3
            if users[message.from_user.id].pets[chosenpet].hunger < 0:
                users[message.from_user.id].pets[chosenpet].hunger = 0
            users[message.from_user.id].pets[chosenpet].willcount -= 1
            out_text = 'Питомец сытно попил, его усталость уменьшена'
    bot.send_message(message.chat.id, out_text, parse_mode='html', reply_markup=telebot.types.ReplyKeyboardRemove())
    users[message.from_user.id].pets[chosenpet].update_score()
    nnn = users[message.from_user.id].pets[chosenpet].scorechecker(users[message.from_user.id], chosenpet)
    if nnn:
        bot.send_message(message.chat.id, nnn, parse_mode='html', reply_markup=telebot.types.ReplyKeyboardRemove())



@bot.message_handler(commands=['getlucky'])
@userchecker
def luckthefirst(message):
    out_text = f'Какому из питомцев вы хотите погадать?'
    choise = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    for i in users[message.from_user.id].writepets():
        choise.add(i)
    bot.send_message(message.chat.id, out_text, parse_mode='html', reply_markup=choise)
    bot.register_next_step_handler(message, luckysecond)

@petchecker
def luckysecond(message):
    petname = message.text
    for i in users[message.from_user.id].pets.items():
        if petname == i[1].name:
            chosenpet = i[0]
            break
    if petname == i[1].name:
        out_text = f'Выбран питомец {petname}'
        bot.send_message(message.chat.id, out_text, parse_mode='html')
        trvenum = random.randint(0, 100)
        print(trvenum)
        bot.send_message(message.chat.id, 'Угадайте число от одного до 100', parse_mode='html')
        bot.register_next_step_handler(message, getluck2, trvenum, chosenpet)
    
    else:
        out_text = 'Такого питомца у вас нет. Но вы всегда можете создать его!'
        bot.send_message(message.chat.id, out_text, parse_mode='html')

def getluck2(message, trvnum, chosenpet):
    users[message.from_user.id].pets[chosenpet].hungerpluser()
    users[message.from_user.id].pets[chosenpet].willcount += 1
    users[message.from_user.id].pets[chosenpet].willcount += users[message.from_user.id].pets[chosenpet].willminuser()
    nul = 'Ваш питомец устал. Потренируйте его волю.'
    if willchecker(users[message.from_user.id].pets[chosenpet].willcount, users[message.from_user.id].pets[chosenpet].will) == nul:
        bot.send_message(message.chat.id, willchecker(users[message.from_user.id].pets[chosenpet].willcount, users[message.from_user.id].pets[chosenpet].will), parse_mode='html')
    else:
        trvnum = trvnum
        usern_number = message.text
        if usern_number.isdigit():
            usern_number = int(usern_number)
            print(trvnum)
            if usern_number > trvnum:
                out_text = 'Чуть-чуть поменьше'
            elif usern_number < trvnum:
                out_text = 'Чуть-чуть побольше'
            elif usern_number == trvnum:
                out_text = 'Верно!'
                users[message.from_user.id].pets[chosenpet].lucky += 1
        else:
            out_text = 'Не угадали, попробуйте еще'
        bot.send_message(message.chat.id, out_text, parse_mode='html')
    users[message.from_user.id].pets[chosenpet].update_score()
    nnn = users[message.from_user.id].pets[chosenpet].scorechecker(users[message.from_user.id], chosenpet)
    if nnn:
        bot.send_message(message.chat.id, nnn, parse_mode='html', reply_markup=telebot.types.ReplyKeyboardRemove())

bot.polling(non_stop=True, interval=0)