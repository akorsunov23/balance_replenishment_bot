import handlers
from aiogram import executor
from config.logging import *
from config.bot_config import dp, bot
from handlers.admin_panel.log_list import *


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=False)
