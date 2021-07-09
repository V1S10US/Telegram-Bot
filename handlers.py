from aio_bot import  bot, dispatcher

from aiogram.types import Message
from config import admin_id

async def send_to_admin(dp):
    await bot.send_message(admin_id, text='<b>Here we go again...</b>')


@dispatcher.message_handler()
async def echo(message: Message):
    text = f"Reversed message: {message.text[::-1]}"
    #await bot.send_message(chat_id=message.from_user.id,     # old version
    #                       text=text)
    await message.answer(text)