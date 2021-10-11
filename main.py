import telebot
import websearch
import validating
import config

telegram_key = config.api_key


API_KEY = telegram_key
bot = telebot.TeleBot(API_KEY, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '''𝗛𝗮𝗿𝘃𝗮𝗿𝗱 𝗥𝗲𝗳𝗲𝗿𝗲𝗻𝗰𝗶𝗻𝗴 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿 𝗳𝗼𝗿 𝗪𝗲𝗯𝘀𝗶𝘁𝗲𝘀 - ᑕᖇEᗩTEᗪ ᗷY ᗷᒪᗩᑕKᗷIᖇᗪ
    ''')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, '''𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 ℍ𝕒𝕣𝕧𝕒𝕣𝕕 ℝ𝕖𝕗𝕖𝕣𝕖𝕟𝕔𝕚𝕟𝕘 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 !

ℙ𝕝𝕖𝕒𝕤𝕖 𝕖𝕟𝕥𝕖𝕣 𝕪𝕠𝕦𝕣 𝕤𝕚𝕥𝕖 𝕥𝕠 𝕔𝕣𝕖𝕒𝕥𝕖 𝕔𝕚𝕥𝕒𝕥𝕚𝕠𝕟 𝕚𝕟 ℍ𝕒𝕣𝕧𝕒𝕣𝕕 ℝ𝕖𝕗𝕖𝕣𝕖𝕟𝕔𝕚𝕟𝕘 𝕤𝕥𝕪𝕝𝕖ﾟ･
    
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
        bot.reply_to(message, websearch.create_site(message.text))


bot.polling()
