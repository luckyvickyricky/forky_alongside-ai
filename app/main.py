from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logging import langfuse_logger
from app.core.exceptions import ServiceException, service_exception_handler
from app.api.v1 import documents, keywords, questions, evaluate

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered interview practice system based on portfolio documents"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(ServiceException, service_exception_handler)

app.include_router(documents.router, prefix="/api/v1")
app.include_router(keywords.router, prefix="/api/v1")
app.include_router(questions.router, prefix="/api/v1")
app.include_router(evaluate.router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    if langfuse_logger.enabled:
        print("Langfuse logging is enabled")
    else:
        print("Langfuse logging is disabled")


@app.on_event("shutdown")
async def shutdown_event():
    if langfuse_logger.enabled:
        langfuse_logger.flush()


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
        "version": settings.app_version,
        "langfuse_enabled": settings.enable_langfuse
    }

