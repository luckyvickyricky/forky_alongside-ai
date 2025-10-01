from pydantic import BaseModel
from typing import Optional


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


class DocumentParseResponse(BaseModel):
    success: bool
    html_content: Optional[str] = None
    error: Optional[str] = None
    metadata: Optional[dict] = None

