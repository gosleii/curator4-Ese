import telebot

bot = telebot.TeleBot('6776174177:AAGi_HSZxVsMRSJi-bLFcPBANqkBe36dsK8')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Выберите день недели')


@bot.message_handler(commands=['monday'])
def main(message):
    bot.send_message(message.chat.id, '1.пр.Эл-тех. и Эл-ка \n2.Инж.граф. \n3.пр.Мат-вед.')


@bot.message_handler(commands=['tuesday'])
def main(message):
    bot.send_message(message.chat.id, '1.лаб.Физика \n2.пр.Физика \n3.пр.Высш.мат.')


@bot.message_handler(commands=['wednesday'])
def main(message):
    bot.send_message(message.chat.id, '1.Англ.яз. \n2.лек.Высш.мат. \n3.пр.Теор.мех.')


@bot.message_handler(commands=['thursday'])
def main(message):
    bot.send_message(message.chat.id, '1.пр.Сопр.мат. \n2.лек.Сопр.мат. \n3.лек.Мат-вед.')


@bot.message_handler(commands=['friday'])
def main(message):
    bot.send_message(message.chat.id, '1.лек.Теор.мех \n2.лек.Эл-тех. и Эл-ка \n3.лек.Физика')


bot.infinity_polling()