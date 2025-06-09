from db.basemodel.basedao import *
from db.models.ormmodels.models import *
from typing import Optional, Dict
from sqlalchemy import case, desc
from sqlalchemy.orm import selectinload
from datetime import datetime, timedelta, UTC
import pytz



class UserDAO(BaseDAO[User]):
    model = User

    # @classmethod
    # async def get_purchase_statistics(cls, session: AsyncSession, telegram_id: int) -> Optional[Dict[str, int]]:
    #     try:
    #         # Запрос для получения общего числа покупок и общей суммы
    #         result = await session.execute(
    #             select(
    #                 func.count(Purchase.id).label('total_purchases'),
    #                 func.sum(Purchase.price).label('total_amount')
    #             ).join(User).filter(User.telegram_id == telegram_id)
    #         )
    #         stats = result.one_or_none()

    #         if stats is None:
    #             return None

    #         total_purchases, total_amount = stats
    #         return {
    #             'total_purchases': total_purchases,
    #             'total_amount': total_amount or 0  # Обработка случая, когда сумма может быть None
    #         }

    #     except SQLAlchemyError as e:
    #         # Обработка ошибок при работе с базой данных
    #         print(f"Ошибка при получении статистики покупок пользователя: {e}")
    #         return None
        
    # @classmethod
    # async def get_statistics(cls, session: AsyncSession):
    #     try:
    #         now = datetime.now(pytz.UTC).replace(tzinfo=None)

    #         query = select(
    #             func.count().label('total_users'),
    #             func.sum(case((cls.model.created_at >= now - timedelta(days=1), 1), else_=0)).label('new_today'),
    #             func.sum(case((cls.model.created_at >= now - timedelta(days=7), 1), else_=0)).label('new_week'),
    #             func.sum(case((cls.model.created_at >= now - timedelta(days=30), 1), else_=0)).label('new_month')
    #         )

    #         result = await session.execute(query)
    #         stats = result.fetchone()

    #         statistics = {
    #             'total_users': stats.total_users,
    #             'new_today': stats.new_today,
    #             'new_week': stats.new_week,
    #             'new_month': stats.new_month
    #         }

    #         logger.info(f"Статистика успешно получена: {statistics}")
    #         return statistics
    #     except SQLAlchemyError as e:
    #         logger.error(f"Ошибка при получении статистики: {e}")
    #         raise

    # @classmethod
    # async def get_purchased_products(cls, session: AsyncSession, user_id: int) -> Optional[List[Purchase]]:
    #     try:
    #         # Запрос для получения пользователя с его покупками и связанными продуктами
    #         result = await session.execute(
    #             select(User)
    #             .options(
    #                 selectinload(User.purchases).selectinload(Purchase.tariff)
    #             )
    #             .filter(User.id == user_id)
    #         )
    #         user = result.scalar_one_or_none()

    #         if user is None:
    #             return None
    #         return user.purchases

    #     except SQLAlchemyError as e:
    #         # Обработка ошибок при работе с базой данных
    #         print(f"Ошибка при получении информации о покупках пользователя: {e}")
    #         return None

        
    # @classmethod
    # async def get_purchased_active(cls, session: AsyncSession, user_id: int) -> Optional[List[Purchase]]:
    #     try:
    #         # Запрос для получения пользователя с его покупками и связанными продуктами
    #         result = await session.execute(
    #             select(User)
    #             .options(
    #                 selectinload(User.purchases).selectinload(Purchase.tariff)
    #             )
    #             .filter(User.id == user_id)
    #         )
    #         user = result.scalar_one_or_none()

    #         if user is None:
    #             return None
    #         return next((purchase for purchase in user.purchases if purchase.active), None)


    #     except SQLAlchemyError as e:
    #         # Обработка ошибок при работе с базой данных
    #         print(f"Ошибка при получении информации о покупках пользователя: {e}")
    #         return None   


    # @classmethod
    # async def get_latest_purchases(cls, session: AsyncSession, user_id: int, limit: int = 1) -> Optional[List[Purchase]]:
    #     try:
    #         # Запрос для получения последних активных покупок пользователя по дате создания
    #         result = await session.execute(
    #             select(Purchase)
    #             .join(User)
    #             .options(selectinload(Purchase.tariff))
    #             .filter(User.id == user_id)
    #             .order_by(desc(Purchase.created_at))
    #             .limit(limit)
    #         )
    #         purchases = result.scalars().all()

    #         if not purchases:
    #             return None
    #         return purchases

    #     except SQLAlchemyError as e:
    #         # Обработка ошибок при работе с базой данных
    #         print(f"Ошибка при получении последних активных покупок пользователя: {e}")
    #         return None
    
    # @classmethod
    # async def update_user(cls, session: AsyncSession, record_id: int, values: BaseModel):
    #     values_dict = values.model_dump(exclude_unset=True)
    #     logger.info(f"Обновление записи {cls.model.__name__} с параметрами: {values_dict}")
        
    #     try:
            
    #         query = select(cls.model).filter_by(telegram_id=record_id)
    #         result = await session.execute(query)
    #         record = result.scalar_one_or_none()

    #         if not record:
    #             logger.info(f"Запись с id={record_id} не найдена")
    #             return None

    #         for key, value in values_dict.items():
    #             setattr(record, key, value)

    #         await session.flush()

    #         logger.info(f"Запись {cls.model.__name__} успешно обновлена")
    #         return record

    #     except SQLAlchemyError as e:
    #         await session.rollback()
    #         logger.error(f"Ошибка при обновлении записи: {e}")
    #         raise e   
