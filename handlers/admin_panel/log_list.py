import os.path

from aiogram.dispatcher import FSMContext
from aiogram import types
from config.bot_config import dp
from config.database import User
from utils.state import StateAdmin
from keyboards.admin_panel import log


@dp.callback_query_handler(text='log_list')
async def logs(callback_query: types.CallbackQuery):
	await callback_query.message.answer(text='Какие логи показать:', reply_markup=log())


@dp.callback_query_handler()
async def get_error_log(callback_query: types.CallbackQuery):
	text = str()
	file = str()
	if callback_query.data == 'error_log':
		file = 'error'
	else:
		file = 'info'

	current_path = os.getcwd()
	parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
	file_path = os.path.join(parent_path, f'balance_replenishment_bot/{file}.log')

	if os.path.isfile(file_path):
		with open(file_path, 'r') as file:
			text = ''.join((file.read().split('\n'))[-4:])

	else:
		text = 'Логов пока нет!'

	await callback_query.message.answer(text=f'... {text}')
