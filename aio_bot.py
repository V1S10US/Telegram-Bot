"""
This is a echo bot.
It echoes any incoming text messages.
"""

import config
from aiogram import Bot, Dispatcher, executor
import asyncio

loop = asyncio.get_event_loop()
bot = Bot(config.token, parse_mode='HTML')
dispatcher = Dispatcher(bot, loop)

if __name__ == '__main__' :

    from handlers import dispatcher, send_to_admin
    executor.start_polling(dispatcher, on_startup=send_to_admin)
