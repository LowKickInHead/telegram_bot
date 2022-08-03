import time

import handlers as h
from aiogram import Bot
from aiogram import executor
from aiogram.dispatcher import Dispatcher

TOKEN = "5320843943:AAGc_40shVPFQeYN5s5YTb8cm19HVJ8qzxQ"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Идёт подключение к серверу...")
    time.sleep(2)
    print("Бот вышел в онлайн.")
    time.sleep(2)
    print("Готов к работе!")


dp.register_message_handler(h.command_start, commands=["start"])
dp.register_message_handler(h.command_help, commands=["help"])
dp.register_message_handler(h.command_open_time, commands=["Режим_работы"])
dp.register_message_handler(h.command_summa_zakaza, commands=["Сумма_заказа"])
dp.register_message_handler(h.command_o_nas, commands=["О_нас"])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
