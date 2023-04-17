from aiogram import executor
from config.logging import *
from config.bot_config import dp, bot
from handlers.start.start import *
from handlers.start.amount_request import *
from handlers.admin_panel.admin import *
from handlers.admin_panel.users_list import *
from handlers.admin_panel.log_list import *


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=False)
