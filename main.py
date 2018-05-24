
from constants import TOKEN
from messages import HELLO
from telebot import types
import telebot
import messages
import requests


bot = telebot.TeleBot(TOKEN)


markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('Football')
itembtnv = types.KeyboardButton('Basketball')
itembtnc = types.KeyboardButton('Hockey')
itembtnd = types.KeyboardButton('Tennis')
itembtne = types.KeyboardButton('UFC')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, I am a sport_bot and I will help you to find latest news of the sport world. Send me command /info and I will resend you all commands that I have.")

@bot.message_handler(commands=['sports'])
def get_news(message):
    # bot.reply_to(message, CURRENT_WEATHER)
    # print(message)
    # bot.send_message(message.chat.id, CURRENT_WEATHER)
    #my_message = str(message)
    # database.insert({'msg': my_message})
    print('inserted')
    bot.send_message(message.chat.id, "Choose the type of sport:", reply_markup=markup)

@bot.message_handler(commands=['info'])
def give_info(message):
    print("informed")
    bot.send_message(message.chat.id,"These are all commands that I have:\n"
        "/originalsources - this command will direct you into original news web-sites\n"
        "/sports - you have to choose kind of sport which you prefer to know latest news\n"
        "/eldar")

@bot.message_handler(commands=['originalsources'])
def start_menu(message):
    print("original")
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    url_button = types.InlineKeyboardButton(text="QAZSPORT", url="http://kazsport.kaztrk.kz/")
    url_button1 = types.InlineKeyboardButton(text="Soccer365", url="https://soccer365.ru/articles/")
    url_button2 = types.InlineKeyboardButton(text="Hockey-World", url="https://hockeyworld.net/")
    url_button3 = types.InlineKeyboardButton(text="NBA", url="https://nba.com/")
    url_button4 = types.InlineKeyboardButton(text="Tennis", url="https://raketka.kz/")
    url_button5 = types.InlineKeyboardButton(text="UFC", url="https://uk.ufc.com/")
    url_button6 = types.InlineKeyboardButton(text="EuroSport", url="https://eurosport.com/")
    url_button7 = types.InlineKeyboardButton(text="Wrestling", url="https://nba.com/")
    keyboard.add(url_button,url_button1,url_button2,url_button3,url_button4,url_button5,url_button6,url_button7)
    bot.send_message(message.chat.id, "Select a link of the site that you want", reply_markup=keyboard)

@bot.message_handler(regexp="Football")
def show_football_news(message):
    print('soccer')
    bot.send_message(message.chat.id,'Расширенная заявка сборной Сербия на ЧМ-2018\n'
'20:06, 24.05.2018\n'
'Наставник сербов Младен Крстаич объявил расширенный список футболистов, которые готовятся к ЧМ-2018 в России\n.'
'http://soccer365.ru/news/8581/\n'
'ЧМ-2018. Группа D. Аргентина\n'
'20:02, 24.05.2018\n'
'Soccer365.ru знакомит вас с командами-участницами ЧМ-2018, который пройдет в России. На очереди финалист прошлого чемпионата мира - сборная Аргентины.\n'
'http://soccer365.ru/news/8577/\n'
'5 причин, почему Реал должен волноваться перед Ливерпулем в финале ЛЧ\n'
'19:46, 24.05.2018\n'
'Soccer365 представляет вашему вниманию перевод части материала авторитетного британского ресурса FourFourTwo.\n'
'http://soccer365.ru/news/8580/\n'
'ЧМ-2018. Группа С. Франция\n'
'01:42, 24.05.2018\n'
'Soccer365.ru продолжает знакомить с командами-участницами ЧМ-2018. Очередное превью расскажет о шансах недавних серебряных призеров Евро-2016.\n'
'http://soccer365.ru/news/8579/\n'
'ЧМ-2018. Группа В. Португалия\n'
'19:39, 22.05.2018\n'
'Soccer365.ru продолжает знакомить читателей сайта с командами-участницами ЧМ-2018. Второй выпуск посвящен европейским бразильцам.\n'
'http://soccer365.ru/news/8576/\n'
'Заявка сборной Аргентины на ЧМ-2018\n'
'00:40, 22.05.2018\n'
'Наставник аргентинцев Хорхе Сампаоли огласил итоговый состав сборной на ЧМ-2018, который этим летом пройдет в России.\n'
'http://soccer365.ru/news/8575/\n'
'ЧМ-2018. Группа А. Россия\n'
'21:57, 21.05.2018\n'
'Soccer365.ru представляет команды, участвующие в Чемпионате мира 2018 года\n'
'http://soccer365.ru/news/8572/\n'
'Заявка сборной Хорватии на ЧМ-2018\n'
'19:12, 21.05.2018\b'
'Наставник хорватов Златко Далич огласил итоговый состав сборной на ЧМ-2018, который этим летом пройдет в России.\n'
'http://soccer365.ru/news/8574/\n'
'Заявка сборной Испании на ЧМ-2018\n'
'18:39, 21.05.2018\n'
'Наставник испанцев Хулен Лопетеги огласил итоговый состав сборной на ЧМ-2018, который этим летом пройдет в России.\n'
'http://soccer365.ru/news/8573/\n'
'Расширенная заявка сборной Бельгии на ЧМ-2018\n'
'16:48, 21.05.2018\n'
'Наставник бельгийцев Роберто Мартинес огласил имена 28 футболистов, которые готовятся к главному турниру нынешнего лета.\n'
'http://soccer365.ru/news/8571/')

if __name__ == '__main__':
    print('Starting sportbot_bot')
    bot.polling()
