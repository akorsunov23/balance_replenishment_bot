from config.bot_config import dp, bot
from aiogram import types


@dp.callback_query_handler(text='replenish_balance')
async def amount_request(callback_query: types.CallbackQuery):
	await bot.send_message(
		chat_id=callback_query.from_user.id,
		text='Введите сумму, на которую вы хотите пополнить баланс:'
	)
