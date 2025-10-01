from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


class ServiceException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class DocumentParsingException(ServiceException):
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class LLMException(ServiceException):
    def __init__(self, message: str):
        super().__init__(message, status_code=500)


async def service_exception_handler(request: Request, exc: ServiceException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message,
            "path": str(request.url)
        }
    )

