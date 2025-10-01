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
        evaluation_data = overall_evaluation_service.evaluate_all_session(
            html_content=request.html_content,
            session_data=request.session_data.model_dump(),
            user_level=request.user_level
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
            request.html_content,
            portfolio_text=request.portfolio_text,
            evaluation_criteria=request.evaluation_criteria
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

