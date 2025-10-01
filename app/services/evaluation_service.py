from typing import Optional
from app.services.llm_service import llm_service


class EvaluationService:
    def evaluate_answer(
        self, 
        question: str, 
        answer: str, 
        html_content: Optional[str] = None,
        user_level: str = "intermediate"
    ) -> dict:
        context_text = f"\n참고 컨텍스트: {html_content}\n" if html_content else ""
        level_text = f"사용자 레벨: {user_level}\n"
        
        prompt = f"""당신은 면접관입니다. 다음 질문에 대한 지원자의 답변을 평가해주세요.
{level_text}{context_text}
질문: {question}

지원자 답변: {answer}

다음 형식으로 평가해주세요:

전체 점수: [100점 만점]
내용 점수: [100점 만점]
구조 점수: [100점 만점]
기술 정확도: [100점 만점]

긍정적 포인트:
- 강점1
- 강점2

개선 제안:
- 제안1
- 제안2

상세 피드백 - 내용:
[내용에 대한 피드백]

상세 피드백 - 구조:
[구조에 대한 피드백]

상세 피드백 - 추천사항:
[추천사항]
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
            "overall_score": 75,
            "content_score": 75,
            "structure_score": 75,
            "technical_accuracy": 75,
            "positive_points": [],
            "improvement_suggestions": [],
            "detailed_feedback": {
                "content": "",
                "structure": "",
                "recommendations": ""
            }
        }
        
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('전체 점수:'):
                try:
                    score = int(''.join(filter(str.isdigit, line.split(':', 1)[1])))
                    feedback["overall_score"] = min(max(score, 0), 100)
                except:
                    pass
            elif line.startswith('내용 점수:'):
                try:
                    score = int(''.join(filter(str.isdigit, line.split(':', 1)[1])))
                    feedback["content_score"] = min(max(score, 0), 100)
                except:
                    pass
            elif line.startswith('구조 점수:'):
                try:
                    score = int(''.join(filter(str.isdigit, line.split(':', 1)[1])))
                    feedback["structure_score"] = min(max(score, 0), 100)
                except:
                    pass
            elif line.startswith('기술 정확도:'):
                try:
                    score = int(''.join(filter(str.isdigit, line.split(':', 1)[1])))
                    feedback["technical_accuracy"] = min(max(score, 0), 100)
                except:
                    pass
            elif line == '긍정적 포인트:':
                current_section = 'positive'
            elif line.startswith('개선 제안:'):
                current_section = 'suggestions'
            elif line.startswith('상세 피드백 - 내용:'):
                current_section = 'detail_content'
            elif line.startswith('상세 피드백 - 구조:'):
                current_section = 'detail_structure'
            elif line.startswith('상세 피드백 - 추천사항:'):
                current_section = 'detail_recommendations'
            elif line.startswith('- '):
                item = line[2:].strip()
                if current_section == 'positive':
                    feedback['positive_points'].append(item)
                elif current_section == 'suggestions':
                    feedback['improvement_suggestions'].append(item)
            elif current_section == 'detail_content' and line:
                feedback['detailed_feedback']['content'] += line + ' '
            elif current_section == 'detail_structure' and line:
                feedback['detailed_feedback']['structure'] += line + ' '
            elif current_section == 'detail_recommendations' and line:
                feedback['detailed_feedback']['recommendations'] += line + ' '
        
        feedback['detailed_feedback']['content'] = feedback['detailed_feedback']['content'].strip()
        feedback['detailed_feedback']['structure'] = feedback['detailed_feedback']['structure'].strip()
        feedback['detailed_feedback']['recommendations'] = feedback['detailed_feedback']['recommendations'].strip()
        
        return feedback
    
    def generate_following_questions(
        self, 
        question: str, 
        answer: str,
        html_content: Optional[str] = None,
        portfolio_text: Optional[str] = None,
        interviewer_persona: Optional[str] = None,
        max_questions: int = 2,
        context: Optional[str] = None
    ) -> list[dict]:
        context_text = f"\n참고 컨텍스트: {html_content or context}\n" if html_content or context else ""
        portfolio_info = f"\nPortfolio: {portfolio_text}\n" if portfolio_text else ""
        persona = interviewer_persona or "친근한_시니어"
        
        prompt = f"""당신은 {persona} 성향의 면접관입니다. 지원자의 답변을 바탕으로 더 깊이 파고들 수 있는 꼬리질문을 {max_questions}개 만들어주세요.
{context_text}{portfolio_info}
기존 질문: {question}

지원자 답변: {answer}

지원자의 답변에서 구체적으로 확인하고 싶은 부분이나 더 깊이 물어볼 수 있는 꼬리질문 {max_questions}개를 작성해주세요.

다음 형식으로 작성해주세요:
1. 질문 내용
2. 질문 내용
"""
        
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        response = llm_service.generate_completion(messages, trace_name="following_question_generation")
        
        questions = []
        lines = response.strip().split('\n')
        
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if not line or not line[0].isdigit():
                continue
            
            parts = line.split('.', 1)
            if len(parts) < 2:
                continue
            
            content = parts[1].strip()
            
            questions.append({
                "id": f"followup_{i}",
                "text": content,
                "type": "follow_up",
                "interviewer_persona": persona
            })
        
        return questions[:max_questions]


evaluation_service = EvaluationService()

