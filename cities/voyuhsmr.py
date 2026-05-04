from src import cities2

import random

random.shuffle(cities2)
def gra(message, user):
    usern_city = message.text.lower()
    last_letter = None
    print(user.user_city)
    print(usern_city)

    if len(user.user_city) != 0:
        if user.user_city[-1][-1] not in ['ь', 'ы', 'ъ']:
            last_letter = user.user_city[-1][-1]
            print(last_letter)
        else:
            last_letter = user.user_city[-1][-2]
    
    if usern_city not in cities2:
        out_text = 'Такого города не сущесвтует.'
    
    elif usern_city in user.user_city:
        out_text = 'Город уже есть'
    
    elif last_letter and usern_city[0] != last_letter:
        out_text = 'Нет'

    else:
        user.user_city.append(usern_city)
        if usern_city[-1] in ['ь', 'ы', 'ъ']:
            last_letter = usern_city[-2]
        else:
            last_letter = usern_city[-1]
        for c in cities2:
            if c not in user.user_city and c[0] == last_letter:
                user.user_city.append(c)
                out_text = f'Ответ принят. Мой город <b>{c}</b>'
                break
        else:
                out_text = 'Я победил'
                user.number_game = False

    return out_text