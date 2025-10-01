from fastapi import APIRouter, HTTPException
from app.services.keyword_service import keyword_service
from app.models.schemas import KeywordExtractRequest, KeywordExtractResponse

router = APIRouter(prefix="/keywords", tags=["keywords"])


@router.post("/extract", response_model=KeywordExtractResponse)
async def extract_keywords(request: KeywordExtractRequest):
    try:
        keywords = keyword_service.extract_keywords(
            request.html_content,
            request.max_keywords
        )
        
        return KeywordExtractResponse(
            success=True,
            keywords=keywords
        )
    except Exception as e:
        return KeywordExtractResponse(
            success=False,
            error=str(e)
        )

