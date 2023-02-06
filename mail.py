from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from bot_comands import *
from geo import *


open_weather_token = '4c5a015df3cc9900554218396f639c35'

app = ApplicationBuilder().token("5886727935:AAGB2_2T2MwEgYpXqQJoDDJe8knIbTEaASU").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("newyear", day2NewYear))
app.add_handler(CommandHandler("geo", get_weather_command))
app.add_handler(MessageHandler(None, message_processing))
print('START SERVER')
app.run_polling()
print('\nEND SERVER')