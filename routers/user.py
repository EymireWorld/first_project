from fastapi import APIRouter, Depends
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models_db.user import User as UserDB
from models_dto.user import User as UserDTO

router = APIRouter()


@router.post('/', tags = ['user'])
async def create_user(data: UserDTO, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        insert(UserDB).values(data.model_dump()).returning(UserDB)
    )
    await db.commit()

    return result.scalar()


@router.get('/{id}', tags = ['user'])
async def get_user(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(UserDB).where(UserDB.id == id)
    )

    return result.scalar()


@router.put('/{id}', tags = ['user'])
async def update_user(id: int, data: UserDTO, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        update(UserDB).where(UserDB.id == id).values(data.model_dump()).returning(UserDB)
    )
    await db.commit()

    return result.scalar()


@router.delete('/{id}', tags = ['user'])
async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        delete(UserDB).where(UserDB.id == id).returning(UserDB)
    )
    await db.commit()

    return result.scalar()
