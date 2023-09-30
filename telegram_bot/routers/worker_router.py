from aiogram import Router
from aiogram.types import Message

worker_router = Router(name=__name__)

@worker_router.message()
async def message_handler(message: Message):
    await message.answer('Hello from my worker router!')