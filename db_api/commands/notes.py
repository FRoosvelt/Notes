from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError

from db_api.database import get_session
from db_api.tables.notes import Notes_table


# Добавление заметки в база данных
async def add_new_note(
        user_id: int,
        title: str,
        description: str
):
    async with get_session() as session:
        note = Notes_table(
            user_id=user_id,
            title=title,
            description=description
        )
        session.add(note)
        try:
            await session.commit()
        except IntegrityError:
            await session.rollback()


# Удаление заметки из базы данных
async def delete_note(id: int):
    async with get_session() as session:
        sql = delete(Notes_table).where(
            Notes_table.id == id
        )
        await session.execute(sql)
        await session.commit()


# Найти id пользователя по id заметки
async def select_id_notes(user_id: int, id: int):
    async with get_session() as session:
        sql = select(user_id).where(
            Notes_table.id == id
        )
        result = await session.execute(sql)
        return result.scalar()


# Найти все заметки пользователя по фразе из базы данных
async def select_description_search_notes(user_id: int, keyword: str):
    async with get_session() as session:
        sql = select(Notes_table).where(
            Notes_table.user_id == user_id
        ).filter(
            Notes_table.description.like(keyword)
        )
        result = await session.execute(sql)
        return result.scalars().all()


# Найти все заметки пользователя из базы данных
async def select_all_notes(user_id: int):
    async with get_session() as session:
        sql = select(Notes_table).where(
            Notes_table.user_id == user_id
        )
        result = await session.execute(sql)
        return result.scalars().all()
