import info
from aiogram import types
import client_kb
from client_kb import kb_client


async def command_start(message: types.Message):
    await message.answer("Вас приветствует бот компании 'Три Дракона'")
    await message.answer("С моей помощью вы сможете оформить заказ")
    await message.answer("Приятного аппетита!")
    await message.answer("Для просмотра доступных функций используйте меню выбора команд", reply_markup=kb_client)
    await message.answer("Для возврата в начальное меню введите /help")


async def command_help(message: types.Message):
    await message.answer("Используйте меню для навигации", reply_markup=kb_client)




async def command_open_time(message: types.Message):
    await message.answer("""Время работы с 11:00 до 24:00 ежедневно, без выходных.\n
    По г.Пересвет заказы принимаются до 23:45, а в остальные районы заказы принимаются до 23:30.""")


async def command_summa_zakaza(message: types.Message):
    await message.answer(info.summa_zakaza)


async def command_o_nas(message: types.Message):
    await message.answer(info.o_nas)
