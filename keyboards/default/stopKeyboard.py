from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

stop = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="❌ Qidirishni to'xtatish"),
        ],
    ],
    resize_keyboard=True
)