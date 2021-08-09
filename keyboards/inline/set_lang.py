from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_markup = InlineKeyboardMarkup(row_width=3)
lang1 = InlineKeyboardButton('🇺🇿 UZ', callback_data='uz')
lang2 = InlineKeyboardButton('🇷🇺 RU', callback_data='ru')
lang3 = InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 EN', callback_data='en')
inline_markup.add(lang1, lang2, lang3)