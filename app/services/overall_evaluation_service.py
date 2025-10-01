from typing import Optional, List
from app.services.llm_service import llm_service


class OverallEvaluationService:
    def evaluate_all_answers(
        self, 
        qa_pairs: List[dict], 
        portfolio_context: Optional[str] = None
    ) -> dict:
        qa_text = "\n\n".join([
            f"질문 {i+1}: {qa['question']}\n답변: {qa['answer']}"
            for i, qa in enumerate(qa_pairs)
        ])
        
        context_text = f"\n포트폴리오 컨텍스트:\n{portfolio_context[:2000]}\n" if portfolio_context else ""
        
        prompt = f"""당신은 면접관입니다. 전체 면접을 종합적으로 평가해주세요.
{context_text}
면접 내용:
{qa_text}

다음 형식으로 평가해주세요:

총점: [100점 만점]
평균 점수: [10점 만점 평균]

기술 역량: [상/중/하]
의사소통 능력: [상/중/하]
문제 해결 능력: [상/중/하]

강점 영역:
- 강점1
- 강점2
- 강점3

개선 필요 영역:
- 개선1
- 개선2

최종 추천:
[전반적인 평가와 채용 추천 의견]
"""
        
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        response = llm_service.generate_completion(messages, trace_name="overall_evaluation")
        
        evaluation = self._parse_overall_evaluation(response)
        return evaluation
    
    def _parse_overall_evaluation(self, response: str) -> dict:
        lines = response.strip().split('\n')
        
        evaluation = {
            "total_score": 70,
            "average_score": 7.0,
            "technical_competence": "중",
            "communication_skills": "중",
            "problem_solving": "중",
            "areas_of_strength": [],
            "areas_for_improvement": [],
            "final_recommendation": ""
        }
        
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('총점:'):
                try:
                    score_text = line.split(':', 1)[1].strip()
                    score = int(''.join(filter(str.isdigit, score_text)))
                    evaluation["total_score"] = min(max(score, 0), 100)
                except:
                    pass
            elif line.startswith('평균 점수:'):
                try:
                    score_text = line.split(':', 1)[1].strip()
                    score = float(''.join(c for c in score_text if c.isdigit() or c == '.'))
                    evaluation["average_score"] = min(max(score, 0.0), 10.0)
                except:
                    pass
            elif line.startswith('기술 역량:'):
                evaluation["technical_competence"] = line.split(':', 1)[1].strip()
            elif line.startswith('의사소통 능력:'):
                evaluation["communication_skills"] = line.split(':', 1)[1].strip()
            elif line.startswith('문제 해결 능력:'):
                evaluation["problem_solving"] = line.split(':', 1)[1].strip()
            elif line == '강점 영역:':
                current_section = 'strength'
            elif line == '개선 필요 영역:':
                current_section = 'improvement'
            elif line.startswith('최종 추천:'):
                current_section = 'recommendation'
            elif line.startswith('- '):
                item = line[2:].strip()
                if current_section == 'strength':
                    evaluation['areas_of_strength'].append(item)
                elif current_section == 'improvement':
                    evaluation['areas_for_improvement'].append(item)
            elif current_section == 'recommendation' and line:
                evaluation['final_recommendation'] += line + ' '
        
        evaluation['final_recommendation'] = evaluation['final_recommendation'].strip()
        
        return evaluation
    
    def evaluate_portfolio(self, html_content: str) -> dict:
        prompt = f"""당신은 포트폴리오 평가 전문가입니다. 다음 포트폴리오의 완성도를 평가해주세요.

포트폴리오 내용:
{html_content[:4000]}

다음 형식으로 평가해주세요:

완성도 점수: [10점 만점]
기술 깊이 점수: [10점 만점]
표현력 점수: [10점 만점]

강점:
- 강점1
- 강점2
- 강점3

개선사항:
- 개선1
- 개선2

종합 평가:
[전반적인 포트폴리오 품질 평가]
"""
        
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        response = llm_service.generate_completion(messages, trace_name="portfolio_evaluation")
        
        evaluation = self._parse_portfolio_evaluation(response)
        return evaluation
    
    def _parse_portfolio_evaluation(self, response: str) -> dict:
        lines = response.strip().split('\n')
        
        evaluation = {
            "completeness_score": 7,
            "technical_depth_score": 7,
            "presentation_score": 7,
            "strengths": [],
            "improvements": [],
            "overall_assessment": ""
        }
        
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('완성도 점수:'):
                try:
                    score_text = line.split(':', 1)[1].strip()
                    score = int(''.join(filter(str.isdigit, score_text)))
                    evaluation["completeness_score"] = min(max(score, 0), 10)
                except:
                    pass
            elif line.startswith('기술 깊이 점수:'):
                try:
                    score_text = line.split(':', 1)[1].strip()
                    score = int(''.join(filter(str.isdigit, score_text)))
                    evaluation["technical_depth_score"] = min(max(score, 0), 10)
                except:
                    pass
            elif line.startswith('표현력 점수:'):
                try:
                    score_text = line.split(':', 1)[1].strip()
                    score = int(''.join(filter(str.isdigit, score_text)))
                    evaluation["presentation_score"] = min(max(score, 0), 10)
                except:
                    pass
            elif line == '강점:':
                current_section = 'strengths'
            elif line == '개선사항:':
                current_section = 'improvements'
            elif line.startswith('종합 평가:'):
                current_section = 'overall'
            elif line.startswith('- '):
                item = line[2:].strip()
                if current_section in ['strengths', 'improvements']:
                    evaluation[current_section].append(item)
            elif current_section == 'overall' and line:
                evaluation['overall_assessment'] += line + ' '
        
        evaluation['overall_assessment'] = evaluation['overall_assessment'].strip()
        
        return evaluation


overall_evaluation_service = OverallEvaluationService()

