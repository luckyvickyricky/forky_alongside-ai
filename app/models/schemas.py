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


class FollowingQuestionRequest(BaseModel):
    question: str
    answer: str
    context: Optional[str] = None


class FollowingQuestionResponse(BaseModel):
    success: bool
    following_question: Optional[str] = None
    error: Optional[str] = None


class EvaluateAnswerRequest(BaseModel):
    question: str
    answer: str
    context: Optional[str] = None


class AnswerFeedback(BaseModel):
    score: int
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]
    overall_comment: str


class EvaluateAnswerResponse(BaseModel):
    success: bool
    feedback: Optional[AnswerFeedback] = None
    error: Optional[str] = None


class QAPair(BaseModel):
    question: str
    answer: str


class EvaluateAllRequest(BaseModel):
    qa_pairs: List[QAPair]
    portfolio_context: Optional[str] = None


class OverallEvaluation(BaseModel):
    total_score: int
    average_score: float
    technical_competence: str
    communication_skills: str
    problem_solving: str
    areas_of_strength: List[str]
    areas_for_improvement: List[str]
    final_recommendation: str


class EvaluateAllResponse(BaseModel):
    success: bool
    evaluation: Optional[OverallEvaluation] = None
    error: Optional[str] = None


class EvaluatePortfolioRequest(BaseModel):
    html_content: str


class PortfolioEvaluation(BaseModel):
    completeness_score: int
    technical_depth_score: int
    presentation_score: int
    strengths: List[str]
    improvements: List[str]
    overall_assessment: str


class EvaluatePortfolioResponse(BaseModel):
    success: bool
    evaluation: Optional[PortfolioEvaluation] = None
    error: Optional[str] = None
