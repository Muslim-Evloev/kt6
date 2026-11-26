from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.task import Task
from app.schemas.task import TaskCreate


async def create_task(db: AsyncSession, data: TaskCreate, owner_id: int) -> Task:
    task = Task(title=data.title, description=data.description, owner_id=owner_id)
    db.add(task)
    await db.flush()
    await db.refresh(task)
    return task


async def get_user_tasks(db: AsyncSession, owner_id: int) -> list[Task]:
    result = await db.execute(select(Task).where(Task.owner_id == owner_id).order_by(Task.created_at.desc()))
    return list(result.scalars().all())