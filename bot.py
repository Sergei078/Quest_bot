import telebot
from media import Image, Audio
import json
from Buttons import (markup_quest, markup_quest1, markup_quest0, markup_quest5,
                     markup_menu1, markup_menu2, markup_quest7)

bot = telebot.TeleBot("6524252328:AAEnG0LVC_WLRUCvnBuVELU06Eu82fMN8UA")


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        name = message.chat.first_name
        bot.send_message(message.chat.id, f'<b>Привет, {name}👋\n\n</b>'
                                              f'<i>Пройди квест под названием\n'
                                              f'"Необитаемый остров🏝".\n'
                                              f'Нажимай на "Начать квест"\n\n</i>'
                                              f'<b>Удачи друг!\n</b>', parse_mode='html', reply_markup=markup_menu1)
    except:
        bot.send_message(message.chat.id, 'Произошла ошибка!\n'
                                          'Попробуй еще раз.')


@bot.message_handler(func=lambda message: message.text == "Помощь🤝")
def help_message(message):
    bot.send_message(message.chat.id, 'Свяжись с [создателем](https://t.me/SergeiDobrynkin07)',
                     parse_mode='Markdown',)


@bot.message_handler(func=lambda message: message.text == "Начать квест⚔️")
def start_quest(message):
    try:
        img = Image()
        audio = Audio()
        img1 = img.the_opening_scene()
        audio1 = audio.the_opening_scene_audio()
        with open('location.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
        start = data['locations']['start']['description']
        bot.send_photo(message.chat.id, img1, start, parse_mode='html')
        bot.send_audio(message.chat.id, audio1, reply_markup=markup_menu2)
    except:
        bot.send_message(message.chat.id, 'Произошла ошибка!\n'
                                          'Попробуй еще раз.')


@bot.message_handler(func=lambda message: True)
def quest_forest(message):
    try:
        if message.text == "Далее➡️":
            img = Image()
            audio = Audio()
            img1 = img.scene()
            audio1 = audio.scene_audio1()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc1 = data['locations']['scene1']['description']
            bot.send_photo(message.chat.id, img1, loc1, parse_mode='html')
            bot.send_audio(message.chat.id, audio1, reply_markup=markup_quest)
        elif message.text == "Пойти в лес🏞":
            img = Image()
            audio = Audio()
            img1 = img.scene1()
            audio1 = audio.scene_audio2()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc2 = data['locations']['scene2']['description']
            bot.send_photo(message.chat.id, img1, loc2, parse_mode='html')
            bot.send_audio(message.chat.id, audio1, reply_markup=markup_quest0)
        elif message.text == "Достать кокос🥥":
            img = Image()
            audio = Audio()
            img2 = img.scene3()
            audio2 = audio.scene_audio3()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc3 = data['locations']['scene3']['description']
            bot.send_photo(message.chat.id, img2, loc3, parse_mode='html')
            bot.send_audio(message.chat.id, audio2, reply_markup=markup_quest1)
        elif message.text == "Сделать ночлег🏕":
            img = Image()
            audio = Audio()
            img5 = img.scene4()
            audio5 = audio.scene_audio5()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc4 = data['locations']['scene4']['description']
            bot.send_photo(message.chat.id, img5, loc4, parse_mode='html')
            bot.send_audio(message.chat.id, audio5, reply_markup=markup_quest5)
        elif message.text == "Идти на звук":
            img = Image()
            audio = Audio()
            img6 = img.scene5()
            audio6 = audio.scene_audio6()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc5 = data['locations']['scene5']['description']
            bot.send_photo(message.chat.id, img6, loc5, parse_mode='html')
            bot.send_audio(message.chat.id, audio6, reply_markup=markup_menu1)
        elif message.text == "Идти дальше по лесу🏞":
            img = Image()
            audio = Audio()
            img9 = img.scene6()
            audio9 = audio.scene_audio7()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc6 = data['locations']['scene6']['description']
            bot.send_photo(message.chat.id, img9, loc6, parse_mode='html')
            bot.send_audio(message.chat.id, audio9, reply_markup=markup_menu1)
        elif message.text == "Идти дальше":
            img = Image()
            audio = Audio()
            img3 = img.scene2()
            audio4 = audio.scene_audio4()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc7 = data['locations']['scene7']['description']
            bot.send_photo(message.chat.id, img3, loc7, parse_mode='html')
            bot.send_audio(message.chat.id, audio4, reply_markup=markup_menu1)
        elif message.text == "Остаться в шалаше🏕":
            img = Image()
            audio = Audio()
            img17 = img.scene7()
            audio18 = audio.scene_audio8()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc8 = data['locations']['scene6']['description']
            bot.send_photo(message.chat.id, img17, loc8, parse_mode='html')
            bot.send_audio(message.chat.id, audio18, reply_markup=markup_menu1)
        elif message.text == "Звать помощь🆘":
            img = Image()
            audio = Audio()
            img20 = img.scene8()
            audio20 = audio.scene_audio9()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc9 = data['locations']['scene8']['description']
            bot.send_photo(message.chat.id, img20, loc9, parse_mode='html')
            bot.send_audio(message.chat.id, audio20, reply_markup=markup_quest7)
        elif message.text == "Зажечь сигнальный огонь🔥":
            img = Image()
            audio = Audio()
            img21 = img.scene9()
            audio21 = audio.scene_audio10()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc10 = data['locations']['scene5']['description']
            bot.send_photo(message.chat.id, img21, loc10, parse_mode='html')
            bot.send_audio(message.chat.id, audio21, reply_markup=markup_menu1)
        elif message.text == "Не делать огонь":
            img = Image()
            audio = Audio()
            img22 = img.scene10()
            audio22 = audio.scene_audio11()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc11 = data['locations']['scene6']['description']
            bot.send_photo(message.chat.id, img22, loc11, parse_mode='html')
            bot.send_audio(message.chat.id, audio22, reply_markup=markup_menu1)
        else:
            bot.send_message(message.chat.id, 'Я незнаю такой команды', reply_markup=markup_menu1)
    except:
        bot.send_message(message.chat.id, 'Произошла ошибка!\n'
                                          'Попробуй еще раз.')


bot.polling()