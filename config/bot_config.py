import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

BOT_KEY = os.getenv('BOT_API_KEY')
ADMIN = int(os.getenv('ADMIN_ID'))

bot = Bot(token=BOT_KEY)
dp = Dispatcher(bot)
