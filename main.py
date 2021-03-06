import telebot
import websearch
import validating
import config

telegram_key = config.api_key

API_KEY = telegram_key
bot = telebot.TeleBot(API_KEY, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '''ðð®ð¿ðð®ð¿ð± ð¥ð²ð³ð²ð¿ð²ð»ð°ð¶ð»ð´ ðð²ð»ð²ð¿ð®ðð¼ð¿ ð³ð¼ð¿ ðªð²ð¯ðð¶ðð²ð - ááEá©TEáª á·Y á·áªá©áKá·Iááª
    ''')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, '''ððððð ðð ð¥ð  âðð£ð§ðð£ð âðððð£ðððððð ð¾ðððð£ðð¥ð ð£ !

âðððð¤ð ððð¥ðð£ ðªð ð¦ð£ ð¤ðð¥ð ð¥ð  ðð£ððð¥ð ððð¥ðð¥ðð ð ðð âðð£ð§ðð£ð âðððð£ðððððð ð¤ð¥ðªððï¾ï½¥
    
    ''')


@bot.message_handler(commands=['link'])
def send_help(message):
    bot.reply_to(message, "Please enter your site link")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_link(message):
    bot.reply_to(message, "Got it | Checking")
    link = validating.check_url(message.text)
    if link is None:
        bot.reply_to(message, "Invalid link")
    else:
        bot.reply_to(message, "Valid link. Generating link")
        try:
            bot.reply_to(message, websearch.create_site(message.text))
        except:
            bot.reply_to(message, "Server down, Please try again")


bot.polling()
