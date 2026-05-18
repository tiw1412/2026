import koten as ktn
import telebot
import mainatlast

bot = telebot.TeleBot(ktn.config['token'])


class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.countofpets = 0
        self.classes = {}
        self.names = {}

class Pets:
    def __init__(self, name):
        self.name = name



users = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.from_user.id not in users.keys():
        listreg = [telebot.types.BotCommand('/reg', 'Регистрация')]
        out_text = 'Добро пожаловать! Зарегистрируйтесь для продолжения'
        bot.send_message(message.chat.id, out_text, parse_mode='html')
        bot.set_my_commands(listreg)
    else:
        out_text = 'С возвращением!'
        bot.send_message(message.chat.id, out_text, parse_mode='html')


@bot.message_handler(commands=['reg'])
def reguser(message):
    users[message.from_user.id] = User(id=message.from_user.id, username = message.from_user.username)
    bot.set_my_commands([None])
    out_text = 'Успешно!'
    bot.send_message(message.chat.id, out_text, parse_mode='html')

globaltest = True

@bot.message_handler(commands=['info'])
def reguser(message):
    out_text = '*инфо*'
    bot.send_message(message.chat.id, out_text, parse_mode='html')

@bot.message_handler(commands=['createapet'])
def create_a_pet(message):
    globaltest = True
    return globaltest


@bot.message_handler(content_types=['text'])
def mainmanager(message):
    phase = 0
    while globaltest:
        if phase == 0:
            out_text = mainatlast.naming(message, users[message.from_user.id], phase)
            bot.send_message(message.chat.id, out_text, parse_mode='html')
        if phase == 1:
            out_text = mainatlast.naming(message, users[message.from_user.id], phase)
            bot.send_message(message.chat.id, out_text, parse_mode='html')
            phase += 1
        if phase == 2:
            out_text = mainatlast.naming(message, users[message.from_user.id], phase)
            bot.send_message(message.chat.id, out_text, parse_mode='html')
            phase += 1
bot.polling(non_stop=True, interval=0)