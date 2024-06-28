from pydantic import (
    BaseModel,
    Field,
    ConfigDict
)


class ChangeEmail(BaseModel):
    model_config = ConfigDict(extra='forbid')
    login: str = Field(..., description='Логин')
    email: str = Field(..., description='Email')
    password: str = Field(..., description='Пароль')