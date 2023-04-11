import telebot
from telebot import types

api_token = '5990596269:AAHYTufiFOvYpiBLeLyOacl0RwAm-a3yR9U'  ##'6216981541:AAF32frwWYsvuDZdcvsAZtTOQorpt4I_5jI'
my_id = 690413583 ##535286796
## 690413583 - Димин
bot = telebot.TeleBot(api_token)
a = ['null']


def get_hashtag(message):
    if message.text == 'Trading':
        a[0] = 'Trading'
    elif message.text == 'Consulting':
        a[0] = 'Consulting'
    else:
        a[0] = 'ErrorType'


def get_info_user(bot, message):  # функция для отправки информации о юзере в личку
    ##get_hashtag(message, a)
    bot.send_message(my_id, '#' + a[0] + '\n' + message.text + '\n' + '\n'
                     +'ID: ' + f'{message.chat.id}')

    
markup2 = types.ReplyKeyboardMarkup(True)
markup2.row('Trading', 'Consulting')
markup2.row('О нас')
markupBack = types.ReplyKeyboardMarkup(True)
markupBack.row('Back')


@bot.message_handler(commands=['start'])
def start_message(message):
    ##bot.send_message(message.chat.id, "Приветствую! Какую услугу хотите получить?️")

    bot.send_message(message.chat.id, "Пожалуйста, выберите интересующий Вас раздел:", reply_markup=markup2)

@bot.message_handler(func=lambda message: True)

def menu(message):
    ##if message.chat.id == 411205186: exit(menu)
    if message.text == "Trading":
        get_hashtag(message)
        bot.send_message(message.chat.id, "Отдел занимается оптовой продажей товаров по Вашему персональному заказу")
        bot.send_message(message.chat.id,
                         "Пожалуйста, заполните анкету по данному такому образцу: \nВаше ФИО \nДанные для связи (номер телефона или почтовый адрес)"
                         "\nИнтересующий Вас продукт и потенциальный объем партии", reply_markup=markupBack)

    elif message.text == "Consulting":
        get_hashtag(message)
        bot.send_message(message.chat.id, "Отдел занимается коучингом, ментерингом, консультированием, аналитикой "
                                          "рентабельности продукта или концепции, проектированием уникальных программ "
                                          "по созданию, реорганизации или модернизации бизнеса")
        bot.send_message(message.chat.id,
                         "Пожалуйста, заполните анкету по данному такому образцу: \nВаше ФИО \nДанные для связи (номер телефона или почтовый адрес)"
                         "\nПодробное описание услуги, в которой Вы нуждаетесь", reply_markup=markupBack)

    elif message.text == 'О нас':
        bot.send_message(message.chat.id, "💠_О нас_ \nКопания Ogroup — команда специалистов в сфере трейдинга и "
                                          "краудфандинга, специализирующаяся на комфорте клиентов и "
                                          "высококвалифицированной помощи в построении бизнеса. Помимо этого команда "
                                          "наших специалистов уже два года упрощает клиентам работу с оптовыми "
                                          "поставками по индивидуальным заказам. Сфера нашей работы невероятно "
                                          "обширна — от ландшафтного дизайнам общепита до поставок электроники и "
                                          "бумаги в офис. \nОснователь Ogroup — Огиенко Дмитрий Викторович, работает в "
                                          "сфере уже 4 года, так что прекрасно разбирается во многих тонкостях "
                                          "бизнеса и в том, как найти оптимальное решение для самых сложных кейсов.\n"
                                          "\n💠*Наша цель* состоит в том, чтобы каждая идея и индивидуальный запрос нашли того,"
                                          " кто поможет им реализоваться. \n"
                                          "\n💠_О наших отделах_: \n*Trading.* Опытная команда из этого отдела занимается"
                                          " оптовой продажей по индивидуальным заказам клиента, выбирая для этого самые выгодные для клиента пути."
                                          "\n*Consalting.* Специалисты из этого отдела помогут клиентам понять рентабельность"
                                          " продукта, а также консультируют анализируют этот продукт, чтобы понять его "
                                          "максимальную доходность и окупаемость. Помимо этого команда Ogroup продумает "
                                          "концепцию бизнеса, а после этого спроектирует уникальные программы для "
                                          "создания, реорганизации или модернизации вашего бизнеса.\n"
                                          "\n💠_Наши контакты_: \nCEO: Огиенко Дмитрий Викторович"
                                          "\n+7 (962) 255-10-01 (Telegram & WhatsApp)", reply_markup=markupBack, parse_mode="Markdown")
    elif message.text == "Back":
        bot.send_message(message.chat.id, "Пожалуйста, выберите интересующий Вас раздел:", reply_markup=markup2)

    else:
        bot.send_message(message.chat.id,
                         'Спасибо за Ваше обращение! Совсем скоро мы свяжемся с Вами для обсуждения подробностей',
                         reply_markup=markupBack)
        get_info_user(bot, message)
        ##start_message(message)


bot.polling(none_stop=True)
