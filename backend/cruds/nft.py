from sqlmodel.ext.asyncio.session import AsyncSession
from models.nft import Nft
from typing import Optional
from sqlalchemy.future import select


async def create_nft(db: AsyncSession, nft: Nft) -> Nft:
    db.add(nft)
    await db.commit()
    await db.refresh(nft)
    return nft


async def get_nft(db: AsyncSession, id: str) -> Optional[Nft]:
    return await db.get(Nft, id)


async def update_nft(db: AsyncSession, nft: Nft) -> Nft:
    db.add(nft)
    await db.commit()
    await db.refresh(nft)
    return nft


async def delete_nft(db: AsyncSession, nft: Nft) -> None:
    await db.delete(nft)
    await db.commit()
