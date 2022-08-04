from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("/Режим_работы")
b2 = KeyboardButton("/Сумма_заказа")
b3 = KeyboardButton("/О_нас")
b4 = KeyboardButton("Поделиться номером", request_contact=True)
b5 = KeyboardButton("Отправить,где я", request_location=True)
b6 = KeyboardButton("/Меню")
kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(b6).add(b1).add(b2, b3)



button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')
button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)
