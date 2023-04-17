from aiogram import types
from config.bot_config import dp, ADMIN
from keyboards.user_replenish_balance import replenish_balance


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
	user_id = message.from_user.id

	if user_id == ADMIN:
		await message.answer('Привет АДМИН')

	else:
		await message.answer(
			'Привет, {username}!\n'
			'Я - бот для пополнения баланса.\n'
			'Нажмите на кнопку, чтобы пополнить баланс.'.format(
				username=message.from_user.full_name
			),
			reply_markup=replenish_balance
		)
