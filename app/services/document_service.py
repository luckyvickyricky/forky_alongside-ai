import requests
from app.core.config import settings


class DocumentService:
    def __init__(self):
        self.api_key = settings.upstage_document_api_key
        self.url = "https://api.upstage.ai/v1/document-digitization"
    
    def parse_pdf_to_html(self, file_path: str) -> dict:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        files = {"document": open(file_path, "rb")}
        data = {
            "ocr": "force",
            "base64_encoding": "['table']",
            "model": "document-parse"
        }
        
        response = requests.post(self.url, headers=headers, files=files, data=data)
        return response.json()
    
    def parse_pdf_bytes(self, file_bytes: bytes, filename: str) -> dict:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        files = {"document": (filename, file_bytes, "application/pdf")}
        data = {
            "ocr": "force",
            "base64_encoding": "[]",  # 빈 배열로 설정하여 base64 인코딩 비활성화
            "model": "document-parse"
        }
        
        response = requests.post(self.url, headers=headers, files=files, data=data)
        result = response.json()
        
        # 응답 데이터 정리: 불필요한 필드 제거
        if "metadata" in result and "elements" in result["metadata"]:
            for element in result["metadata"]["elements"]:
                # base64_encoding 필드가 있으면 제거
                if "base64_encoding" in element:
                    del element["base64_encoding"]
        
        return result


document_service = DocumentService()

