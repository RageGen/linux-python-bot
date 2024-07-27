from bot_parts.functions import *
from aiogram import Router, F
from aiogram.filters import Command,CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import bot_parts.keyboard_buttons as kb
router=Router()
allowed_user_ids = []

class Unit(StatesGroup):
    name = State()
    action_service = State()
    action_process = State()
    
class System(StatesGroup):
    action=State()
    
    
@router.message(CommandStart())
async def write_file_c(message: Message,state: FSMContext)->None:
    if message.chat.id in allowed_user_ids:
        await message.answer("Hi! What do you want?",reply_markup=kb.main_buttons)
    else:
        await message.answer("Not to do, wrong user.")
        return
    
    
@router.message(Command('cancel'))
async def write_file_c(message: Message,state: FSMContext)->None:
    await message.answer("Cancel!",reply_markup=kb.main_buttons)
    await state.clear()

@router.message(F.text=="Find proccess or service by name.")
async def write_file_c(message: Message,state:FSMContext)->None:
    if message.chat.id in allowed_user_ids:
        await message.answer("Hi! What the process you want to find?", reply_markup=kb.ReplyKeyboardRemove())
        await state.set_state(Unit.name)
    else:
        await message.answer("Not to do, wrong user.")
        return
    
@router.message(F.text=="System actions")
async def write_file_c(message: Message,state:FSMContext)->None:
    if message.chat.id in allowed_user_ids:
        await message.answer("Hi! What do you want to do with system?",reply_markup=kb.reply_buttons_system_actions)
        await state.set_state(System.action)
    else:
        await message.answer("Not to do, wrong user.")
        return


@router.message(System.action)
async def write_file_c(message: Message,state:FSMContext)->None:
    await state.update_data(action=message.text)
    match message.text:
        case "reboot":
            await message.answer("Rebooting")
            reboot_system()
        case "shut down":
            await message.answer("Shutting down")
            shutdown_system()
        case _:
            await message.answer("Not to do")



@router.message(Unit.name)
async def write_file_c(message: Message,state:FSMContext)->None:
    await state.update_data(name=message.text)
    entry=determine_entity_type(message.text)
    await message.answer(entry)
    match entry:
        case "service":
            await message.answer("What you want to do with service?",reply_markup=kb.reply_buttons_unit_service)
            await state.set_state(Unit.action_service)
        case "process":
            await message.answer("What you want to do with process?",reply_markup=kb.reply_buttons_unit_procces)
            await state.set_state(Unit.action_process)
        case _:
            await message.answer("Not to do.")

@router.message(Unit.action_service)
async def process_dont_like_write_bots(message: Message, state: FSMContext) -> None:
    await state.update_data(action_service=message.text)
    data = await state.get_data()
    await message.answer(service_manager((data['name']),data['action_service']))
        
@router.message(Unit.action_process)
async def process_dont_like_write_bots(message: Message, state: FSMContext) -> None:
    await state.update_data(action_process=message.text)
    data = await state.get_data()
    await message.answer(process_manager((data['name']),data['action_process']))
        
@router.message(F.text == "System monitoring")
async def write_file_c(message: Message, state: FSMContext) -> None:
    if message.chat.id in allowed_user_ids:
        system_info = get_system_info()  
        await message.answer(system_info)
    else:
        await message.answer("Not to do, wrong user.")
        return
