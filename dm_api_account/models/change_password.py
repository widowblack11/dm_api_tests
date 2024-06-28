
from typing import Optional
from uuid import UUID
from pydantic import (
    BaseModel,
    Field,
    StrictStr,
)


class ChangePassword(BaseModel):
    login: Optional[StrictStr] = Field(None, description='User login')
    #token: Optional[UUID] = Field(None, description='Password reset token')
    token: str
    old_password: Optional[StrictStr] = Field(
        None, description='Старый пароль',
        serialization_alias='oldPassword'
    )
    new_password: Optional[StrictStr] = Field(
        None, description='Новый пароль',
        serialization_alias='newPassword'
    )