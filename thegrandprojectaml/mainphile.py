import koten as ktn
import telebot
import mainatlast

bot = telebot.TeleBot(ktn.config['token'])


class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.creating_a_pet = False
        self.pets = []

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


@bot.message_handler(commands=['info'])
def reguser(message):
    out_text = '*инфо*'
    bot.send_message(message.chat.id, out_text, parse_mode='html')

@bot.message_handler(commands=['createapet'])
def create_a_pet(message):
    out_text = 'Придумайте имя своему питомцу'
    users[message.from_user.id.creating_a_pet] = True
    bot.send_message(message.chat.id, out_text, parse_mode='html')

@bot.message_handler(content_types=['text'])
def start_game(message):
    if message.from_user.id.creating_a_pet == True:
        out_text = mainatlast.naming(message, users[message.from_user.id])


    bot.send_message(message.chat.id, out_text, parse_mode='html')
bot.polling(non_stop=True, interval=0)