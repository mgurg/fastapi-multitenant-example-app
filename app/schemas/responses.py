from uuid import UUID

from pydantic import BaseModel


class BaseResponse(BaseModel):
    # may define additional fields or config shared across responses
    class Config:
        orm_mode = True


class StandardResponse(BaseResponse):
    ok: bool


class RoleBasic(BaseModel):
    role_name: str

    class Config:
        orm_mode = True


class UserLoginOut(BaseModel):  # OK
    auth_token: str
    first_name: str
    last_name: str
    tz: str
    lang: str
    uuid: UUID
    role_FK: RoleBasic

    class Config:
        orm_mode = True
