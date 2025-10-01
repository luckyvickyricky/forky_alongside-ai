from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_service import document_service

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/parse")
async def parse_document(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    try:
        file_bytes = await file.read()
        result = document_service.parse_pdf_bytes(file_bytes, file.filename)
        
        # html_content만 반환
        html_content = result.get("content", {}).get("html")
        if not html_content:
            raise HTTPException(status_code=500, detail="Failed to extract HTML content from PDF")
        
        return {"html_content": html_content}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Document parsing failed: {str(e)}")

