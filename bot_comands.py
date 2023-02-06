from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from datetime import datetime
from game import *
from geo import *
from nyDays import *



async def message_processing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text[0] !='/':
        await update.message.reply_text('Вы ввели пpocтo текст, не имеющий команды')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Вот что умеет данный бот: \n'
                                    f'/hi приветствие\n'
                                    f'/time показывает текущее время\n'
                                    f'/start показывает все команды\n/sum введите 2 числа через пробел для сложения\n'
                                    f'/geo показывает погоду в указанном городе\n'
                                    f'/newyear сколько осталось до нового года'
                                    )

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split() # /sum  123  34534
    x = int(items[1])
    y = int(items[2])

    await update.message.reply_text(f'{x} + {y} = {x + y}')



async def day2NewYear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{days2NY()}')



async def get_weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{get_weather()}')















