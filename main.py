#28/04/2020
#3rd attempt to create a bot for Telegram

# Functionality:
# 1. Sends a message once there is an input /start  DONE
# 2. /woof - sends an image of a dog                DONE
# 3. /meow - sends an image of a cat                DONE
# 4. /chirp - sends an image of a bird              DONE

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import requests
import re
import random
import os

# The Updater class continuously fetches mew updates
# from telegram and passes them on to the Dispatcher class.
# Created Updater object will create Dispatcher object
# and link them together with a Queue.

# Creating an Updater object
updater = Updater(token='1289242052:AAHYzJiJUL6WQ9HgHACHLm2YgeTlyAyVxGM', use_context = True)

# Introducing locally Dispatcher used by my Updater. 
# Doing so for quicker access to the Dispatcher. 
dispatcher = updater.dispatcher

# Setting up the logging module in order to know
# when and why things don't work
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Exception-Handling
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    level=logging.INFO)

def get_url_woof():
    """Getting an URL of an image of a dog"""
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        contents = requests.get('https://random.dog/woof.json').json()
        url = contents['url']
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def get_url_meow():
    """Getting an URL of an image of a cat"""
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        contents = requests.get('https://api.thecatapi.com/v1/images/search').json()
        tmp = str(contents) # Turning input to a string
        tmp = tmp.split(", ") # Spliting string by a comma 
        url = tmp[2] # 3rd slice is an URL, but it still has extra information

        # Removing extra information, leaving URL only
        url = url.replace('\'url\': \'', '')
        url = url.replace('\'', '')

        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def get_chirp():
    """Getting a path of a random image from a local directory"""
    directory = "/home/kris/Documents/telegram_bots/birds/"
    random_image = random.choice(os.listdir(directory))
    url = directory + random_image
    return url


def start(update, context):
    """Writes a message to a recipient after command /start is written"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def woof(update, context):
    """Sends a cute image of a dog to a recipient when /woof is written"""
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=get_url_woof())

def meow(update, context):
    """Sends a cute image of a cat to a recipient when /meow is written"""
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=get_url_meow())

def chirp(update, context):
    """Sends a cute image of a bird to a recipient when /chirp is written"""
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(get_chirp(), 'rb'))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

woof_handler = CommandHandler('woof', woof)
dispatcher.add_handler(woof_handler)

meow_handler = CommandHandler('meow', meow)
dispatcher.add_handler(meow_handler)

chirp_handler = CommandHandler('chirp', chirp)
dispatcher.add_handler(chirp_handler)

# Starts polling - aka when there is an input that is defined in the program
# it will send an appropriate message or image to a recipient.
updater.start_polling()
