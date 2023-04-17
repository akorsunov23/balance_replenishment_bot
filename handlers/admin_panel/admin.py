from aiogram import types
from config.bot_config import dp, ADMIN
from keyboards.admin_panel import admin_panel


@dp.message_handler(commands=['admin'])
async def start_command(message: types.Message):
	user_id = message.from_user.id

	if user_id == ADMIN:
		await message.answer('Привет АДМИН!', reply_markup=admin_panel())

	else:
		await message.answer(
			'Привет, {username}!\n'
			'Вы не являетесь админом Бота('.format(
				username=message.from_user.full_name
			)
		)
