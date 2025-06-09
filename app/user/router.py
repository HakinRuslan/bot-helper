from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from sqlalchemy.ext.asyncio import AsyncSession
from .user import UserDAO
from .kbs import *
from .schemas import *
from config import settings
from db.models.models.manager import *
from .form import *

user_router = Router()

@user_router.callback_query(F.data == "cancel")
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.answer('Отмена!')
    await call.message.edit_text(
        text="Произошла отмена. Выберите действие",
        reply_markup=()
    )


@user_router.callback_query(F.data == "rev")
async def cmd_start(message: Message, session_with_commit: AsyncSession):
    uservalues = Usersch(username = message.from_user.username, name = message.from_user.fullname)
    await UserDAO.add(session=session_with_commit, values = uservalues)
    return await message.answer(
        f"{message.from_user.full_name}, Выберите тип вашей проблемы:",
        reply_markup=extra_serv()
    )


@user_router.message()
async def page_home(message: Message, state: FSMContext):
    if message.from_user.text == "Проблемы с покупкой":
        await state.update_data(type_of_problem = message.text)
        msg = await message.answer(
            f"Хорошо. Пожайлуста, выбери тот кофе автомат, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
        await state.update_data(last_msg_id=msg.message_id)
        await state.set_state(Revinfo.coffee)
    elif message.from_user.text == "Неисправность автомата":
        await state.update_data(type_of_problem = message.text)
        msg = await message.answer(
            f"Хорошо. Пожайлуста, выбери тот кофе автомат, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
        await state.update_data(last_msg_id=msg.message_id)
        await state.set_state(Revinfo.coffee)
    elif message.from_user.text == "Хочу оставить отзыв":
        await state.update_data(type_of_problem = message.text)
        msg = await message.answer(
            f"Хорошо. Пожайлуста, выбери тот кофе автомат, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
        await state.update_data(last_msg_id=msg.message_id)
        await state.set_state(RevRealinfo.coffee)
    else:
        return await message.answer(
            f"Пожайлуста, выбери из списка вещей, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
    
@user_router.message(Revinfo.coffee)
async def page_home(message: Message, state: FSMContext):
    await state.update_data(type_of_problem = message.text)
    msg = await message.answer(
        f"Хорошо. Опиши, свои впечатления.",
    )
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(Revinfo.desc)

@user_router.message(RevRealinfo.coffee)
async def page_home(message: Message, state: FSMContext):
    await state.update_data(type_of_problem = message.text)
    msg = await message.answer(
        f"Хорошо. Опиши, свои впечатления.",
        reply_markup = cancel()
    )
    await state.update_data(last_msg_id=msg.message_id)
    await state.set_state(RevRealinfo.desc)
    
@user_router.message()
async def page_home(message: Message, state: FSMContext):
    if message.from_user.text == "Проблемы с покупкой":
        await state.update_data(type_of_problem = message.text)
        msg = await message.answer(
            f"Хорошо. Пожайлуста, выбери тот кофе автомат, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
        await state.update_data(last_msg_id=msg.message_id)
        await state.set_state(Revinfo.coffee)
    elif message.from_user.text == "Неисправность автомата":
        await state.update_data(type_of_problem = message.text)
        msg = await message.answer(
            f"Хорошо. Пожайлуста, выбери тот кофе автомат, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
        await state.update_data(last_msg_id=msg.message_id)
        await state.set_state(Revinfo.coffee)
    elif message.from_user.text == "Хочу оставить отзыв":
        await state.update_data(type_of_problem = message.text)
        msg = await message.answer(
            f"Хорошо. Пожайлуста, выбери тот кофе автомат, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
        await state.update_data(last_msg_id=msg.message_id)
        await state.set_state(RevRealinfo.coffee)
    else:
        return await message.answer(
            f"Пожайлуста, выбери из списка вещей, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
    

@user_router.message()
async def page_home(message: Message, state: FSMContext):
    if message.from_user.text == "Проблемы с покупкой":
        await state.update_data(type_of_problem = message.text)
        msg = await message.answer(
            f"Хорошо. Пожайлуста, выбери тот кофе автомат, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
        await state.update_data(last_msg_id=msg.message_id)
        await state.set_state(Revinfo.coffee)
    elif message.from_user.text == "Неисправность автомата":
        await state.update_data(type_of_problem = message.text)
        msg = await message.answer(
            f"Хорошо. Пожайлуста, выбери тот кофе автомат, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
        await state.update_data(last_msg_id=msg.message_id)
        await state.set_state(Revinfo.coffee)
    elif message.from_user.text == "Хочу оставить отзыв":
        await state.update_data(type_of_problem = message.text)
        msg = await message.answer(
            f"Хорошо. Пожайлуста, выбери тот кофе автомат, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
        await state.update_data(last_msg_id=msg.message_id)
        await state.set_state(RevRealinfo.coffee)
    else:
        return await message.answer(
            f"Пожайлуста, выбери из списка вещей, о чьем свое впечатление ты хочешь оставить!",
            reply_markup=extra_serv()
        )
    

# @user_router.callback_query(F.data == "my_profile")
# async def page_about(call: CallbackQuery, session_without_commit: AsyncSession):
#     await call.answer("Профиль")
#     user_info = await UserDAO.find_one_or_none(session=session_without_commit, filters=UserBaseInDB(telegram_id=call.from_user.id))
#     # Получаем статистику покупок пользователя
#     purchases = await UserDAO.get_purchased_products(session=session_without_commit, user_id=user_info.id)
#     # total_amount = purchases.get("total_amount", 0)
#     # total_purchases = purchases.get("total_purchases", 0)

#     # Формируем сообщение в зависимости от наличия покупок
#     # if total_purchases == 0:
#     #     await call.message.answer(
#     #         text="🔍 <b>У вас пока нет купленных тарифов.</b>\n\n"
#     #              "Откройте тарифы и выберите.",
#     #         reply_markup=main_user_kb(call.from_user.id)
#     if purchases:
#         text = (
#             f"🛍 <b>Ваш профиль:</b>\n\n"
#             f"Купленный тариф: <b>{purchases[0].tariff.name}</b>\n"
#             "Желаете посмотреть детали купленного вами тарифа?"
#         )
#         await call.message.answer(
#             text=text,
#             reply_markup=purchases_kb()
#         )
#     else:
#         text = (
#             f"🛍 <b>Ваш профиль:</b>\n\n"
#             f"<b>У вас не оформлена подписка, не куплен тарифф.</b>\n"
#             "Оформите подписку или тариф."
#         )
#         await call.message.answer(
#             text=text,
#             reply_markup=purchases_kb()
#         )

# @user_router.callback_query(F.data == "purchases")
# async def page_user_purchases(call: CallbackQuery, session_without_commit: AsyncSession):
#     await call.answer("Мой тариф")
#     user_info = await UserDAO.find_one_or_none(session=session_without_commit, filters=UserBaseInDB(telegram_id=call.from_user.id))
#     purchases = await UserDAO.get_purchased_products(session=session_without_commit, user_id=user_info.id)
#     if not purchases:
#         await call.message.edit_text(
#             text=f"🔍 <b>Вы пока не оформили подписку.</b>\n\n", reply_markup=main_user_kb(call.from_user.id)
#         )
#         return

#     tariff = purchases[0].tariff
#     typetariff = await TypeiftariffsDAO.find_one_or_none(session=session_without_commit, filters=TariffTypeIDModel(id=tariff.type_of_tarrifs_id))
#     tariff_text = (
#         f"📦 <b>Название подписки:</b> {tariff.name}\n\n"
#         f"💰 <b>Цена:</b> {purchases[0].price} $.\n\n"
#         f"📂 <b>Описание:</b>\n<i>{tariff.description}</i>\n\n"
#         f"❗ <b>Окончится в:</b>\n<i> в конце {format_date_russian(purchases[0].expires.strftime('%d/%m/%y'))}</i>\n\n"
#     )
#     await call.message.answer(
#             text=tariff_text,
#     )

#     await call.message.answer(
#         text="🙏 Спасибо за доверие!",
#         reply_markup=main_user_kb(call.from_user.id)
    )