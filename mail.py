from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_comands import *



app = ApplicationBuilder().token("5886727935:AAGB2_2T2MwEgYpXqQJoDDJe8knIbTEaASU").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("play", play_command))
print('START SERVER')
app.run_polling()
print('END SERVER')