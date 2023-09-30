from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

manager_router = Router(name=__name__)

@manager_router.message(Command("start"))
# Обработка команды /start
async def start_command(message: Message):
    # узнать статус пользователя по API
    # если это менеджер, то отправить меню для менеджера
    # иначе отправить меню для сотрудника

    # пока что будет меню для сотрудника
    await message.reply(
        text="Привет! Я телеграм-бот. Погнали нахуй",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(
                    text='Новая задача',
                    callback_data="create_task"
                ),
                InlineKeyboardButton(
                    text='Все задачи',
                    callback_data="show_tasks"
                )
            ]]
        )
    )



@manager_router.message()
async def message_handler(message: Message):
    await message.answer('Hello from my manager router!')