import random
import telebot

token = '5622740231:AAHAFtpX1vBnrKryyn9-ycptyYG6zZrGlr8'

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def startMessage(message):
    bot.send_message(message.chat.id, "Задай вопрос")

@bot.message_handler(content_types=['text'])
def yesNo(message):
    if message.text[-1] == '?':
        rand = random.randint(0, 1)
        if rand == 0:
            bot.send_message(message.chat.id, "ДА")
        else:
            bot.send_message(message.chat.id, "НЕТ")
    else:
        bot.send_message(message.chat.id, "Это не вопрос")


bot.infinity_polling()