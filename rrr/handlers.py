import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.InlineKeyboardMarkup()

    btn_start = types.InlineKeyboardButton("Начать", callback_data='start_action')

    markup.add(btn_start)

    bot_name = bot.get_me().first_name

    bot.send_message(message.chat.id, f"{message.from_user.first_name}, приветствую! Я - {bot_name}, ИИ-помощник 🤖, который помогает с подобором подарков.",
        parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'start_action')
def show_commands(call):

    markup_two = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Ответить на 7 вопросов')
    btn2 = types.KeyboardButton("Поговорить с человеком")
    markup_two.add(btn1, btn2)


    bot_name = bot.get_me().first_name

    bot.send_message(call.message.chat.id, 
        f"Вариантов подарочных наборов очень много! У меня есть 7 вопросов, которые помогут мне понять, что порекомендовать именно вам ✨ Начнем?",
        reply_markup=markup_two)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    inline_markup = types.InlineKeyboardMarkup()
    btn3 = types.InlineKeyboardButton("Написать Рустаму", url="https://t.me/RustamPodarok")
    inline_markup.add(btn3)

    inline_markup_webapp = types.InlineKeyboardMarkup()
    webapp_button = types.InlineKeyboardButton(
        "Ответить на 7 вопросов",
        web_app=types.WebAppInfo("https://coffeeinveins.ru/")
    )
    inline_markup_webapp.add(webapp_button)

    if message.chat.type == 'private':
        if message.text == 'Ответить на 7 вопросов':
            bot.send_message(message.chat.id, "Ииии... Поехали!", reply_markup=inline_markup_webapp)
        elif message.text == 'Поговорить с человеком':
            bot.send_message(message.chat.id, "🎁 Нюансы заказа и индивидуальные скидки вы можете обсудить с человеком - менеджером Рустамом", reply_markup=inline_markup)
        else:
            bot.send_message(message.chat.id, "У меня недостаточно данных, чтобы ответить на ваш вопрос :( \n Напишите, пожалуйста, Рустаму @RustamPodarok")

if __name__ == "__main__":
    bot.polling()



# from telegrambot.decorators import command
# from telegrambot.handlers import BaseCommandHandler

# @command('start')
# def start_command(update, context):
#     pass
#     # Handle start command here

# @command('author')
# def author_command(update, context):
#     pass


# class telebot.types.MenuButtonWebApp(web_app, 'Ответить на 5 вопросов', cacao, **kwargs)