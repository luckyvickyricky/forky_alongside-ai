import requests
import sys


def test_health_endpoint():
    try:
        response = requests.get("http://127.0.0.1:8000/api/v1/health")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Health check: {data['status']}")
            print(f"Service: {data['service']}")
            print(f"Version: {data['version']}")
            print(f"Langfuse enabled: {data.get('langfuse_enabled', False)}")
            return True
        else:
            print(f"Health check failed with status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Failed to connect to server: {e}")
        return False


def test_root_endpoint():
    try:
        response = requests.get("http://127.0.0.1:8000/")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nRoot endpoint: {data['message']}")
            return True
        else:
            print(f"Root endpoint failed with status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Failed to connect to server: {e}")
        return False


if __name__ == "__main__":
    print("Testing Forky AI Interview Server...")
    print("=" * 50)
    
    health_ok = test_health_endpoint()
    root_ok = test_root_endpoint()
    
    print("=" * 50)
    
    if health_ok and root_ok:
        print("\nAll tests passed!")
        sys.exit(0)
    else:
        print("\nSome tests failed!")
        sys.exit(1)

