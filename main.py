import telebot

from requests import get
from telebot import types

bot = telebot.TeleBot("5530984093:AAEMUfVKZB5vCETu0DFMgFGNigd54XKZtrQ")

@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.chat.id, "Саламяу")
  bot.send_photo(message.chat.id, get("https://krot.info/uploads/posts/2022-03/thumbs/1646140691_1-krot-info-p-kot-mem-smeshnie-foto-1.jpg").content)

@bot.message_handler(commands=['video'])
def wud(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Драмма", url='https://www.youtube.com/watch?v=6PHg69mkBIo&list=PLmj55h0usuJkM8umDNDe7pB_CMczRXodP&index=13')
    markup.add(button1)
    bot.send_message(message.chat.id, "Я плакал восемь часов(".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=["by"])
def by(message):
    bot.send_message(message.chat.id, "Увидимся")
    bot.send_photo(message.chat.id, get("https://cdn-store.rambler.ru/rcmimg/8f1fa489510cb241432d83674d090131.jpg").content)


bot.polling(none_stop=True)














