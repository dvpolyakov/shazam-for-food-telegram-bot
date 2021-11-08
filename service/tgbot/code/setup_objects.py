from aiogram import Bot, Dispatcher

from service.tgbot.code.bot_token import API_TOKEN

# from service.tgbot.code.database_setup import DBConnection
# from aiogram.contrib.fsm_storage.memory import MemoryStorage

# db_connection = DBConnection()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
