from celery import Celery
from app.config import get_settings

settings = get_settings()

celery_app = Celery(
    "kt6_worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)


@celery_app.task
def send_task_notification(task_id: int, title: str, owner_email: str):
    """Фоновая задача: имитация отправки уведомления о создании задачи."""
    import time
    time.sleep(2)  # имитация внешнего API
    print(f"[NOTIFICATION] Task #{task_id} '{title}' created for {owner_email}")
    return {"task_id": task_id, "status": "notified"}