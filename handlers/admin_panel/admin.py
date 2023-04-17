from aiogram import types
from config.database import User
from config.bot_config import dp, ADMIN
from keyboards.admin_panel import admin_panel


@dp.message_handler(commands=['admin'])
async def start_command(message: types.Message):
	"""Хандлер, реагирующий на команду /admin, и при проверке соответствия открывается панель управления."""

	user_id = message.from_user.id

	if user_id == ADMIN:
		await message.answer('Привет АДМИН!', reply_markup=admin_panel())

	else:
		query = User.select().where(User.user_id == message.from_user.id)
		user = User.get(User.user_id == message.from_user.id)
		if not query.exists() or user.is_active:
			await message.answer(
				'Привет, {username}!\n'
				'Вы не являетесь админом Бота('.format(
					username=message.from_user.full_name
				)
			)
