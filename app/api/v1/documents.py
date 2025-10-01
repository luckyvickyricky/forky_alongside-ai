from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_service import document_service
from app.models.schemas import DocumentParseResponse

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/parse", response_model=DocumentParseResponse)
async def parse_document(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    try:
        file_bytes = await file.read()
        result = document_service.parse_pdf_bytes(file_bytes, file.filename)
        
        return DocumentParseResponse(
            success=True,
            html_content=result.get("content", {}).get("html"),
            metadata=result
        )
    except Exception as e:
        return DocumentParseResponse(
            success=False,
            error=str(e)
        )

