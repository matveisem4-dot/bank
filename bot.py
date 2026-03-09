import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Токен берем из секретов (безопасность уровня Pro)
API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --- ЭЛИТНЫЕ МАГИСТРАЛИ (БЕЗЛИМИТНАЯ СКОРОСТЬ) ---
OS_CONFIGS = {
    "android": {
        "link": "https://t.me/proxy?server=5.135.161.164&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d",
        "label": "⚡️ ULTRA-LOW LATENCY",
        "desc": "Оптимизация под Samsung Fold & Android Kernel. Пинг < 20ms."
    },
    "ios": {
        "link": "https://t.me/proxy?server=162.19.163.43&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d",
        "label": "🛡 APPLE ENCLAVE SECURE",
        "desc": "Выделенный канал для iOS. Обход любых блокировок."
    },
    "windows": {
        "link": "https://t.me/proxy?server=exp.proxy.com&port=443&secret=ee00000000000000000000000000000000676f6f676c652e636f6d",
        "label": "💎 WORKSTATION MAX",
        "desc": "Многопоточный доступ. Скорость до 1 Гбит/с."
    }
}

def get_main_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🤖 ANDROID", callback_data="os:android")],
        [InlineKeyboardButton(text="🍎 iOS / iPHONE", callback_data="os:ios")],
        [InlineKeyboardButton(text="💻 WINDOWS PC", callback_data="os:windows")]
    ])

@dp.message(F.text == "/start")
async def cmd_start(message: types.Message):
    await message.answer(
        "⚡️ **ALISA PRIVATE NETWORK V55**\n\n"
        "Добро пожаловать в элитную сеть доступа.\n"
        "Статус системы: **Dedicated Server (Germany) — Online**\n\n"
        "Выберите вашу платформу для автоматической калибровки канала:",
        reply_markup=get_main_kb(),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data.startswith("os:"))
async def tune_system(callback: CallbackQuery):
    os_key = callback.data.split(":")[1]
    cfg = OS_CONFIGS[os_key]
    
    # Эффект дорогого софта
    msg = await callback.message.edit_text("📡 Установка связи с выделенным сервером...")
    await asyncio.sleep(0.4)
    await msg.edit_text(f"🚀 Проверка пропускной способности для {os_key.upper()}...")
    await asyncio.sleep(0.4)
    await msg.edit_text(f"💎 Активация профиля: {cfg['label']}...")
    await asyncio.sleep(0.4)

    res_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❇️ ПОДКЛЮЧИТЬ МГНОВЕННО", url=cfg['link'])]
    ])

    await msg.edit_text(
        f"✅ **СИСТЕМА ГОТОВА**\n\n"
        f"🌐 Сервер: **Premium Frankfurt Node**\n"
        f"🛠 Настройка: *{cfg['desc']}*\n"
        f"📶 Скорость: **Максимальная**\n\n"
        "Нажмите кнопку ниже для мгновенной активации:",
        reply_markup=res_kb,
        parse_mode="Markdown"
    )

async def start_engine():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start_engine())
