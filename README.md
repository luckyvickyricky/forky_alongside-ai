# Forky AI Interview Server

포트폴리오 기반 AI 면접 연습 시스템의 백엔드 API 서버입니다.

## 목차

- [주요 기능](#주요-기능)
- [빠른 시작](#빠른-시작)
- [기술 스택](#기술-스택)
- [프로젝트 구조](#프로젝트-구조)
- [API 엔드포인트](#api-엔드포인트)
- [로컬 실행 방법](#로컬-실행-방법)
- [API 문서](#api-문서)
- [배포](#배포)
- [개발 가이드](#개발-가이드)

## 주요 기능

1. Document Parsing: PDF 포트폴리오를 HTML로 변환
2. Keyword Extraction: AI 기반 키워드 자동 추출
3. Question Generation: 포트폴리오 기반 면접 질문 생성
4. Answer Evaluation: 실시간 답변 평가 및 피드백
5. Following Questions: 답변 기반 꼬리질문 생성
6. Overall Evaluation: 전체 면접 결과 종합 평가
7. Portfolio Assessment: 포트폴리오 완성도 평가

## 빠른 시작

5분 안에 서버를 실행할 수 있습니다.

### 1. 설치

```bash
git clone https://github.com/your-repo/forky_alongside-ai.git
cd forky_alongside-ai
./scripts/install.sh
```

### 2. 환경 설정

```bash
cp env.example .env
nano .env
```

최소 필수 환경 변수:
```
UPSTAGE_API_KEY=your_key_here
UPSTAGE_DOCUMENT_API_KEY=your_key_here
```

### 3. 서버 실행

개발 모드:
```bash
./scripts/dev.sh
```

프로덕션 모드:
```bash
./scripts/start.sh
```

### 4. 확인

- API 문서: http://localhost:8000/api/docs
- 헬스 체크: http://localhost:8000/api/v1/health

```bash
curl http://localhost:8000/api/v1/health
```

## 기술 스택

- Framework: FastAPI
- LLM: Upstage Solar Pro2
- Document Engine: Upstage Document Parsing
- Logging: Langfuse (선택사항)
- Package Manager: UV
- Python: 3.10+

## 프로젝트 구조

```
forky_alongside-ai/
├── app/                        # 메인 애플리케이션
│   ├── api/v1/                # API 엔드포인트
│   │   ├── documents.py       # 문서 파싱
│   │   ├── keywords.py        # 키워드 추출
│   │   ├── questions.py       # 질문 생성/평가
│   │   └── evaluate.py        # 종합 평가
│   ├── core/                  # 핵심 설정
│   │   ├── config.py          # 환경 설정
│   │   ├── logging.py         # Langfuse 통합
│   │   ├── exceptions.py      # 에러 핸들링
│   │   └── middleware.py      # 요청 로깅
│   ├── models/                # 데이터 모델
│   │   └── schemas.py         # Pydantic 스키마
│   ├── services/              # 비즈니스 로직
│   │   ├── llm_service.py              # LLM 클라이언트
│   │   ├── document_service.py         # 문서 파싱
│   │   ├── keyword_service.py          # 키워드 추출
│   │   ├── question_service.py         # 질문 생성
│   │   ├── evaluation_service.py       # 답변 평가
│   │   └── overall_evaluation_service.py  # 종합 평가
│   └── main.py                # 애플리케이션 진입점
├── scripts/                   # 유틸리티 스크립트
│   ├── install.sh            # 설치 자동화
│   ├── dev.sh                # 개발 서버
│   ├── start.sh              # 프로덕션 서버
│   └── test.sh               # 테스트 실행
├── deployment/               # 배포 설정
│   ├── forky.service        # systemd 서비스
│   └── deploy.md            # 배포 가이드
├── examples/                # 사용 예제
│   └── simple_workflow.py   # 워크플로우 데모
└── test_server.py           # 서버 테스트
```

## API 엔드포인트

- `POST /api/v1/documents/parse` - PDF를 HTML로 변환
- `POST /api/v1/keywords/extract` - 문서에서 키워드 추출
- `POST /api/v1/questions/generate` - 메인 질문 생성
- `POST /api/v1/questions/following` - 꼬리질문 생성
- `POST /api/v1/questions/evaluate` - 단일 답변 평가 및 피드백
- `POST /api/v1/evaluate/all` - 전체 면접 결과 종합 평가
- `POST /api/v1/evaluate/portfolio` - 포트폴리오 완성도 평가
- `GET /api/v1/health` - 서버 상태 확인

## 로컬 실행 방법

### 사전 요구사항
- Python 3.10 이상
- UV 패키지 매니저

### 단계별 실행

#### 1. 저장소 클론
```bash
git clone https://github.com/your-repo/forky_alongside-ai.git
cd forky_alongside-ai
```

#### 2. UV 설치 (없는 경우)
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
```

#### 3. 의존성 설치
```bash
uv sync
```

#### 4. 환경 변수 설정
`.env` 파일을 생성하고 API 키를 입력합니다:
```bash
cp env.example .env
nano .env
```

필수 환경 변수:
```
UPSTAGE_API_KEY=up_AyzO9yJCPmeLcPjVR0v8dNhl8vHnt
UPSTAGE_DOCUMENT_API_KEY=up_fSlKyT6Kt0MhX3Fgn2sf8fe4zazZv
```

선택 환경 변수 (Langfuse 사용시):
```
ENABLE_LANGFUSE=false
LANGFUSE_SECRET_KEY=your_key
LANGFUSE_PUBLIC_KEY=your_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

#### 5. 개발 서버 실행
```bash
# 방법 1: 스크립트 사용 (권장)
./scripts/dev.sh

# 방법 2: 직접 실행
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### 6. 서버 확인
브라우저에서:
- Swagger UI: http://localhost:8000/api/docs
- ReDoc: http://localhost:8000/api/redoc
- Health Check: http://localhost:8000/api/v1/health

터미널에서:
```bash
curl http://localhost:8000/api/v1/health
```

#### 7. 워크플로우 테스트
서버가 실행 중인 상태에서 새 터미널을 열어:
```bash
uv run python examples/simple_workflow.py
```

### 문제 해결

#### 포트가 이미 사용 중
```bash
lsof -i :8000
kill -9 <PID>
```

#### 환경 변수 오류
`.env` 파일이 올바르게 설정되었는지 확인:
```bash
cat .env
```

#### 의존성 오류
```bash
rm -rf .venv
uv sync
```

#### Python 버전 확인
```bash
python3 --version
# 3.10 이상이어야 합니다
```

## API 문서

### 기본 정보

- Base URL: `http://localhost:8000/api/v1`
- 모든 요청과 응답은 JSON 형식
- Swagger UI: `http://localhost:8000/api/docs`
- ReDoc: `http://localhost:8000/api/redoc`

### 1. 헬스 체크

**GET /api/v1/health**

서버 상태를 확인합니다.

Response:
```json
{
  "status": "healthy",
  "service": "Forky AI Interview Server",
  "version": "0.1.0",
  "langfuse_enabled": false
}
```

### 2. 문서 파싱

**POST /api/v1/documents/parse**

PDF 파일을 HTML로 변환합니다.

Request:
- Content-Type: `multipart/form-data`
- Body: PDF 파일 (file)

Response:
```json
{
  "success": true,
  "html_content": "<html>...</html>",
  "metadata": {...}
}
```

### 3. 키워드 추출

**POST /api/v1/keywords/extract**

포트폴리오 문서에서 키워드를 추출합니다.

Request:
```json
{
  "html_content": "<html>...</html>",
  "max_keywords": 10
}
```

Response:
```json
{
  "success": true,
  "keywords": ["React", "Node.js", "MongoDB"]
}
```

### 4. 질문 생성

**POST /api/v1/questions/generate**

포트폴리오 기반 면접 질문을 생성합니다.

Request:
```json
{
  "keywords": ["React", "Node.js"],
  "company": "네이버",
  "text": "포트폴리오 텍스트",
  "html_content": "<html>...</html>",
  "portfolio_text": "포트폴리오 요약",
  "company_info": "회사 정보",
  "job_position": "백엔드 개발자"
}
```

Response:
```json
{
  "success": true,
  "questions": [
    {
      "id": "tech_1",
      "type": "technical",
      "text": "React 프로젝트에서 상태 관리는 어떻게 하셨나요?",
      "explanation": "기술",
      "question": "질문 내용",
      "answer": "답변 가이드"
    }
  ],
  "is_fallback": false
}
```

### 5. 꼬리질문 생성

**POST /api/v1/questions/following**

이전 답변을 바탕으로 꼬리질문을 생성합니다.

Request:
```json
{
  "html_content": "컨텍스트 정보",
  "question": "React 프로젝트에 대해 설명해주세요",
  "answer": "Redux를 사용하여 상태 관리를 했습니다",
  "interviewer_persona": "친근한_시니어",
  "portfolio_text": "포트폴리오 내용",
  "max_questions": 2,
  "context": "추가 컨텍스트"
}
```

Response:
```json
{
  "success": true,
  "questions": [
    {
      "id": "followup_1",
      "text": "Redux의 어떤 패턴을 사용하셨나요?",
      "type": "follow_up",
      "interviewer_persona": "친근한_시니어"
    }
  ]
}
```

### 6. 답변 평가

**POST /api/v1/questions/evaluate**

답변을 평가하고 피드백을 제공합니다.

Request:
```json
{
  "html_content": "포트폴리오 컨텍스트",
  "question": "React 프로젝트에 대해 설명해주세요",
  "answer": "Redux를 사용하여 상태 관리를 했습니다",
  "user_level": "intermediate"
}
```

Response:
```json
{
  "success": true,
  "feedback": {
    "overall_score": 75,
    "content_score": 80,
    "structure_score": 70,
    "technical_accuracy": 85,
    "improvement_suggestions": [
      "Redux의 미들웨어 사용 경험 추가",
      "성능 최적화 사례 언급"
    ],
    "positive_points": [
      "구체적인 기술 스택 언급",
      "실무 경험 기반 답변"
    ],
    "detailed_feedback": {
      "content": "내용에 대한 상세 피드백",
      "structure": "구조에 대한 피드백",
      "recommendations": "추천사항"
    }
  }
}
```

### 7. 전체 면접 평가

**POST /api/v1/evaluate/all**

모든 질문-답변을 종합 평가합니다.

Request:
```json
{
  "html_content": "포트폴리오 컨텍스트",
  "session_data": {
    "questions": ["질문1", "질문2"],
    "answers": ["답변1", "답변2"],
    "question_types": ["technical", "behavioral"]
  },
  "user_level": "intermediate"
}
```

Response:
```json
{
  "success": true,
  "evaluation": {
    "total_score": 85,
    "average_score": 8.5,
    "technical_competence": "상",
    "communication_skills": "중",
    "problem_solving": "상",
    "areas_of_strength": ["기술적 깊이", "실무 경험"],
    "areas_for_improvement": ["의사소통 명확성"],
    "final_recommendation": "기술 역량은 우수하나 설명력 보완 필요"
  }
}
```

### 8. 포트폴리오 평가

**POST /api/v1/evaluate/portfolio**

포트폴리오의 완성도를 평가합니다.

Request:
```json
{
  "html_content": "<html>...</html>",
  "portfolio_text": "포트폴리오 텍스트",
  "evaluation_criteria": ["기술적 깊이", "프로젝트 완성도"]
}
```

Response:
```json
{
  "success": true,
  "evaluation": {
    "completeness_score": 8,
    "technical_depth_score": 7,
    "presentation_score": 9,
    "strengths": ["명확한 프로젝트 설명", "기술 스택 상세 기재"],
    "improvements": ["성과 지표 추가 필요", "코드 샘플 부족"],
    "overall_assessment": "전반적으로 우수한 포트폴리오입니다."
  }
}
```

### 에러 응답

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

### 사용 예제

#### Python
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

#### cURL
```bash
curl -X POST "http://localhost:8000/api/v1/keywords/extract" \
  -H "Content-Type: application/json" \
  -d '{
    "html_content": "<html>My portfolio</html>",
    "max_keywords": 5
  }'
```

#### JavaScript
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

## 배포

### AWS EC2 배포

자세한 배포 가이드는 `deployment/deploy.md`를 참조하세요.

#### 빠른 배포
```bash
# EC2 인스턴스 접속
ssh -i your-key.pem ubuntu@your-ec2-ip

# 프로젝트 클론 및 설치
git clone https://github.com/your-repo/forky_alongside-ai.git
cd forky_alongside-ai
./scripts/install.sh

# 환경 변수 설정
cp env.example .env
nano .env

# systemd 서비스 등록
sudo cp deployment/forky.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable forky
sudo systemctl start forky

# 상태 확인
sudo systemctl status forky
```

### 프로덕션 서버 실행
```bash
./scripts/start.sh
```

## 개발 가이드

### 워크플로우

1. 사용자가 PDF 포트폴리오 업로드
2. 문서 파싱 및 키워드 추출
3. AI가 면접 질문 생성
4. 사용자 답변 수신
5. 답변 평가 및 피드백
6. 꼬리질문 생성 및 반복
7. 전체 면접 결과 평가
8. 포트폴리오 완성도 평가

### 로깅

모든 LLM 호출은 Langfuse를 통해 자동으로 로깅됩니다. Langfuse를 활성화하려면 환경 변수에서 `ENABLE_LANGFUSE=true`로 설정하고 관련 API 키를 입력하세요.

각 API 호출은 고유한 trace name으로 추적됩니다:
- `keyword_extraction`: 키워드 추출
- `question_generation`: 메인 질문 생성
- `following_question_generation`: 꼬리질문 생성
- `answer_evaluation`: 답변 평가
- `overall_evaluation`: 전체 면접 평가
- `portfolio_evaluation`: 포트폴리오 평가

### 테스트
```bash
# 간단한 서버 테스트
./scripts/test.sh

# 워크플로우 예제 실행 (서버가 실행 중이어야 함)
uv run python examples/simple_workflow.py
```

### 특징

- RESTful API 설계
- 자동 API 문서 생성 (Swagger UI, ReDoc)
- CORS 지원
- 요청 처리 시간 로깅
- LLM 호출 추적 (Langfuse)
- 환경 변수 기반 설정
- 배포 자동화 스크립트
- systemd 서비스 지원

## 변경 이력

### [0.1.0] - 2025-10-01

#### 추가된 기능
- 초기 프로젝트 구조 및 설정
- PDF 문서를 HTML로 변환하는 Document Parsing API
- 포트폴리오에서 키워드 추출 기능
- AI 기반 면접 질문 생성
- 사용자 답변 평가 및 피드백 시스템
- 꼬리질문 자동 생성
- 전체 면접 결과 종합 평가
- 포트폴리오 완성도 평가
- Langfuse 통합으로 LLM 호출 로깅
- CORS 설정으로 프론트엔드 통합 준비
- 커스텀 에러 핸들링
- 요청 처리 시간 로깅 미들웨어
- 배포 자동화 스크립트
- systemd 서비스 설정
- AWS EC2 배포 가이드
- API 문서화
- 워크플로우 예제 코드

#### API 명세 변경
외부 AI 서버 명세에 맞춰 파라미터를 수정했습니다:

1. 질문 생성: 회사 정보, 직무 정보 추가 지원
2. 꼬리질문: 면접관 페르소나, 최대 질문 수 지원
3. 답변 평가: 사용자 레벨 기반 평가, 상세 피드백 구조화
4. 전체 평가: 세션 데이터 구조화, 질문 타입 추가
5. 포트폴리오 평가: 평가 기준 커스터마이징 지원

## 라이센스

MIT License

## 버전

0.1.0 (2025-10-01)
