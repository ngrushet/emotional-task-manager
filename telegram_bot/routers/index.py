from aiogram import Router
from aiogram.types import Message

from telegram_bot.routers.manager_router import manager_router
from telegram_bot.routers.worker_router import worker_router

index_router = Router(name=__name__)

# нужно навесить middleware с запросом в API на тему того, 
# есть ли у чела нужная роль в команде 
# Навесить на сообщения и на callbacks 
# и на оба роутера
index_router.include_router(worker_router)
index_router.include_router(manager_router)

@index_router.message()
async def message_handler(message: Message):
    await message.answer('Hello from my index router!')