from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from telegram_bot.services.database import SQLSessionContext


class DBSessionMiddleware(BaseMiddleware):
    session_pool: async_sessionmaker[AsyncSession]

    __slots__ = ("session_pool",)

    def __init__(self, session_pool: async_sessionmaker[AsyncSession]) -> None:
        self.session_pool = session_pool

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any | None:
        async with SQLSessionContext(session_pool=self.session_pool) as (
            repository,
            uow,
        ):
            data["repository"] = repository
            data["uow"] = uow
            return await handler(event, data)
