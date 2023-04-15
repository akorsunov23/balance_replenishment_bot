from aiogram import types
from config.bot_config import dp, bot, ADMIN
from keyboards.user_replenish_balance import replenish_balance


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
	user_id = message.from_user.id

	if user_id == ADMIN:
		await bot.send_message(
			chat_id=message.from_user.id,
			text='Привет АДМИН'
		)

	else:
		await bot.send_message(
			chat_id=message.from_user.id,
			text='Привет, {username}!\n'
			'Я - бот для пополнения баланса.\n'
			'Нажмите на кнопку, чтобы пополнить баланс.'.format(
				username=message.from_user.username
			),
			reply_markup=replenish_balance
		)
