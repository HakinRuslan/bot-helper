from db.basemodel.basedao import *
from ..ormmodels.models import *
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc
from typing import Optional, Tuple


class ReviewsDao(BaseDAO[Review]):
    model = Review

    # @classmethod
    # async def get_full_summ(cls, session: AsyncSession) -> int:
    #     """Получить общую сумму покупок."""
    #     query = select(func.sum(cls.model.price).label('total_price'))
    #     result = await session.execute(query)
    #     total_price = result.scalars().one_or_none()
    #     return total_price if total_price is not None else 0
    
    # @classmethod
    # async def get_latest_active_purchase(
    #     cls, session: AsyncSession, user_id: int
    # ) -> Optional["Purchase"]:
    #     try:
    #         result = await session.execute(
    #             select(cls.model)
    #             .join(User)
    #             .options(selectinload(cls.model.tariff))
    #             .filter(User.id == user_id, cls.model.active.is_(True))
    #             .order_by(desc(cls.model.created_at))
    #             .limit(1)
    #         )
    #         purch = result.scalar_one_or_none()
        
    #         if purch is None:
    #             return None
                
    #         return purch

    #     except SQLAlchemyError as e:
    #         print(f"Ошибка при получении активной последней покупки: {e}")
    #         return None