from typing import Optional
from app.services.llm_service import llm_service


class EvaluationService:
    def evaluate_answer(
        self, 
        question: str, 
        answer: str, 
        context: Optional[str] = None
    ) -> dict:
        context_text = f"\n참고 컨텍스트: {context}\n" if context else ""
        
        prompt = f"""당신은 면접관입니다. 다음 질문에 대한 지원자의 답변을 평가해주세요.
{context_text}
질문: {question}

지원자 답변: {answer}

다음 형식으로 평가해주세요:

점수: [1-10 사이의 숫자]

강점:
- 강점1
- 강점2

약점:
- 약점1
- 약점2

개선 제안:
- 제안1
- 제안2

종합 의견:
[전반적인 평가]
"""
        
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        response = llm_service.generate_completion(messages, trace_name="answer_evaluation")
        
        feedback = self._parse_feedback(response)
        return feedback
    
    def _parse_feedback(self, response: str) -> dict:
        lines = response.strip().split('\n')
        
        feedback = {
            "score": 5,
            "strengths": [],
            "weaknesses": [],
            "suggestions": [],
            "overall_comment": ""
        }
        
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('점수:'):
                try:
                    score_text = line.split(':', 1)[1].strip()
                    score = int(''.join(filter(str.isdigit, score_text)))
                    feedback["score"] = min(max(score, 1), 10)
                except:
                    pass
            elif line == '강점:':
                current_section = 'strengths'
            elif line == '약점:':
                current_section = 'weaknesses'
            elif line.startswith('개선 제안:'):
                current_section = 'suggestions'
            elif line.startswith('종합 의견:'):
                current_section = 'overall'
            elif line.startswith('- '):
                item = line[2:].strip()
                if current_section in ['strengths', 'weaknesses', 'suggestions']:
                    feedback[current_section].append(item)
            elif current_section == 'overall' and line:
                feedback['overall_comment'] += line + ' '
        
        feedback['overall_comment'] = feedback['overall_comment'].strip()
        
        return feedback
    
    def generate_following_question(
        self, 
        question: str, 
        answer: str, 
        context: Optional[str] = None
    ) -> str:
        context_text = f"\n참고 컨텍스트: {context}\n" if context else ""
        
        prompt = f"""당신은 면접관입니다. 지원자의 답변을 바탕으로 더 깊이 파고들 수 있는 꼬리질문을 만들어주세요.
{context_text}
기존 질문: {question}

지원자 답변: {answer}

지원자의 답변에서 구체적으로 확인하고 싶은 부분이나 더 깊이 물어볼 수 있는 꼬리질문 1개를 작성해주세요.
질문만 작성하고 다른 설명은 하지 마세요.
"""
        
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        response = llm_service.generate_completion(messages, trace_name="following_question_generation")
        
        return response.strip()


evaluation_service = EvaluationService()

