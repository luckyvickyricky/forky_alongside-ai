from pydantic import BaseModel
from typing import Optional, List


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


class DocumentParseResponse(BaseModel):
    success: bool
    html_content: Optional[str] = None
    error: Optional[str] = None
    metadata: Optional[dict] = None


class KeywordExtractRequest(BaseModel):
    html_content: str
    max_keywords: int = 10


class KeywordExtractResponse(BaseModel):
    success: bool
    keywords: Optional[List[str]] = None
    error: Optional[str] = None


class QuestionGenerateRequest(BaseModel):
    html_content: str
    keywords: Optional[List[str]] = None
    num_questions: int = 5


class Question(BaseModel):
    question_id: str
    question_text: str
    category: Optional[str] = None


class QuestionGenerateResponse(BaseModel):
    success: bool
    questions: Optional[List[Question]] = None
    error: Optional[str] = None
