import telebot
from telebot import types

from telebot_key import *
bot = telebot.TeleBot(TELEBOT_KEY)


@bot.message_handler(commands=['start'])
def main(message):
    print("I am in main!")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("женский")
    btn2 = types.KeyboardButton("мужской")
    btn3 = types.KeyboardButton("Унисекс")
    markup.add(btn1, btn2,btn3)
    bot.send_message(message.chat.id, text='Какой парфюм хотели бы?', reply_markup=markup) #1вопрос

    @bot.message_handler(content_types=['text'])
    def func(message):
        if (message.text == "женский") or (message.text =="мужской") or (message.text =="Унисекс"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Бодрящий на утро.Освежающий аромат, "
                                        "который можно носить на работу/учебу")
            btn2 = types.KeyboardButton("Вечерний. Пряный, плотный аромат")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text="Свежий или вечерний?", reply_markup=markup) #2вопрос

        elif (message.text == "Бодрящий на утро.Освежающий аромат, который можно носить на работу/учебу"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Легкий и воздушный (свежие)")
            btn2 = types.KeyboardButton("Многослойный свежий аромат с ярким акцентом ")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text="Какой характер у вашего аромата?", reply_markup=markup) #3.1.вопрос

        elif (message.text == "Легкий и воздушный (свежие)"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Яркий, искрящийся")
            btn2 = types.KeyboardButton("Чистый и спокойный")
            btn3 = types.KeyboardButton("Акватический (морской)")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, text="Какое настроение у этого аромата?", reply_markup=markup)  # 4.1.1вопрос


        elif (message.text == "Многослойный свежий аромат с ярким акцентом"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Яркий, искрящийся")
            btn2 = types.KeyboardButton("Цветочно-фруктовый")
            btn3 = types.KeyboardButton("Лесная сказка")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, text="Какое настроение у этого аромата?", reply_markup=markup)  # 4.1.2вопрос

        elif (message.text == "Вечерний. Пряный, плотный аромат"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Восточные чувственные ароматы")
            btn2 = types.KeyboardButton("Яркая гурманика")
            btn3 = types.KeyboardButton("Нежные и сладкие ароматы")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, text="Какое настроение у этого аромата?", reply_markup=markup) #3.2вопрос

        elif (message.text == "Восточные чувственные ароматы") or (message.text == "Яркая гурманика") or (message.text == "Нежные и сладкие ароматы"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Ванильные, пудровые, цветочные,")
            btn2 = types.KeyboardButton("Сладкая вата, мёд, выпечка, карамель")
            btn3 = types.KeyboardButton("Мягкое дерево, специи, сочные фрукты")
            btn4 = types.KeyboardButton("Древесные, табачные, амбро-мускусные")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text="Какие ноты нравятся больше?", reply_markup=markup) #4.2.опрос

        elif (message.text == "Яркий, искрящийся") or (message.text == "Цветочно-фруктовый") or (message.text == "Лесная сказка"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Ванильные, пудровые, цветочные,")
            btn2 = types.KeyboardButton("Полевые травы, вода и лотос, прозрачные цветы")
            btn3 = types.KeyboardButton("Ягоды, цитрусовые, сочные фрукты")
            btn4 = types.KeyboardButton("Зеленый чай, бергамот, скошенная трава")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text="Какие ноты нравятся больше?", reply_markup=markup) #4.2.опрос

        elif (message.text == "Яркий, искрящийся") or (message.text == "Чистый и спокойный") or (message.text == "Акватический (морской)"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Белый мускус, ладан, пудровые")
            btn2 = types.KeyboardButton("Полевые травы, вода и лотос, прозрачные цветы")
            btn3 = types.KeyboardButton("Ягоды, цитрусовые, сочные фрукты")
            btn4 = types.KeyboardButton("Зеленый чай, бергамот, скошенная трава")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text="Какие ноты нравятся больше?", reply_markup=markup) # 4.2.опрос









print("start server")
bot.polling(non_stop=True)
