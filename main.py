from aiogram import executor
from config.bot_config import dp, bot
from handlers.start.start import *
from handlers.start.amount_request import *
from handlers.admin_panel.admin import *


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=False)
