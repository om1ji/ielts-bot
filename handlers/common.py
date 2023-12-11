from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardMarkup
from orm import db
from keyboard import keyboards, buttons
from handlers import states
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery


async def NotImplemented(callback_query: CallbackQuery):
    await callback_query.answer("Not implemented yet")
