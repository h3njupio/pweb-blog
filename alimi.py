from PWEB import settings
import telegram

my_token = settings.TELE_TOKEN
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()

for u in updates:
    print(u.message)

chat_id = bot.getUpdates()[-1].message.chat.id
id_channel = '-1001257363188'

bot.send_message(chat_id=id_channel, text='hahaha')
