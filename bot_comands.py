from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from game import *


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split() # /sum  123  34534
    x = int(items[1])
    y = int(items[2])

    await update.message.reply_text(f'{x} + {y} = {x + y}')


async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = (update.message.text).split()


    await update.message.reply_text(int(msg[1]))
    await update.message.reply_text(player.player(msg))

