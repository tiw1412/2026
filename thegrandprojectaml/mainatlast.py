def naming(message, user, phase):
    if phase == 0:
        out_text = 'Кто есть ваш питомец?'
    if phase == 1:
        user.classes[str(user.countofpets)] = str(message.text)
        out_text = f'Неплохая биологическая единица - <b>{str(message.text)}</b>! Как зовут вашего питомца?'
    if phase == 2:
        user.names[str(user.countofpets)] = str(message)
        out_text = f'Прекрасное имя, <b>{str(message.text)}</b>'

    return out_text