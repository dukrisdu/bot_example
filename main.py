from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(bot, update):
    print ("Got bop")
    #url = get_image_url()
    #chat_id = update.message.chat_id
    #print (chat_id)
    update.message.reply_text("I'm sorry Dave I'm afraid I can't do that.")
    print ("done")
    bot.send_message(bot, update.message.chat_id,"I got your message <(")
    #bot.send_photo(chat_id=chat_id, photo=url)
    print ("done")

def echo(update, context):
    url = get_image_url()
    context.bot.send_message(chat_id=update.effective_chat.id, text="bop")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

def main():
    updater = Updater('1289242052:AAHYzJiJUL6WQ9HgHACHLm2YgeTlyAyVxGM', use_context = True)
    dp = updater.dispatcher
    #dp.add_handler(CommandHandler('bop',bop))
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dp.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()