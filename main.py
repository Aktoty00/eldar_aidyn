
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
    url_button1 = types.InlineKeyboardButton(text="Soccer365", url="http://soccer365.ru/articles/")
    url_button2 = types.InlineKeyboardButton(text="Hockey-World", url="https://hockey-world.net/")
    url_button3 = types.InlineKeyboardButton(text="NBA", url="https://nba.com/")
    url_button4 = types.InlineKeyboardButton(text="Tennis", url="https://raketka.kz/")
    url_button5 = types.InlineKeyboardButton(text="UFC", url="http://uk.ufc.com/")
    url_button6 = types.InlineKeyboardButton(text="EuroSport", url="https://www.eurosport.com/")
    url_button7 = types.InlineKeyboardButton(text="Wrestling", url="https://www.ijf.org/news")
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

@bot.message_handler(regexp="Basketball")
def show_football_news(message):
    print('basket')
    bot.send_message(message.chat.id,'В Алматы завершился 13-й юношеский Чемпионат по баскетболу «Кубок надежды»\n'
'http://nbf.kz/news/?id=1561\n'
'Нурсултан  Назарбаев поддержал инициативу «Challenge Другой ты!»\n'
'http://nbf.kz/news/?id=1560\n'
'Итоги турнира по баскетболу среди столичных школьных команд приуроченный к 20-летию Астаны\n'
'http://nbf.kz/news/?id=1558\n'
'Легенды баскетбола СССР провели мастер-класс для воспитанников детских домов в Алматы\n'
'http://nbf.kz/news/?id=1557\n'
'Интервью с участниками Jr. NBA Europe Selection Camp 2018\n'
'http://nbf.kz/news/?id=1556\n'
'В Алматы остоялась церемония открытия Чемпионата Казахстана по баскетболу «Кубок Надежды 2018»\n'
'http://nbf.kz/news/?id=1555\n'
'В Алматы стартовал 13-й юношеский Чемпионат по баскетболу «Кубок надежды»\n'
'http://nbf.kz/news/?id=1554\n'
'Турнир по баскетболу среди столичных школьных команд приуроченный к 20-летию Астаны\n'
'http://nbf.kz/news/?id=1552\n'
'Сборная Казахстана выиграла «Кубок Победы 2018»!\n'
'http://nbf.kz/news/?id=1551\n'
'Чемпионат Казахстана - "Кубок Надежды 2018"\n'
'http://nbf.kz/news/?id=1550\n'
'С Днем рождения Марат Сагидович!\n'
'http://nbf.kz/news/?id=1549\n'
'В Алматы состоится тренерский семинар с участием Олимпийских чемпионов Алжана Жармухамедова и Ивана Едешко\n'
'http://nbf.kz/news/?id=1520)\n')

@bot.message_handler(regexp="Hockey")
def show_football_news(message):
    print('hock')
    bot.send_message(message.chat.id,
            'НХЛ. "Вегас" ждёт соперника по финалу\n'       
'http://articles-nhl/193802-nkhl-vegas-zhdjot-sopernika-po-finalu/\n'

            'ЧМ-2018. Швеция защитила титул, Россия впервые за 5 лет без медалей\n'     
'http://articles-worldcup/193778-chm-2018-shvetsiya-zashchitila-titul-rossiya-vpervye-za-5-let-bez-medalej/\n'

            'ЧМ-2018. Канада в шикарном матче отправила Россию домой\n'     
'http://articles-worldcup/193594-chm-2018-kanada-v-shikarnom-matche-otpravila-rossiyu-domoj/\n'

            'ЧМ-2018. Россия в четвертьфинале вышла на Канаду\n'        
'http://articles-worldcup/193495-chm-2018-rossiya-v-chetvertfinale-vyshla-na-kanadu\n'

            'ЧМ-2018. Россия вернула Словакии должок за Пхенчхан\n'     
'http://articles-worldcup/193432-chm-2018-rossiya-vernula-slovakii-dolzhok-za-pkhenchkhan\n'

            'ЧМ-2018. Сборная России одержала четвертую победу на турнире\n'        
'http://articles-worldcup/193351-chm-2018-sbornaya-rossii-oderzhala-chetvertuyu-pobedu-na-turnire\n'

            'ЧМ-2018. Чехия поставила Россию на место\n'        
'http://articles-worldcup/193237-chm-2018-chekhiya-postavila-rossiyu-na-mesto\n'

            'ЧМ-2018. Россия продолжает громить аутсайдеров\n'      
'http://articles-worldcup/193078-chm-2018-rossiya-prodolzhaet-gromit-autsajderov\n'

            'ЧМ-2018. Россия снова забросила 7 шайб, на очереди - Беларусь\n'       
'http://articles-worldcup/193011-chm-2018-rossiya-snova-zabrosila-7-shajb-na-ocheredi-belarus\n'

            'ЧМ-2018. Россия размялась на французах\n'      
'http://articles-worldcup/192914-chm-2018-rossiya-razmyalas-na-frantsuzakh\n'

            'ЧМ по хоккею 2018: расписание, состав сборной России. Все, что нужно знать турнире\n'      
'http://articles-worldcup/192692-chm-po-khokkeyu-2018-raspisanie-sostav-sbornoj-rossii-vse-chto-nuzhno-znat-turnire\n'

            'Возвращение короля. "Ак Барс" победил ЦСКА в финале Кубка Гагарина\n'      
'http://articles-khl/192291-vozvrashchenie-korolya-ak-bars-pobedil-tsska-v-finale-kubka-gagarina\n'

            '"Ак Барс" не дал шансов "Трактору", ЦСКА спасли теневые герои\n'       
'http://articles-khl/191678-ak-bars-ne-dal-shansov-traktoru-tsska-spasli-tenevye-geroi\n'

            'Непризнанные звезды НХЛ 2017-18\n'     
'http://articles-nhl/191650-nepriznannye-zvezdy-nkhl-2017-18\n'

            'Награды NHL: кто все-таки станет MVP?\n'       
'http://articles-nhl/191576-nagrady-nhl-kto-vse-taki-stanet-mvp\n'

            'Я прагматик, но я верю в легенды. Итоги восточных полуфиналов КХЛ\n'       
'http://articles-khl/191125-ya-pragmatik-no-ya-veryu-v-legendy-itogi-vostochnykh-polufinalov-kkhl\n')

if __name__ == '__main__':
    print('Starting sportbot_bot')
    bot.polling()
