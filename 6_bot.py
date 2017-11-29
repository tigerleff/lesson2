# Установите модуль ephem
# Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском.
# При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import datetime
import ephem

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

#print(datetime.datetime.now())


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def planet_ephem(bot, update, args):
    date = datetime.datetime.now().strftime('%Y/%m/%d')

    if args[0] == 'Jupiter':
        planet_constellation = ephem.constellation(ephem.Jupiter(date))   #/planet Jupiter
    elif args[0] == 'Mars':
        planet_constellation = ephem.constellation(ephem.Mars(date))      #/planet Mars
    elif args[0] == 'Mercury':
        planet_constellation = ephem.constellation(ephem.Mercury(date))   #/planet Mercury
    elif args[0] == 'Moon':
        planet_constellation = ephem.constellation(ephem.Moon(date))      #/planet Moon
    elif args[0] == 'Neptune':
        planet_constellation = ephem.constellation(ephem.Neptune(date))   #/planet Neptune
    elif args[0] == 'Pluto':
        planet_constellation = ephem.constellation(ephem.Pluto(date))     #/planet Pluto
    elif args[0] == 'Saturn':
        planet_constellation = ephem.constellation(ephem.Saturn(date))    #/planet Saturn
    elif args[0] == 'Sun':
        planet_constellation = ephem.constellation(ephem.Sun(date))       #/planet Sun
    elif args[0] == 'Uranus':
        planet_constellation = ephem.constellation(ephem.Uranus(date))    #/planet Uranus
    elif args[0] == 'Venus':
        planet_constellation = ephem.constellation(ephem.Venus(date))     #/planet Venus
    
    text = planet_constellation

    update.message.reply_text(" Планета {0} находится в созвездии {1} на дату {2}".format(args[0], text[1], date ))


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    updater = Updater("453680228:AAHKfirSvEenS5paUgKAMtGsn1wfNNlkRuk")

    dp = updater.dispatcher
    #dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(CommandHandler("planet", planet_ephem, ))
    dp.add_handler(CommandHandler("planet", planet_ephem, pass_args = True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()

main()