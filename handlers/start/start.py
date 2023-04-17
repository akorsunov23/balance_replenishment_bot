from aiogram import types
from config.bot_config import dp, ADMIN
from config.database import User
from keyboards.user_replenish_balance import replenish_balance


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
	user_id = message.from_user.id

	if user_id == ADMIN:
		await message.answer('Привет АДМИН')

	else:
		query = User.select().where(User.user_id == message.from_user.id)
		user = User.get(User.user_id == message.from_user.id)
		if not query.exists() or user.is_active:
			await message.answer(
				'Привет, {username}!\n'
				'Я - бот для пополнения баланса.\n'
				'Нажмите на кнопку, чтобы пополнить баланс.'.format(
					username=message.from_user.full_name
				),
				reply_markup=replenish_balance
			)
		# elif User.get(User.user_id == message.from_user.id).is_active:
		# 	await message.answer(
		# 		'Привет, {username}!\n'
		# 		'Я - бот для пополнения баланса.\n'
		# 		'Нажмите на кнопку, чтобы пополнить баланс.'.format(
		# 			username=message.from_user.full_name
		# 		),
		# 		reply_markup=replenish_balance
		# 	)
