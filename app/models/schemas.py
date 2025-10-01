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
    keywords: Optional[List[str]] = None
    company: Optional[str] = None
    text: Optional[str] = None
    html_content: Optional[str] = None
    portfolio_text: Optional[str] = None
    company_info: Optional[str] = None
    job_position: Optional[str] = None


class Question(BaseModel):
    id: str
    type: str
    text: str
    explanation: Optional[str] = None
    question: Optional[str] = None
    answer: Optional[str] = None


class QuestionGenerateResponse(BaseModel):
    success: bool
    questions: Optional[List[Question]] = None
    is_fallback: Optional[bool] = None
    fallback_reason: Optional[str] = None
    error: Optional[str] = None


class FollowingQuestionRequest(BaseModel):
    html_content: Optional[str] = None
    question: str
    answer: str
    interviewer_persona: Optional[str] = None
    portfolio_text: Optional[str] = None
    max_questions: Optional[int] = 2
    context: Optional[str] = None


class FollowingQuestion(BaseModel):
    id: str
    text: str
    type: str
    interviewer_persona: Optional[str] = None


class FollowingQuestionResponse(BaseModel):
    success: bool
    questions: Optional[List[FollowingQuestion]] = None
    error: Optional[str] = None


class EvaluateAnswerRequest(BaseModel):
    html_content: Optional[str] = None
    question: str
    answer: str
    user_level: Optional[str] = "intermediate"


class DetailedFeedback(BaseModel):
    content: str
    structure: str
    recommendations: str


class AnswerFeedback(BaseModel):
    overall_score: int
    content_score: int
    structure_score: int
    technical_accuracy: int
    improvement_suggestions: List[str]
    positive_points: List[str]
    detailed_feedback: DetailedFeedback


class EvaluateAnswerResponse(BaseModel):
    success: bool
    feedback: Optional[AnswerFeedback] = None
    error: Optional[str] = None


class SessionData(BaseModel):
    questions: List[str]
    answers: List[str]
    question_types: List[str]


class EvaluateAllRequest(BaseModel):
    html_content: Optional[str] = None
    session_data: SessionData
    user_level: Optional[str] = "intermediate"


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
    portfolio_text: Optional[str] = None
    evaluation_criteria: Optional[List[str]] = None


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
