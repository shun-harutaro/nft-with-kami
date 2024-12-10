from sqlmodel.ext.asyncio.session import AsyncSession
from models.user import User
from typing import Optional


async def create_user(db: AsyncSession, user: User) -> User:
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user(db: AsyncSession, user_id: str) -> Optional[User]:
    return await db.get(User, user_id)


async def update_user(db: AsyncSession, user: User) -> User:
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def delete_user(db: AsyncSession, user_id: str) -> None:
    user = db.get(User, user_id)
    if user:
        await db.delete(user)
        await db.commit()
