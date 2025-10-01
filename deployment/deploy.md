# AWS EC2 배포 가이드

## 사전 준비

1. AWS EC2 인스턴스 생성 (Ubuntu 22.04 LTS 권장)
2. 보안 그룹에서 8000 포트 개방
3. SSH 접속 준비

## 배포 단계

### 1. 서버 접속 및 기본 패키지 설치

```bash
ssh -i your-key.pem ubuntu@your-ec2-ip

sudo apt update
sudo apt install -y git python3-pip
```

### 2. UV 설치

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
```

### 3. 프로젝트 클론

```bash
cd ~
git clone https://github.com/your-repo/forky_alongside-ai.git
cd forky_alongside-ai
```

### 4. 환경 변수 설정

```bash
cp env.example .env
nano .env
```

필수 환경 변수를 입력합니다:
- UPSTAGE_API_KEY
- UPSTAGE_DOCUMENT_API_KEY
- 기타 필요한 설정

### 5. 의존성 설치

```bash
uv sync
```

### 6. 서비스 등록

```bash
sudo cp deployment/forky.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable forky
sudo systemctl start forky
```

### 7. 서비스 상태 확인

```bash
sudo systemctl status forky
```

### 8. 로그 확인

```bash
sudo journalctl -u forky -f
```

## 서비스 관리 명령어

```bash
sudo systemctl start forky
sudo systemctl stop forky
sudo systemctl restart forky
sudo systemctl status forky
```

## 업데이트 방법

```bash
cd ~/forky_alongside-ai
git pull
uv sync
sudo systemctl restart forky
```

## 방화벽 설정 (선택사항)

```bash
sudo ufw allow 8000/tcp
sudo ufw enable
```

## Nginx 리버스 프록시 설정 (선택사항)

Nginx를 사용하여 80/443 포트로 서비스하려면:

```bash
sudo apt install -y nginx
sudo nano /etc/nginx/sites-available/forky
```

내용:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

활성화:
```bash
sudo ln -s /etc/nginx/sites-available/forky /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 문제 해결

### 서비스가 시작되지 않는 경우

```bash
sudo journalctl -u forky -n 50
```

### 포트가 이미 사용 중인 경우

```bash
sudo lsof -i :8000
sudo kill -9 <PID>
```

