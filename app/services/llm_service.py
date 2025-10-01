from openai import OpenAI
from app.core.config import settings
from app.core.logging import langfuse_logger
import uuid


class LLMService:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.upstage_api_key,
            base_url=settings.upstage_base_url
        )
        self.model = settings.llm_model
    
    def generate_completion(
        self, 
        messages: list[dict], 
        stream: bool = False,
        trace_name: str = "llm_completion"
    ) -> str:
        trace_id = str(uuid.uuid4())
        
        if langfuse_logger.enabled:
            trace = langfuse_logger.trace(
                name=trace_name,
                metadata={"model": self.model, "stream": stream}
            )
            if trace:
                trace_id = trace.id
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            reasoning_effort=settings.reasoning_effort,
            stream=stream
        )
        
        if stream:
            return response
        
        output = response.choices[0].message.content
        
        if langfuse_logger.enabled:
            langfuse_logger.generation(
                trace_id=trace_id,
                name=trace_name,
                model=self.model,
                input_data=messages,
                output=output,
                metadata={"reasoning_effort": settings.reasoning_effort}
            )
        
        return output


llm_service = LLMService()

