from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from data.config import BOT_TOKEN

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=storage) 