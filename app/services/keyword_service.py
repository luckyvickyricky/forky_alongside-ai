from app.services.llm_service import llm_service


class KeywordService:
    def extract_keywords(self, html_content: str, max_keywords: int = 10) -> list[str]:
        prompt = f"""다음은 포트폴리오 문서의 HTML 내용입니다.
이 문서에서 면접 질문을 만들기 위한 핵심 키워드를 {max_keywords}개 추출해주세요.

키워드는 다음과 같은 것들을 포함해야 합니다:
- 사용한 기술 스택
- 프로젝트 이름
- 주요 기능이나 역할
- 중요한 개념이나 방법론

HTML 내용:
{html_content[:3000]}

다음 형식으로만 답변해주세요 (다른 설명 없이 키워드만):
키워드1, 키워드2, 키워드3, ...
"""
        
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        response = llm_service.generate_completion(messages)
        
        keywords = [k.strip() for k in response.split(',')]
        return keywords[:max_keywords]


keyword_service = KeywordService()

