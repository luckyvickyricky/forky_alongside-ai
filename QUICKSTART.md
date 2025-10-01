# Quick Start Guide

5분 안에 Forky AI Interview Server를 실행하세요.

## 1. 설치

```bash
git clone https://github.com/your-repo/forky_alongside-ai.git
cd forky_alongside-ai
./scripts/install.sh
```

## 2. 환경 설정

```bash
cp env.example .env
nano .env
```

최소 필수 환경 변수:
```
UPSTAGE_API_KEY=your_key_here
UPSTAGE_DOCUMENT_API_KEY=your_key_here
```

## 3. 서버 실행

개발 모드:
```bash
./scripts/dev.sh
```

프로덕션 모드:
```bash
./scripts/start.sh
```

## 4. 확인

브라우저에서:
- API 문서: http://localhost:8000/api/docs
- 헬스 체크: http://localhost:8000/api/v1/health

## 5. 첫 API 호출

```bash
curl http://localhost:8000/api/v1/health
```

## 6. 워크플로우 테스트

서버가 실행 중인 상태에서:
```bash
uv run python examples/simple_workflow.py
```

## 문제 해결

### 포트가 이미 사용 중
```bash
lsof -i :8000
kill -9 <PID>
```

### 환경 변수 오류
`.env` 파일이 올바르게 설정되었는지 확인하세요.

### 의존성 오류
```bash
uv sync
```

## 다음 단계

- API 문서: `API_DOCUMENTATION.md` 참고
- 배포: `deployment/deploy.md` 참고
- 전체 문서: `README.md` 참고

## 지원

문제가 있으면 이슈를 등록해주세요.

