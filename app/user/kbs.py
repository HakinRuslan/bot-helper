from typing import List
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardBuilder, ReplyKeyboardMarkup
from db.models.ormmodels.models import *
from db.models.models.manager import *
from user.user import UserDAO
from .form import Pagination
from .schemas import *


def cancel() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Отмена", callback_data="cancel")
    kb.adjust(2)
    return kb.as_markup()

def revkbs() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Оставить впечатления", callback_data="rev")
    kb.adjust(2)
    return kb.as_markup()


def extra_serv() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Проблемы с покупкой")
    kb.button(text="Неисправность автомата")
    kb.button(text="Хочу оставить отзыв")
    kb.adjust(1)
    
    return kb.as_markup(resize_keyboard=True)