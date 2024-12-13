from typing import List, Dict
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.nft import Nft
from services.nft_service import get_metadata_from_transaction
from fastapi import APIRouter, HTTPException


async def get_nfts_image_and_time_by_user_id(db: AsyncSession, user_id: str) -> List[Dict[str, str]]:
    query = select(Nft.id, Nft.created_at).where(Nft.user_id == user_id)
    result = await db.execute(query)
    rows = result.fetchall()
    if not rows:
        raise HTTPException(status_code=404, detail="No NFTs found for the given user ID")
    nft_data = []
    for row in rows:
        nft_id, created_at = row[0], row[1]
        try:
            metadata = get_metadata_from_transaction(nft_id)
            image_url = metadata["metadata"].get("image", "")
            nft_data.append({"image_url": image_url, "created_at": created_at})
        except Exception as e:
            print(f"Error fetching metadata for NFT ID {nft_id}: {e}")
            nft_data.append(
                {"image_url": "Error retrieving metadata", "created_at": created_at})

    nft_data.sort(key=lambda x: x["created_at"], reverse=True)
    for nft in nft_data:
        nft["created_at"] = nft["created_at"].strftime("%m/%d %H:%M")

    return nft_data
