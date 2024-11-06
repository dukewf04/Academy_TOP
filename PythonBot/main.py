import telebot
from conf import TOKEN

# Объект бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_text(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_support = telebot.types.KeyboardButton('Help me')
    keyboard.add(button_support)
    bot.send_message(chat_id, 'Начнем?', reply_markup=keyboard)


# Обработка сообщений при помощи функции-декоратора
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'Привет'.lower():
        bot.send_message(message.from_user.id, 'Привет! Чем я тебе могу помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Чего тебе надо?')


# Запуск бота
bot.polling(none_stop=True, interval=0)