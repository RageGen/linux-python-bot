from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

main_buttons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Find proccess or service by name."),KeyboardButton(text="System actions"),KeyboardButton(text="System monitoring")]
])
reply_buttons_unit_service = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="info"),KeyboardButton(text="stop"),KeyboardButton(text="restart")]
])
reply_buttons_unit_procces = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="info"),KeyboardButton(text="kill")]
])
reply_buttons_system_actions = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="reboot"),KeyboardButton(text="shut down")]
])
