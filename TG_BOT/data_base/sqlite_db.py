import sqlite3 as sq
from aiogram import types
from aiogram import Bot
TOKEN = "5394717777:AAE22w9qhC-a8dW7COJdWxlGLJDyYnRGJhE"
bot = Bot(token=TOKEN)

def sql_start():
    global base, cur
    base = sq.connect('pizza_drakon.db')
    cur = base.cursor()
    if base:
        print("Подключение к базе данных выполнено")
    base.execute("CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)")
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO menu VALUES (?, ?, ?, ?)", tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f"{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}")