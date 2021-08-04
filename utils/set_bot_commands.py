from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "♻️ Botni ishga tushurish"),
            types.BotCommand('search', '🔎 Suhbatdosh qidirish'),
            types.BotCommand('next', '🆕 Yangi suhbatdosh'),
            types.BotCommand('stop', '❌ Suhbatni to\'xtatish'),
            types.BotCommand('send_account', '🔗 Profilni jo\'natish'),
            types.BotCommand("help", "📋 Yordam"),
        ]
    )
