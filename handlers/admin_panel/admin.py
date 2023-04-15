from aiogram import types
from config.bot_config import dp, bot, ADMIN


@dp.message_handler(commands=['admin'])
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
			'Вы не являетесь админом Бота('.format(
				username=message.from_user.username
			)
		)
