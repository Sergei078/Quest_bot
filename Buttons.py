from telebot import types

markup_menu1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Начать квест⚔️")
btn3 = types.KeyboardButton("Помощь🤝")
markup_menu1.add(btn1, btn3)

markup_menu2 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Далее➡️")
markup_menu2.add(btn1)

markup_quest = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Пойти в лес🏞")
btn2 = types.KeyboardButton("Звать помощь🆘")
markup_quest.add(btn1, btn2)

markup_quest0 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Достать кокос🥥")
btn2 = types.KeyboardButton("Идти дальше")
markup_quest0.add(btn1, btn2)

markup_quest1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn3 = types.KeyboardButton("Сделать ночлег🏕")
btn4 = types.KeyboardButton("Идти дальше по лесу🏞")
markup_quest1.add(btn3, btn4)

markup_quest5 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn9 = types.KeyboardButton("Идти на звук")
btn10 = types.KeyboardButton("Остаться в шалаше🏕")
markup_quest5.add(btn9, btn10)

markup_quest6 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn9 = types.KeyboardButton("Пойти в лес🏞")
btn10 = types.KeyboardButton("Дальше звать помощь🆘")
markup_quest6.add(btn9, btn10)

markup_quest7 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn9 = types.KeyboardButton("Зажечь сигнальный огонь🔥")
btn10 = types.KeyboardButton("Не делать огонь")
markup_quest7.add(btn9, btn10)
