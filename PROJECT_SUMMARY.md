# Project Summary

## Forky AI Interview Server

포트폴리오 기반 AI 면접 연습 시스템

### 핵심 기능

1. Document Parsing: PDF 포트폴리오를 HTML로 변환
2. Keyword Extraction: AI 기반 키워드 자동 추출
3. Question Generation: 포트폴리오 기반 면접 질문 생성
4. Answer Evaluation: 실시간 답변 평가 및 피드백
5. Following Questions: 답변 기반 꼬리질문 생성
6. Overall Evaluation: 전체 면접 결과 종합 평가
7. Portfolio Assessment: 포트폴리오 완성도 평가

### 기술 스택

- Framework: FastAPI
- LLM: Upstage Solar Pro2
- Document Engine: Upstage Document Parsing
- Logging: Langfuse
- Package Manager: UV
- Python: 3.10+

### 프로젝트 구조

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
└── docs/                    # 문서
    ├── README.md
    ├── QUICKSTART.md
    ├── API_DOCUMENTATION.md
    ├── CHANGELOG.md
    └── PROJECT_SUMMARY.md

```

### API 엔드포인트

- POST /api/v1/documents/parse - PDF → HTML 변환
- POST /api/v1/keywords/extract - 키워드 추출
- POST /api/v1/questions/generate - 메인 질문 생성
- POST /api/v1/questions/following - 꼬리질문 생성
- POST /api/v1/questions/evaluate - 답변 평가
- POST /api/v1/evaluate/all - 전체 면접 평가
- POST /api/v1/evaluate/portfolio - 포트폴리오 평가
- GET /api/v1/health - 헬스 체크

### 특징

- RESTful API 설계
- 자동 API 문서 생성 (Swagger UI)
- CORS 지원
- 요청 처리 시간 로깅
- LLM 호출 추적 (Langfuse)
- 환경 변수 기반 설정
- 배포 자동화 스크립트
- systemd 서비스 지원

### 개발 워크플로우

1. 사용자가 PDF 포트폴리오 업로드
2. 문서 파싱 및 키워드 추출
3. AI가 면접 질문 생성
4. 사용자 답변 수신
5. 답변 평가 및 피드백
6. 꼬리질문 생성 및 반복
7. 전체 면접 결과 평가
8. 포트폴리오 완성도 평가

### 배포 환경

- 개발: localhost:8000
- 프로덕션: AWS EC2 + systemd
- 옵션: Nginx 리버스 프록시

### 문서

- README.md: 전체 가이드
- QUICKSTART.md: 5분 시작 가이드
- API_DOCUMENTATION.md: API 상세 문서
- deployment/deploy.md: AWS EC2 배포
- CHANGELOG.md: 버전 히스토리

### 테스트

- test_server.py: 헬스 체크
- examples/simple_workflow.py: 전체 워크플로우
- scripts/test.sh: 자동화 테스트

### 라이센스

MIT License

### 버전

0.1.0 (2025-10-01)

