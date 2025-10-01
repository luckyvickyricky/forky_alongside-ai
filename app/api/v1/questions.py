from fastapi import APIRouter
from app.services.question_service import question_service
from app.services.evaluation_service import evaluation_service
from app.models.schemas import (
    QuestionGenerateRequest, 
    QuestionGenerateResponse, 
    Question,
    FollowingQuestionRequest,
    FollowingQuestionResponse,
    FollowingQuestion,
    EvaluateAnswerRequest,
    EvaluateAnswerResponse,
    AnswerFeedback,
    DetailedFeedback
)

router = APIRouter(prefix="/questions", tags=["questions"])


@router.post("/generate", response_model=QuestionGenerateResponse)
async def generate_questions(request: QuestionGenerateRequest):
    try:
        content = request.html_content or request.text or ""
        
        questions_data = question_service.generate_main_questions(
            content,
            request.keywords or [],
            company=request.company,
            company_info=request.company_info,
            job_position=request.job_position,
            portfolio_text=request.portfolio_text
        )
        
        questions = [Question(**q) for q in questions_data]
        
        return QuestionGenerateResponse(
            success=True,
            questions=questions,
            is_fallback=False
        )
    except Exception as e:
        return QuestionGenerateResponse(
            success=False,
            error=str(e)
        )


@router.post("/following", response_model=FollowingQuestionResponse)
async def generate_following_question(request: FollowingQuestionRequest):
    try:
        following_questions = evaluation_service.generate_following_questions(
            request.question,
            request.answer,
            html_content=request.html_content,
            portfolio_text=request.portfolio_text,
            interviewer_persona=request.interviewer_persona,
            max_questions=request.max_questions or 2,
            context=request.context
        )
        
        questions = [FollowingQuestion(**q) for q in following_questions]
        
        return FollowingQuestionResponse(
            success=True,
            questions=questions
        )
    except Exception as e:
        return FollowingQuestionResponse(
            success=False,
            error=str(e)
        )


@router.post("/evaluate", response_model=EvaluateAnswerResponse)
async def evaluate_answer(request: EvaluateAnswerRequest):
    try:
        feedback_data = evaluation_service.evaluate_answer(
            request.question,
            request.answer,
            html_content=request.html_content,
            user_level=request.user_level
        )
        
        feedback = AnswerFeedback(**feedback_data)
        
        return EvaluateAnswerResponse(
            success=True,
            feedback=feedback
        )
    except Exception as e:
        return EvaluateAnswerResponse(
            success=False,
            error=str(e)
        )

