import telebot
from telebot import types

api_token = '6216981541:AAF32frwWYsvuDZdcvsAZtTOQorpt4I_5jI'
my_id = 535286796
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
    bot.send_message(my_id, '#' + a[0] + '\n' + message.text + '\n'
                     ##+ f'{message.chat.id}' + ''
                     + f'{message.from_user.first_name}' + ' '
                     + f'{message.from_user.last_name}')


markup2 = types.ReplyKeyboardMarkup(True)
markup2.row('Trading', 'Consulting')
markupBack = types.ReplyKeyboardMarkup(True)
markupBack.row('Back')


@bot.message_handler(commands=['start'])
def start_message(message):
    ##bot.send_message(message.chat.id, "Приветствую! Какую услугу хотите получить?️")

    bot.send_message(message.chat.id, "Пожалуйста, выберите интересующий Вас отдел:", reply_markup=markup2)


@bot.message_handler(func=lambda message: True)
def menu(message):
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

    elif message.text == "Back":
        bot.send_message(message.chat.id, "Пожалуйста, выберите интересующий Вас отдел:", reply_markup=markup2)

    else:
        bot.send_message(message.chat.id, 'Спасибо за Ваше обращение! Совсем скоро мы свяжемся с Вами для обсуждения подробностей',
                         reply_markup=markupBack)
        get_info_user(bot, message)
        ##start_message(message)


bot.polling(none_stop=True)
