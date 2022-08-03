from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("/Режим_работы")
b2 = KeyboardButton("/Сумма_заказа")
b3 = KeyboardButton("/О_нас")
b4 = KeyboardButton("Поделиться номером", request_contact=True)
b5 = KeyboardButton("Отправить,где я", request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1,b2,b3).add(b4).add(b5)
