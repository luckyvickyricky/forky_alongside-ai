# Changelog

## [0.1.0] - 2025-10-01

### Added

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

### Features

- Upstage Solar Pro2 LLM 통합
- Upstage Document Parsing 엔진 사용
- FastAPI 기반 RESTful API
- 환경 변수 기반 설정 관리
- 자동 API 문서 생성 (Swagger UI, ReDoc)

### Documentation

- README.md: 전체 프로젝트 가이드
- API_DOCUMENTATION.md: 상세 API 문서
- QUICKSTART.md: 빠른 시작 가이드
- deployment/deploy.md: AWS EC2 배포 가이드
- CHANGELOG.md: 변경 이력

### Scripts

- scripts/install.sh: 자동 설치 스크립트
- scripts/dev.sh: 개발 서버 실행
- scripts/start.sh: 프로덕션 서버 실행
- scripts/test.sh: 서버 테스트

### Examples

- examples/simple_workflow.py: 전체 워크플로우 예제
- test_server.py: 서버 헬스 체크 테스트

