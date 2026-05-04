import npyvpmgoh as nvp
import telebot
import random
from voyuhsmr import cities2, gra
from minrtd import game

class Usern:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.city_game = False
        self.user_city = []
        self.number_game = False
        self.secnum = 0

users = {}
hellos = ['Сожгите свой телефон. Прямо сейчас', 'Я гидра, я семиголовая змея. Хочешь упороться?',
          'Хамени погиб от рук лени. Мир праху его 🕋🕯🙏', 'Привет, я Джордж Фоид, я не могу заржать',
          'Агарта против Гипербореи: у кого белее кожа', '15 марта 2019 в Крайстчерче ничего не произошло',
          'Когда подшарил за смешное 🐻🔴👧🚂🙂', 'UAE + Dumbass = ❤']


bot = telebot.TeleBot(nvp.config['token'])

def check_user(func):
    def wrap(*args, **kargs):
        if args[0].from_user.id not in users.keys():
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True,
                                               one_time_keyboard = True)
            key_start = telebot.types.KeyboardButton('/start')
            markup.add(key_start)
            bot.send_message(args[0].chat.id, 'Fy', parse_mode='html', reply_markup=markup)
            return None
        return func(*args, **kargs)
    return wrap

def check_game(user_id):
    if user_id not in users.keys():
        return False
    if users[user_id].city_game:
      return 'city'
    elif users[user_id].number_game:
        return 'numbers'
    else:
        return False

@bot.message_handler(commands=['help'])
def help(message):
    ot = 'Rjvfyls\n\
        /help\n\
        /start\n\
        /city\n\
        /numbergssr'
    bot.send_message(message.chat.id, ot, parse_mode='html')

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id not in users.keys():
        users[message.from_user.id] = Usern(id=message.from_user.id, name=message.from_user.first_name)
    
    out_text = '{hello}\n<b>{user_name}</b>, Вы написали {bot_name}'.format(
        hello = random.choice(hellos),
        user_name = message.from_user.first_name,
        bot_name = nvp.config['name']
    )
    bot.send_message(message.chat.id, out_text, parse_mode='html')
    bot.send_message(message.chat.id, 'Ты уже обречен', parse_mode='html', reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(commands=['city'])
@check_user
def city(message):

    users[message.from_user.id].city_game = \
        not users[message.from_user.id].city_game
    if users[message.from_user.id].city_game:
        bot.send_message(message.chat.id,
                         'Играем в города! Ваш ход',
                         parse_mode='html')
    else:
        bot.send_message(message.chat.id,
                         'Игра закончена',
                         parse_mode='html')
        
@bot.message_handler(commands=['numbergssr'])
@check_user
def nbss(message):

    users[message.from_user.id].number_game = \
        not users[message.from_user.id].number_game
    if users[message.from_user.id].number_game:
        users[message.from_user.id].secnum = random.randint(0, 10000000000000000000000000000)
        bot.send_message(message.chat.id,
                         'Угадайте число от одного до 10^28. С каждой подсказской будем отрезать тебе палец',
                         parse_mode='html')
    else:
        bot.send_message(message.chat.id,
                         f'Сколько пальцев у тебя осталось?, {users[message.from_user.id].secnum}',
                         parse_mode='html')

@bot.message_handler(content_types=['text'])
def txet(message):
    if message.text.lower() in hellos:
        bot.send_message(message.chat.id, random.choice(hellos), parse_mode='html')
        return
    if check_game(message.from_user.id) == 'city':
        out_text = gra(message, users[message.from_user.id])
        bot.send_message(message.chat.id, out_text, parse_mode='html')
    elif check_game(message.from_user.id) == 'numbers':
        out_text = game(message, users[message.from_user.id])
        bot.send_message(message.chat.id, out_text, parse_mode='html')
    out_text = f'Dctvyfchfnmyf {message.text}'
    bot.send_message(message.chat.id, out_text, parse_mode='html')

bot.polling(non_stop=True, interval=0)