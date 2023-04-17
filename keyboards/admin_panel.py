from aiogram import types
from config.database import User


def admin_panel() -> types.InlineKeyboardMarkup():
	result = types.InlineKeyboardMarkup()
	bottom_1 = types.InlineKeyboardButton('Список пользователей', callback_data='users_list')
	bottom_2 = types.InlineKeyboardButton('Выгрузка логов', callback_data='log_list')
	result.row(bottom_1, bottom_2)

	return result


def users_list() -> types.InlineKeyboardMarkup():
	keyboard = types.InlineKeyboardMarkup()
	users = User.select().where(User.is_active == True)
	for user in users:
		keyboard.add(types.InlineKeyboardButton(
			text=f'{user.full_name}, баланс: {user.balance} руб.',
			callback_data=user.user_id)
		)
	return keyboard


def action_for_user() -> types.InlineKeyboardMarkup():
	result = types.InlineKeyboardMarkup()

	update_balance = types.InlineKeyboardButton(text='Изменить баланс', callback_data='update_balance')
	block_user = types.InlineKeyboardButton(text='Заблокировать пользователя', callback_data='block_user')
	result.row(update_balance, block_user)

	return result


def log() -> types.InlineKeyboardMarkup():
	result = types.InlineKeyboardMarkup()

	error_log = types.InlineKeyboardButton(text='Ошибки и предупреждения', callback_data='error_log')
	info_log = types.InlineKeyboardButton(text='Информационные', callback_data='info_log')

	result.row(error_log, info_log)

	return result
