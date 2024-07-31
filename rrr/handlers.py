import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):

    inline_markup_webapp = types.InlineKeyboardMarkup()


    btn_webapp = types.InlineKeyboardButton(
        "Ответить на 7 вопросов",
        web_app=types.WebAppInfo("https://rurobotgift.ru/")
    )
    btn_human = types.InlineKeyboardButton("Поговорить с человеком", url="https://t.me/RustamPodarok")

    inline_markup_webapp.add(btn_webapp, btn_human)

    bot_name = bot.get_me().first_name


    # Send picture

    # with open('rr.jpg', 'rb') as photo:
    #     bot.send_photo(
    #         message.chat.id, 
    #         photo, 
    #         caption=f"{message.from_user.first_name}, приветствую! Я - {bot_name}, бот-помощник 🤖\nМой профиль - подбор подарков.\n🎁 Нюансы заказа и индивидуальные скидки вы можете обсудить с человеком - менеджером Рустамом.\n\nА у меня есть 7 вопросов, которые помогут мне понять, что порекомендовать именно вам ✨ Начнем?",
    #         parse_mode='html',
    #         reply_markup=inline_markup_webapp
    #     )

    
    bot.send_message(
        message.chat.id,
        f"{message.from_user.first_name}, приветствую! Я - {bot_name}, бот-помощник 🤖\nМой профиль - подбор подарков.\n🎁 Нюансы заказа и индивидуальные скидки вы можете обсудить с человеком - менеджером Рустамом.\n\nА у меня есть 7 вопросов, которые помогут мне понять, что порекомендовать именно вам ✨ Начнем?",
        parse_mode='html',
        reply_markup=inline_markup_webapp
    )


if __name__ == "__main__":
    bot.polling()