import time

import admin

import handlers as h
from aiogram import Bot
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from data_base import sqlite_db


storage = MemoryStorage()

TOKEN = "5394717777:AAE22w9qhC-a8dW7COJdWxlGLJDyYnRGJhE"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
admin.register_handlers_admin(dp)


async def on_startup(_):
    print("Идёт подключение к серверу...")

    print("Бот вышел в онлайн.")

    print("Готов к работе!")
    sqlite_db.sql_start()


dp.register_message_handler(h.command_start, commands=["start"])
dp.register_message_handler(h.command_help, commands=["help"])
dp.register_message_handler(h.command_open_time, commands=["Режим_работы"])
dp.register_message_handler(h.command_summa_zakaza, commands=["Сумма_заказа"])
dp.register_message_handler(h.command_o_nas, commands=["О_нас"])
dp.register_message_handler(h.menu, commands=["Меню"])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
