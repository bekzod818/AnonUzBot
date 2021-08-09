from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_markup = InlineKeyboardMarkup(row_width=1)
lang1 = InlineKeyboardButton('12 yosh - 18 yosh', callback_data='age1')
lang2 = InlineKeyboardButton('18 yosh - 24 yosh', callback_data='age2')
lang3 = InlineKeyboardButton('25 yosh - 30 yosh', callback_data='age3')
inline_markup.add(lang1, lang2, lang3)