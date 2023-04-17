import os.path
from aiogram import types
from aiogram.dispatcher import FSMContext
from config.bot_config import dp
from keyboards.admin_panel import log
from utils.state import StateAdmin


@dp.callback_query_handler(text='log_list')
async def logs(callback_query: types.CallbackQuery, state: FSMContext):
	await callback_query.message.answer(text='Какие логи показать:', reply_markup=log())
	await state.set_state(StateAdmin.get_log)


@dp.callback_query_handler(state=StateAdmin.get_log)
async def get_error_log(callback_query: types.CallbackQuery, state: FSMContext):
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
			text = '\n'.join((file.read().split('tab'))[-3:])

	else:
		text = 'Логов пока нет!'

	await callback_query.message.answer(text=f'...\n {text}')
	await state.finish()
