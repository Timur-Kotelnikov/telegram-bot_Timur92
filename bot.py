import telebot
import funcs

bot = telebot.TeleBot(funcs.telegram_token)


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_chat_action(chat_id=message.chat.id, action='typing')
    bot.send_sticker(chat_id=message.chat.id,
                     sticker='CAACAgEAAxkBAAICzWMPQDSBg2nNxmbdMLW35gABYp3AdAAC3QADqUJpR-QuzcszCjL-KQQ')
    bot.send_message(chat_id=message.chat.id, text=f'Hello <b>{message.from_user.first_name}, '
                                                   f'<u>{message.from_user.username}</u></b>!',
                     parse_mode='html')
    bot.send_message(chat_id=message.chat.id, text='How can I help you? Try /info')


@bot.callback_query_handler(func=lambda call: True)
def call_hand(call):
    if call.data == 'currency':
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(chat_id=call.message.chat.id, action='typing')
        bot.send_message(chat_id=call.message.chat.id, text=f'{funcs.currency()}')
    if call.data == 'crypto_currency':
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(chat_id=call.message.chat.id, action='typing')
        bot.send_message(chat_id=call.message.chat.id, text=f'{funcs.crypto_currency()}')
    if call.data == 'weather':
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(chat_id=call.message.chat.id, action='typing')
        bot.send_message(chat_id=call.message.chat.id, text='City?')

        @bot.message_handler()
        def w1(message):
            bot.send_chat_action(chat_id=message.chat.id, action='typing')
            bot.send_message(chat_id=message.chat.id, text=f'{funcs.weather(message.text)}')
    if call.data == 'joke':
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_photo(chat_id=call.message.chat.id, photo=funcs.memes())
    if call.data == 'cat':
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_photo(chat_id=call.message.chat.id, photo=funcs.cat())
    if call.data == 'NASA':
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_photo(chat_id=call.message.chat.id, photo=funcs.nasa())


@bot.message_handler(commands=['info'])
def send_info(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup.add(telebot.types.InlineKeyboardButton(text='Visit my web-site',
                                                  url='https://timur-kotelnikov.herokuapp.com/'),
               telebot.types.InlineKeyboardButton(text='Weather', callback_data='weather'),
               telebot.types.InlineKeyboardButton(text='Major currencies rates', callback_data='currency'),
               telebot.types.InlineKeyboardButton(text='BTC price', callback_data='crypto_currency'),
               telebot.types.InlineKeyboardButton(text='Joke', callback_data='joke'),
               telebot.types.InlineKeyboardButton(text='Cats', callback_data='cat'),
               telebot.types.InlineKeyboardButton(text='Picture of the Day by NASA', callback_data='NASA'))
    bot.send_message(chat_id=message.chat.id, text='Enjoy!', reply_markup=markup)


@bot.message_handler(content_types='sticker')
def get_id(message):
    bot.send_message(chat_id=message.chat.id, text=message.sticker)


bot.polling(non_stop=True)
