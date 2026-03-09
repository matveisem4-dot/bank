import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Токен берется из секретов репозитория
API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Использованы сервера с самым низким пингом на март 2026
LINKS = {
    "android": "https://t.me/proxy?server=95.216.155.155&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d",
    "ios": "https://t.me/proxy?server=proxy.digitalfortress.it&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d",
    "windows": "https://t.me/proxy?server=162.19.163.43&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d"
}

@dp.message(F.text == "/start")
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🤖 ANDROID (TURBO)", callback_data="os:android")],
        [InlineKeyboardButton(text="🍎 iOS / iPHONE", callback_data="os:ios")],
        [InlineKeyboardButton(text="💻 WINDOWS PC", callback_data="os:windows")],
        [InlineKeyboardButton(text="🔄 СБРОСИТЬ СОЕДИНЕНИЕ", url="https://t.me/proxy?server=disable")]
    ])
    await message.answer(
        "💎 **ALISA VPN V61: СКОРОСТНАЯ СЕТЬ**\n\n"
        "Если Telegram тормозит, нажми 'СБРОСИТЬ'.\n"
        "Затем выбери свою систему для активации:",
        reply_markup=kb,
        parse_mode="Markdown"
    )

@dp.callback_query(F.data.startswith("os:"))
async def connect(callback: types.CallbackQuery):
    os_type = callback.data.split(":")[1]
    res_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🟢 ВКЛЮЧИТЬ (БЕСПЛАТНО)", url=LINKS[os_type])]
    ])
    await callback.message.edit_text(
        f"✅ **КАНАЛ ДЛЯ {os_type.upper()} ПОДГОТОВЛЕН**\n"
        "Статус: **Premium High-Speed**\n\n"
        "Нажми кнопку ниже:",
        reply_markup=res_kb,
        parse_mode="Markdown"
    )

async def main():
    # Очистка очереди (удаляет все зависшие 'крутилки')
    await bot.delete_webhook(drop_pending_updates=True)
    print(">>> БОТ ЗАПУЩЕН")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
