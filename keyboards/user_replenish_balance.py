from aiogram import types

replenish_balance = types.InlineKeyboardMarkup()

bottom = types.InlineKeyboardButton('Пополнить баланс', callback_data='replenish_balance')

replenish_balance.row(bottom)
