from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user, require_admin
from app.models.user import User
from app.schemas.user import UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
async def read_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/admin-only", response_model=list[UserResponse])
async def admin_endpoint(admin: User = Depends(require_admin)):
    """Эндпоинт, защищённый по роли admin (RBAC)."""
    return [admin]