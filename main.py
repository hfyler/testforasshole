import aiogram
import logging
import sys
import asyncio
from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import F
import random
from token1 import token

bot = Bot(token=token)
dp = Dispatcher()
router = Router()

async def main():
    await dp.start_polling(bot, spisochek=[])


@dp.message(Command('тест'))
async def sam_test(message: Message):
    await message.answer('Введите имена потенциальных пидоров через запятую: ')
    @dp.message(F.text)
    async def testing_blyat(message: Message):
        spisochek = message.text.split(', ')
        pidor = random.choice(spisochek)
        await message.answer("Пидор сегодняшнего дня...")
        await message.answer(pidor)
        await message.answer("Поздравляем!!!")
        await message.answer("Спасибо. А на сегодня всё")
        await message.answer("Пока!")
        await sys.exit()


if __name__ == "__main__":
    asyncio.run(main())