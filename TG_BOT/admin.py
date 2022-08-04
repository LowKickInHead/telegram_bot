from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from client_kb import button_case_admin
from data_base import sqlite_db

admin_id = 293427068


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# Проверка на права админа
# @dp.message_handler(commands=['admin'], user_id=int(admin_id))


# Начало диалога загрузки нового пункта меню
# @dp.message_handler(commands="Загрузить", state=None)
async def make_changes_command(message: types.Message):
    if message.from_user.id == admin_id:
        await message.answer("Что хозяин надо ???", reply_markup=button_case_admin)
        await message.delete()


async def cm_start(message: types.Message):
    if message.from_user.id == admin_id:
        await message.answer("Используйте меню для загрузки и удаления товаров")
        await FSMAdmin.photo.set()
        await message.reply("Загрузи фото")


# Ловим первый ответ и пишем в словарь
# @dp.message_handler(content_types=["photo"], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.from_user.id == admin_id:
            data["photo"] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Теперь введи название")


# @dp.message_handler(state="*", commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if message.from_user.id == admin_id:
        if current_state is None:
            return
        await state.finish()
        await message.reply("ОК")


# Ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.from_user.id == admin_id:
            data["name"] = message.text
            await FSMAdmin.next()
            await message.reply("Введи описание")


# Ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.from_user.id == admin_id:
            data["descriotion"] = message.text
        await FSMAdmin.next()
        await message.reply("Введи цену")


# Ловим чертвертый ответ
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == admin_id:
        async with state.proxy() as data:
            data["price"] = float(message.text)
        await message.answer("Успешно")

        await sqlite_db.sql_add_command(state)
        await state.finish()


# Регистрация хендлеров
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=["Загрузить"], state=None)
    dp.register_message_handler(load_photo, content_types=["photo"], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(make_changes_command, commands=['moderator'], state=None)
