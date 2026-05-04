def game(message, user):
    usern_number = message.text

    if usern_number.isdigit():
        usern_number = int(usern_number)
        print(user.secnum)
        if usern_number > user.secnum:
            out_text = 'Чуть-чуть поменьше'
        elif usern_number < user.secnum:
            out_text = 'Чуть-чуть побольше'
        elif usern_number == user.secnum:
            out_text = 'Да'
            user.city_game = False
    else:
        out_text = 'Пиши нормально, придурок'
    return out_text