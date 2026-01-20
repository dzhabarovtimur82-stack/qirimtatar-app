from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from db import add_user

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    add_user(message.from_user.id, message.from_user.username)

    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🌟 Начать урок",
                    web_app=WebAppInfo(url="https://dzhabarovtimur82.github.io/qirimtatar-app/")
                )
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Добро пожаловать! Нажми кнопку ниже:", reply_markup=kb)
