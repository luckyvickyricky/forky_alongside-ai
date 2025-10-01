from openai import OpenAI
from app.core.config import settings


class LLMService:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.upstage_api_key,
            base_url=settings.upstage_base_url
        )
        self.model = settings.llm_model
    
    def generate_completion(self, messages: list[dict], stream: bool = False) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            reasoning_effort=settings.reasoning_effort,
            stream=stream
        )
        
        if stream:
            return response
        
        return response.choices[0].message.content


llm_service = LLMService()

