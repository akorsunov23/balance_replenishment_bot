from aiogram.dispatcher.filters.state import StatesGroup, State


class StateUser(StatesGroup):
	entered_amounts = State()
	payment_processing = State()
	replenishment_passed = State()


class StateAdmin(StatesGroup):
	get_list = State()
	get_user = State()
	update_user = State()
	get_log = State()
