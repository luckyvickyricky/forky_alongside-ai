import uuid
from typing import Optional
from app.services.llm_service import llm_service


class QuestionService:
    def generate_main_questions(
        self, 
        html_content: str, 
        keywords: Optional[list[str]] = None,
        num_questions: int = 5
    ) -> list[dict]:
        keyword_text = ""
        if keywords:
            keyword_text = f"\n주요 키워드: {', '.join(keywords)}\n"
        
        prompt = f"""당신은 면접관입니다. 다음 포트폴리오 문서를 바탕으로 {num_questions}개의 면접 질문을 만들어주세요.
{keyword_text}
포트폴리오 내용:
{html_content[:4000]}

질문은 다음 조건을 만족해야 합니다:
1. 포트폴리오에 명시된 경험과 기술을 기반으로 한 질문
2. 지원자의 실제 역량과 이해도를 파악할 수 있는 질문
3. 구체적이고 답변을 유도할 수 있는 질문
4. 각 질문은 서로 다른 측면을 다루어야 함

다음 형식으로 답변해주세요:
1. [카테고리] 질문 내용
2. [카테고리] 질문 내용
...

카테고리는 다음 중 하나여야 합니다: 기술, 경험, 문제해결, 협업, 성장
"""
        
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        response = llm_service.generate_completion(messages, trace_name="question_generation")
        
        questions = []
        lines = response.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if not line or not line[0].isdigit():
                continue
            
            parts = line.split('.', 1)
            if len(parts) < 2:
                continue
            
            content = parts[1].strip()
            category = None
            
            if content.startswith('['):
                end_bracket = content.find(']')
                if end_bracket > 0:
                    category = content[1:end_bracket]
                    content = content[end_bracket+1:].strip()
            
            questions.append({
                "question_id": str(uuid.uuid4()),
                "question_text": content,
                "category": category
            })
        
        return questions[:num_questions]


question_service = QuestionService()

