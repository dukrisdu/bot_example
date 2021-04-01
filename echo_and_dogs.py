# 27/04/2020
# Bot for telegram.
# A simpe program that will access the API, gets the image URL
# and then sends the image.

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

# Function that gets the URL. 
# Using the requests library, it access the API and get the json data
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']
    return image_url

# To send a message or an image we need:
# 1. The image URL or message
# 2. The recipient's ID (group's or user's)

def bop(bot, update):
    # Getting the image URL by calling a function
    url = get_url()

    # Get the recipient's ID
    chat_id = update.message.chat_id

    # Send an image 
    bot.send_photo(chat_id = chat_id, photo = url)


def main():
    updater = Updater('ENTER YOUR API HERE', use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
