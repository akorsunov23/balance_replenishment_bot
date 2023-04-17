import os
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from aiogram import types
from dotenv import load_dotenv
from config.bot_config import dp, bot
from config.database import User
from utils.state import StateUser

load_dotenv()

PAYMENTS_TOKEN = os.getenv('PAYMENTS_TOKEN')


@dp.callback_query_handler(text='replenish_balance')
async def amount_request(callback_query: types.CallbackQuery, state: FSMContext):
	"""Хандлер, реагирующий на кнопку /пополнить баланс/, и запрашивающий желаемую сумму пополнения."""

	await callback_query.message.answer('Введите сумму, на которую вы хотите пополнить баланс:')
	await state.set_state(StateUser.entered_amounts)


@dp.message_handler(state=StateUser.entered_amounts)
async def payment_processing(message: types.Message, state: FSMContext):
	"""Генерация платёжки PayMaster"""

	if message.text.isdigit() and PAYMENTS_TOKEN.split(':')[1] == 'TEST':
		price = types.LabeledPrice(label='Желаемая сумма пополнения', amount=int(message.text) * 100)
		await bot.send_invoice(
				message.chat.id,
				title='Пополнение баланса',
				description='Тестовое пополнение баланса',
				provider_token=PAYMENTS_TOKEN,
				currency='rub',
				prices=[price],
				is_flexible=False,
				payload='test-invoice-payload'
		)
		await state.set_state(StateUser.payment_processing)
	else:
		await message.answer('Суммой для пополнения баланса должны быть только цифры!')


@dp.pre_checkout_query_handler(lambda query: True, state=StateUser.payment_processing)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery, state: FSMContext):
	"""Обработка и утверждение платежа."""

	await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
	await state.set_state(StateUser.replenishment_passed)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT, state=StateUser.replenishment_passed)
async def successful_payment(message: types.Message, state: FSMContext):
	"""Проверка платежа, при успешном выполнении добавляет данные в БД и выводит соответствующие сообщение."""

	price = message.successful_payment.total_amount // 100
	currency = message.successful_payment.currency

	query = User.select().where(User.user_id == message.from_user.id)

	if query.exists():
		update = User.get(User.user_id == message.from_user.id)
		update.balance += price
		update.save()
	else:
		new_entry = User(
			user_id=message.from_user.id,
			username=message.from_user.username,
			full_name=message.from_user.full_name,
			balance=price)
		new_entry.save()

	await bot.send_message(message.chat.id, f"Пополнение на сумму {price}{currency} прошло успешно!!!")
	await state.finish()
