import telebot
from telebot import types

TOKEN = '6731771522:AAHNE6M9I00jN0ApmJUPd4yoiMfM_8mtUPY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn2 = types.InlineKeyboardButton('Яблука', callback_data='яблука')
    btn3 = types.InlineKeyboardButton('Вишні', callback_data='вишні')
    btn4 = types.InlineKeyboardButton('Відео', callback_data='video')
    markup.row(btn2,btn3)
    markup.row(btn4)
    bot.reply_to(message, 'Зробіть вибір', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback(call):
    if call.data == 'яблука':
        with open('C:/Users/ASUS/Pictures/Saved Pictures/1.jpg', 'rb') as photo_file:
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.olx.ua/uk/list/q-яблука/')
            markup.row(btn1)
            bot.send_photo(call.message.chat.id, photo_file, reply_markup=markup)
    elif call.data == 'вишні':
        with open('C:/Users/ASUS/Pictures/Saved Pictures/2.png', 'rb') as photo_file:
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.olx.ua/uk/list/q-вишні/')
            markup.row(btn1)
            bot.send_photo(call.message.chat.id, photo_file, reply_markup=markup)
    elif call.data == 'video':
        with open('C:/Users/ASUS/Videos/For python/1.mp4', 'rb') as video_file:
            bot.send_video(call.message.chat.id, video_file)
    else:
        bot.send_message(call.message.chat.id, 'No')


bot.polling()
