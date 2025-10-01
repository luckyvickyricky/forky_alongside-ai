from typing import Optional
from langfuse import Langfuse
from app.core.config import settings


class LangfuseLogger:
    def __init__(self):
        self.client: Optional[Langfuse] = None
        self.enabled = settings.enable_langfuse
        
        if self.enabled and all([
            settings.langfuse_secret_key,
            settings.langfuse_public_key,
            settings.langfuse_host
        ]):
            self.client = Langfuse(
                secret_key=settings.langfuse_secret_key,
                public_key=settings.langfuse_public_key,
                host=settings.langfuse_host
            )
    
    def trace(self, name: str, metadata: dict = None):
        if self.client:
            return self.client.trace(name=name, metadata=metadata)
        return None
    
    def generation(self, trace_id: str, name: str, model: str, input_data: list, output: str, metadata: dict = None):
        if self.client:
            return self.client.generation(
                trace_id=trace_id,
                name=name,
                model=model,
                input=input_data,
                output=output,
                metadata=metadata
            )
        return None
    
    def flush(self):
        if self.client:
            self.client.flush()


langfuse_logger = LangfuseLogger()

