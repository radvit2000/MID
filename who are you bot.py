import telebot
token = '5622740231:AAHAFtpX1vBnrKryyn9-ycptyYG6zZrGlr8'

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def startMessage(message):
    bot.send_message(message.chat.id, "Как тебя зовут?")

@bot.message_handler(content_types=['text'])
def hello(message):
    bot.send_message(message.chat.id, f'Привет {message.text}')

bot.infinity_polling()