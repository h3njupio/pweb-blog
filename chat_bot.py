from PWEB import settings
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os

my_token = settings.TELE_TOKEN
data_dir = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'data')

def get_message(bot, update):
    update.message.reply_text(update.message.text)


def help_command(bot, update):
    update.message.reply_text('What can i do help you?')


def get_photo(bot, update):
    photo_id = update.message.photo[-1].file_id
    photo_file = bot.getFile(photo_id)
    file_name = photo_file.file_path.split('/')[-1]
    file_path = os.path.join(data_dir, 'photo', file_name)
    photo_file.download(file_path)
    update.message.reply_text('photo saved')


def get_file(bot, update):
    file_id = update.message.document.file_id
    file_path = os.path.join(data_dir, 'file', update.message.document.file_name)
    bot.getFile(file_id).download(file_path)
    update.message.reply_text('file saved')


updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

help_handler = CommandHandler('help', help_command)
updater.dispatcher.add_handler(help_handler)

photo_handler = MessageHandler(Filters.photo, get_photo)
updater.dispatcher.add_handler(photo_handler)

file_handler = MessageHandler(Filters.document, get_file)
updater.dispatcher.add_handler(file_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()