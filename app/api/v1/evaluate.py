from fastapi import APIRouter
from app.services.overall_evaluation_service import overall_evaluation_service
from app.models.schemas import (
    EvaluateAllRequest,
    EvaluateAllResponse,
    OverallEvaluation,
    EvaluatePortfolioRequest,
    EvaluatePortfolioResponse,
    PortfolioEvaluation
)

router = APIRouter(prefix="/evaluate", tags=["evaluate"])


@router.post("/all", response_model=EvaluateAllResponse)
async def evaluate_all(request: EvaluateAllRequest):
    try:
        qa_pairs = [qa.model_dump() for qa in request.qa_pairs]
        
        evaluation_data = overall_evaluation_service.evaluate_all_answers(
            qa_pairs,
            request.portfolio_context
        )
        
        evaluation = OverallEvaluation(**evaluation_data)
        
        return EvaluateAllResponse(
            success=True,
            evaluation=evaluation
        )
    except Exception as e:
        return EvaluateAllResponse(
            success=False,
            error=str(e)
        )


@router.post("/portfolio", response_model=EvaluatePortfolioResponse)
async def evaluate_portfolio(request: EvaluatePortfolioRequest):
    try:
        evaluation_data = overall_evaluation_service.evaluate_portfolio(
            request.html_content
        )
        
        evaluation = PortfolioEvaluation(**evaluation_data)
        
        return EvaluatePortfolioResponse(
            success=True,
            evaluation=evaluation
        )
    except Exception as e:
        return EvaluatePortfolioResponse(
            success=False,
            error=str(e)
        )

