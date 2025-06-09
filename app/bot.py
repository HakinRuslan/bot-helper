import logging
from config import settings
import os
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, Redis


redis = Redis(host=settings.host_redis, port=settings.port_redis, password = settings.password_redis, db=0, decode_responses=True)
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

storage = RedisStorage(redis)

bot = Bot(token=settings.TOKEN_BOT, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher(storage=storage)