# API 문서

## 기본 정보

- Base URL: `http://your-server:8000/api/v1`
- 모든 요청과 응답은 JSON 형식
- Swagger UI: `http://your-server:8000/api/docs`
- ReDoc: `http://your-server:8000/api/redoc`

## 엔드포인트

### 1. 헬스 체크

#### GET /api/v1/health

서버 상태를 확인합니다.

**Response**
```json
{
  "status": "healthy",
  "service": "Forky AI Interview Server",
  "version": "0.1.0",
  "langfuse_enabled": false
}
```

---

### 2. 문서 파싱

#### POST /api/v1/documents/parse

PDF 파일을 HTML로 변환합니다.

**Request**
- Content-Type: `multipart/form-data`
- Body: PDF 파일 (file)

**Response**
```json
{
  "success": true,
  "html_content": "<html>...</html>",
  "metadata": {...}
}
```

---

### 3. 키워드 추출

#### POST /api/v1/keywords/extract

포트폴리오 문서에서 키워드를 추출합니다.

**Request**
```json
{
  "html_content": "<html>...</html>",
  "max_keywords": 10
}
```

**Response**
```json
{
  "success": true,
  "keywords": [
    "React",
    "Node.js",
    "MongoDB",
    "REST API",
    "AWS"
  ]
}
```

---

### 4. 질문 생성

#### POST /api/v1/questions/generate

포트폴리오 기반 면접 질문을 생성합니다.

**Request**
```json
{
  "html_content": "<html>...</html>",
  "keywords": ["React", "Node.js"],
  "num_questions": 5
}
```

**Response**
```json
{
  "success": true,
  "questions": [
    {
      "question_id": "uuid-1",
      "question_text": "React 프로젝트에서 상태 관리는 어떻게 하셨나요?",
      "category": "기술"
    }
  ]
}
```

---

### 5. 꼬리질문 생성

#### POST /api/v1/questions/following

이전 답변을 바탕으로 꼬리질문을 생성합니다.

**Request**
```json
{
  "question": "React 프로젝트에 대해 설명해주세요",
  "answer": "Redux를 사용하여 상태 관리를 했습니다",
  "context": "optional context"
}
```

**Response**
```json
{
  "success": true,
  "following_question": "Redux의 어떤 패턴을 사용하셨나요?"
}
```

---

### 6. 답변 평가

#### POST /api/v1/questions/evaluate

답변을 평가하고 피드백을 제공합니다.

**Request**
```json
{
  "question": "React 프로젝트에 대해 설명해주세요",
  "answer": "Redux를 사용하여 상태 관리를 했습니다",
  "context": "optional context"
}
```

**Response**
```json
{
  "success": true,
  "feedback": {
    "score": 8,
    "strengths": [
      "구체적인 기술 스택 언급",
      "실무 경험 기반 답변"
    ],
    "weaknesses": [
      "구현 세부사항 부족"
    ],
    "suggestions": [
      "Redux의 미들웨어 사용 경험 추가",
      "성능 최적화 사례 언급"
    ],
    "overall_comment": "좋은 답변이지만 더 구체적인 설명이 필요합니다."
  }
}
```

---

### 7. 전체 면접 평가

#### POST /api/v1/evaluate/all

모든 질문-답변을 종합 평가합니다.

**Request**
```json
{
  "qa_pairs": [
    {
      "question": "첫 번째 질문",
      "answer": "첫 번째 답변"
    },
    {
      "question": "두 번째 질문",
      "answer": "두 번째 답변"
    }
  ],
  "portfolio_context": "optional context"
}
```

**Response**
```json
{
  "success": true,
  "evaluation": {
    "total_score": 85,
    "average_score": 8.5,
    "technical_competence": "상",
    "communication_skills": "중",
    "problem_solving": "상",
    "areas_of_strength": [
      "기술적 깊이",
      "실무 경험"
    ],
    "areas_for_improvement": [
      "의사소통 명확성"
    ],
    "final_recommendation": "기술 역량은 우수하나 설명력 보완 필요"
  }
}
```

---

### 8. 포트폴리오 평가

#### POST /api/v1/evaluate/portfolio

포트폴리오의 완성도를 평가합니다.

**Request**
```json
{
  "html_content": "<html>...</html>"
}
```

**Response**
```json
{
  "success": true,
  "evaluation": {
    "completeness_score": 8,
    "technical_depth_score": 7,
    "presentation_score": 9,
    "strengths": [
      "명확한 프로젝트 설명",
      "기술 스택 상세 기재"
    ],
    "improvements": [
      "성과 지표 추가 필요",
      "코드 샘플 부족"
    ],
    "overall_assessment": "전반적으로 우수한 포트폴리오입니다."
  }
}
```

---

## 에러 응답

모든 에러는 다음 형식으로 반환됩니다:

```json
{
  "success": false,
  "error": "Error message here"
}
```

HTTP 상태 코드:
- 200: 성공
- 400: 잘못된 요청
- 500: 서버 에러

---

## 사용 예제

### Python
```python
import requests

response = requests.post(
    "http://localhost:8000/api/v1/keywords/extract",
    json={
        "html_content": "<html>My portfolio</html>",
        "max_keywords": 5
    }
)

print(response.json())
```

### cURL
```bash
curl -X POST "http://localhost:8000/api/v1/keywords/extract" \
  -H "Content-Type: application/json" \
  -d '{
    "html_content": "<html>My portfolio</html>",
    "max_keywords": 5
  }'
```

### JavaScript
```javascript
fetch('http://localhost:8000/api/v1/keywords/extract', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    html_content: '<html>My portfolio</html>',
    max_keywords: 5
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

