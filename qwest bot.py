import telebot
token = '5622740231:AAHAFtpX1vBnrKryyn9-ycptyYG6zZrGlr8'

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def startMessage(message):
    bot.send_message(message.chat.id, "Начинаем")
    buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = telebot.types.KeyboardButton('В джунгли')
    button2 = telebot.types.KeyboardButton('По пляжу')

    buttons.add(button1, button2)

    bot.send_message(message.chat.id, text='Ты проснулся на берегу моря после кораблекрушения. Куда пойдёшь?', reply_markup=buttons)

@bot.message_handler(content_types=['text'])
def qwest(message):
    if message.text == 'В джунгли':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('Вперёд на охоту')
        button2 = telebot.types.KeyboardButton('Я не охотник, поищу какосы')

        buttons.add(button1, button2)

        bot.send_message(message.chat.id, text='Над тобой прыгают обезьяны, а ты очень голодень. Попытаешься поймать еду?',
                         reply_markup=buttons)

    if message.text == 'По пляжу' or message.text == 'Я не охотник, поищу какосы':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('Попытаюсь залезть на пальму')
        button2 = telebot.types.KeyboardButton('Пойти ловить рыбу')

        buttons.add(button1, button2)

        bot.send_message(message.chat.id, text='На высоком обрыве стоит пальма с какосами.',
                         reply_markup=buttons)

    if message.text == 'Вперёд на охоту':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('Брошусь на помощь')
        button2 = telebot.types.KeyboardButton('Понаблюдаю за представлением')

        buttons.add(button1, button2)

        bot.send_message(message.chat.id, text='Ты погнался за мартышками и наткнулся на старый храм. Кого-то собираются принести в жертву.',
                         reply_markup=buttons)

    if message.text == 'Попытаюсь залезть на пальму':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('Спуститься по лиане как по канату')
        button2 = telebot.types.KeyboardButton('Медлено спускаться')

        buttons.add(button1, button2)

        bot.send_message(message.chat.id, text='Ты сорвал кокос и пытаешься спуститься',
                         reply_markup=buttons)

    if message.text == 'Спуститься по лиане как по канату':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('Начать сначала')
        buttons.add(button1)

        bot.send_message(message.chat.id, text='Лиана оборвалась и ты упал с обрыва. Ты мёртв',
                         reply_markup=buttons)

    if message.text == 'Медлено спускаться':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('Начать сначала')
        buttons.add(button1)

        bot.send_message(message.chat.id, text='Ты успешно спустился. У тебя есть еда. Жизнь удалась',
                         reply_markup=buttons)

    if message.text == 'Пойти ловить рыбу':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('Начать сначала')
        buttons.add(button1)

        bot.send_message(message.chat.id, text='тебя съели крокодилы', reply_markup=buttons)

    if message.text == 'Брошусь на помощь':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('Попытаюсь убежать')
        button2 = telebot.types.KeyboardButton('Схвачу дубину и приму бой')

        buttons.add(button1, button2)

        bot.send_message(message.chat.id, text='На тебя бегут туземцы с копьями. Под ногами валяется огромная дубина',
                         reply_markup=buttons)

    if message.text == 'Схвачу дубину и приму бой':
        button1 = telebot.types.KeyboardButton('Начать сначала')
        buttons.add(button1)

        bot.send_message(message.chat.id, text='Ты смог отбиться от туземцев и спасти человека. '
                                               'Он оказался капитаном корабля и согласился отвезти тебя на большую землю. '
                                               'Ты спасён',
                         reply_markup=buttons)

    if message.text == 'Попытаюсь убежать' or message.text == 'Вонзаешь нож в колено стражника, освобождаешь пленного и бежишь':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('Начать сначала')
        buttons.add(button1)

        bot.send_message(message.chat.id, text='Тебя догнали туземцы и проткнули копьями. Ты умер.',
                         reply_markup=buttons)

    if message.text == 'Понаблюдаю за представлением':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('Приносишь несчастного в жертву')
        button2 = telebot.types.KeyboardButton('Вонзаешь нож в колено стражника, освобождаешь пленного и бежишь')

        buttons.add(button1, button2)

        bot.send_message(message.chat.id, text='Ты наблюдаешь за жертвопринашением из кустов. Неожидано тебя за плечо '
                                               'хватает туземец и приводит к вождю. Под ногами ты видишь серу. Ты '
                                               'схватил её и бросил в факел. Произошёл взрыв. Вождь не может понять демон '
                                               'ты или божество. Чтобы доказать что ты божество тебе необходимо произвести '
                                               'жертвоприношение. Ты подходишь к алтарю, заносишь над человеком нож и ...',
                         reply_markup=buttons)

    if message.text == 'Приносишь несчастного в жертву':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('Начать сначала')
        buttons.add(button1)

        buttons.add(button1, button2)

        bot.send_message(message.chat.id, text='Ты стал божеством. Туземцы почитают тебя как проявление высших сил',
                         reply_markup=buttons)

    if message.text == 'Начать сначала':
        bot.send_message(message.chat.id, "Начинаем")
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = telebot.types.KeyboardButton('В джунгли')
        button2 = telebot.types.KeyboardButton('По пляжу')

        buttons.add(button1, button2)

        bot.send_message(message.chat.id, text='Ты проснулся на берегу моря после кораблекрушения. Куда пойдёшь?',
                         reply_markup=buttons)
bot.infinity_polling()