from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    app_name: str = "Forky AI Interview Server"
    app_version: str = "0.1.0"
    
    upstage_api_key: str
    upstage_base_url: str = "https://api.upstage.ai/v1"
    upstage_document_api_key: str
    
    llm_model: str = "solar-pro2"
    reasoning_effort: str = "high"
    
    langfuse_secret_key: Optional[str] = None
    langfuse_public_key: Optional[str] = None
    langfuse_host: Optional[str] = None
    enable_langfuse: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

