'''
============= Telegram-бот на Python ==============

 Мой первый Telegram-бот на Python.
 Адрес бота в интернете: https://t.me/first_AM2022_bot
 Функционирует только когда запущен на ПК из Python
 Его токен: 8182648863:AAHfTHFU5Kazl9prItINnuFYvrODTxdgTMw

'''

import telebot 
#token='8182648863:AAHfTHFU5Kazl9prItINnuFYvrODTxdgTMw'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start']) # если ввести сообщение /start или нажать на кнопку Start
def get_text(message):  # то бот его обработает
   # if message.text.lower() ==  '':
   #bot.send_message(message.chat.id, message)   # служебная инфа о чате и о том, с кем ведётся диалог
   bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!!') # Персональное приветствие
   
   bot.send_message(message.chat.id, 'Это смайлики: 😀 ✌️') # Привет ✌️
   bot.send_message(message.chat.id, '<b>Это жирный текст</b>, <i><u>это тоже форматированный текст</u></i>.', parse_mode='html')
   
bot.infinity_polling(none_stop=True,interval=0) # для непрерывного опроса
#bot.polling() # так тоже можно

