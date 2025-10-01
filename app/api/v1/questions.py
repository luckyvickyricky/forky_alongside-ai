from fastapi import APIRouter
from app.services.question_service import question_service
from app.services.evaluation_service import evaluation_service
from app.models.schemas import (
    QuestionGenerateRequest, 
    QuestionGenerateResponse, 
    Question,
    FollowingQuestionRequest,
    FollowingQuestionResponse,
    EvaluateAnswerRequest,
    EvaluateAnswerResponse,
    AnswerFeedback
)

router = APIRouter(prefix="/questions", tags=["questions"])


@router.post("/generate", response_model=QuestionGenerateResponse)
async def generate_questions(request: QuestionGenerateRequest):
    try:
        questions_data = question_service.generate_main_questions(
            request.html_content,
            request.keywords,
            request.num_questions
        )
        
        questions = [Question(**q) for q in questions_data]
        
        return QuestionGenerateResponse(
            success=True,
            questions=questions
        )
    except Exception as e:
        return QuestionGenerateResponse(
            success=False,
            error=str(e)
        )


@router.post("/following", response_model=FollowingQuestionResponse)
async def generate_following_question(request: FollowingQuestionRequest):
    try:
        following_question = evaluation_service.generate_following_question(
            request.question,
            request.answer,
            request.context
        )
        
        return FollowingQuestionResponse(
            success=True,
            following_question=following_question
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
            request.context
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

