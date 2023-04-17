from aiogram.dispatcher import FSMContext
from aiogram import types
from config.bot_config import dp
from config.database import User
from utils.state import StateAdmin
from keyboards.admin_panel import users_list, action_for_user


@dp.callback_query_handler(text='users_list')
async def users(callback_query: types.CallbackQuery, state: FSMContext):
	await callback_query.message.answer(text='Список пользователей:', reply_markup=users_list())
	await state.set_state(StateAdmin.get_list)


@dp.callback_query_handler(state=StateAdmin.get_list)
async def user_detail(callback_query: types.CallbackQuery, state: FSMContext):
	user = User.get(User.user_id == callback_query.data)

	await callback_query.message.answer(
		text=f'{user.full_name}, баланс: {user.balance} руб.',
		reply_markup=action_for_user()
	)
	await state.set_state(StateAdmin.get_user)
	async with state.proxy() as data:
		data['user'] = user


@dp.callback_query_handler(text='block_user', state=StateAdmin.get_user)
async def block_user(callback_query: types.CallbackQuery,  state: FSMContext):

	async with state.proxy() as data:
		user = data['user']

	user.is_active = False
	user.save()

	await callback_query.message.answer(text=f'Пользователь "{user.full_name}" заблокирован')
	await state.finish()


@dp.callback_query_handler(text='update_balance', state=StateAdmin.get_user)
async def update_balance_user(callback_query: types.CallbackQuery,  state: FSMContext):
	await callback_query.message.answer(text='Введите новый баланс для пользователя:')
	await state.set_state(StateAdmin.update_user)


@dp.message_handler(state=StateAdmin.update_user)
async def update_balance_user(message: types.Message,  state: FSMContext):

	if message.text.isdigit():
		async with state.proxy() as data:
			user = data['user']

		user.balance = message.text
		user.save()
		await message.answer(text=f'Баланс для пользователя {user.full_name} изменён.')
		await state.finish()
	else:
		await message.answer(text=f'Сумма только цифрами!')
