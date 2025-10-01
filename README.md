# Forky AI Interview Server

포트폴리오 기반 AI 면접 연습 시스템의 백엔드 API 서버입니다.

## 주요 기능

- PDF 포트폴리오 문서를 HTML로 변환
- 문서에서 키워드 자동 추출
- 포트폴리오 기반 면접 질문 자동 생성
- 답변에 대한 실시간 피드백 제공
- 꼬리질문 자동 생성
- 전체 면접 결과 종합 평가
- 포트폴리오 완성도 평가

## 기술 스택

- Python 3.10+
- FastAPI
- Upstage Solar Pro2 (LLM)
- Upstage Document Parsing
- Langfuse (로깅 및 모니터링)
- UV (패키지 관리)

## 프로젝트 구조

```
forky_alongside-ai/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── documents.py
│   │       ├── keywords.py
│   │       ├── questions.py
│   │       └── evaluate.py
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   ├── services/
│   │   ├── document_service.py
│   │   ├── llm_service.py
│   │   └── evaluation_service.py
│   └── main.py
├── example_file/
├── pyproject.toml
└── README.md
```

## API 엔드포인트

### Document Processing
- `POST /api/v1/documents/parse` - PDF를 HTML로 변환
- `POST /api/v1/keywords/extract` - 문서에서 키워드 추출

### Question Generation
- `POST /api/v1/questions/generate` - 메인 질문 생성
- `POST /api/v1/questions/following` - 꼬리질문 생성

### Evaluation
- `POST /api/v1/questions/evaluate` - 단일 답변 평가 및 피드백
- `POST /api/v1/evaluate/all` - 전체 면접 결과 종합 평가
- `POST /api/v1/evaluate/portfolio` - 포트폴리오 완성도 평가

### Health Check
- `GET /api/v1/health` - 서버 상태 확인

## 설치 및 실행

### 사전 요구사항
- Python 3.10 이상
- UV 패키지 매니저

### 설치
```bash
# UV 설치 (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 의존성 설치
uv sync
```

### 환경 변수 설정
`.env` 파일을 생성하고 다음 내용을 입력합니다:
```
UPSTAGE_API_KEY=your_upstage_api_key
UPSTAGE_BASE_URL=https://api.upstage.ai/v1
UPSTAGE_DOCUMENT_API_KEY=your_document_api_key

ENABLE_LANGFUSE=false
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

참고: `env.example` 파일을 복사하여 사용할 수 있습니다.

### 개발 서버 실행
```bash
# 방법 1: 스크립트 사용
./scripts/dev.sh

# 방법 2: 직접 실행
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 프로덕션 서버 실행
```bash
# 방법 1: 스크립트 사용
./scripts/start.sh

# 방법 2: 직접 실행
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 워크플로우

1. 사용자가 PDF 포트폴리오 업로드
2. `document-parsing`으로 문서 파싱 및 정보 추출
3. 백엔드 서버에서 키워드 추출 및 메인 질문 생성
4. 생성된 질문을 사용자에게 전달
5. 사용자 답변 수신
6. `question-evaluate`로 답변 평가 및 피드백 제공
7. `following-question-generate`로 꼬리질문 생성
8. 5-7 과정을 꼬리질문 횟수만큼 반복
9. 모든 질문 종료 후 `all-evaluate`로 전체 평가
10. 선택적으로 포트폴리오 완성도 평가

## 개발 가이드

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

## 배포

AWS EC2 인스턴스에 배포하는 방법:

1. EC2 인스턴스 생성 및 접속
2. 프로젝트 클론
3. 설치 스크립트 실행: `./scripts/install.sh`
4. 환경 변수 설정: `.env` 파일 작성
5. systemd 서비스 등록 및 실행

자세한 배포 가이드는 `deployment/deploy.md`를 참조하세요.

### 빠른 설치
```bash
git clone https://github.com/your-repo/forky_alongside-ai.git
cd forky_alongside-ai
./scripts/install.sh
cp env.example .env
nano .env
./scripts/start.sh
```

## 라이센스

MIT
