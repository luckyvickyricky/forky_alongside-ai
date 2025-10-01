from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import documents, keywords, questions, evaluate

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered interview practice system based on portfolio documents"
)

app.include_router(documents.router, prefix="/api/v1")
app.include_router(keywords.router, prefix="/api/v1")
app.include_router(questions.router, prefix="/api/v1")
app.include_router(evaluate.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "message": "Forky AI Interview Server",
        "version": settings.app_version,
        "status": "running"
    }


@app.get("/api/v1/health")
async def health_check():
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version
    }

