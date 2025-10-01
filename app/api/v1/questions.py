from fastapi import APIRouter
from app.services.question_service import question_service
from app.models.schemas import QuestionGenerateRequest, QuestionGenerateResponse, Question

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

