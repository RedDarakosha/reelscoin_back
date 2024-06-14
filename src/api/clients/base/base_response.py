from pydantic import BaseModel


class BaseResponse(BaseModel):
    status_code: str = ""
    body: dict = {}
    headers: dict = {}
    exceptions: dict = {}
    content_type: str = ""
