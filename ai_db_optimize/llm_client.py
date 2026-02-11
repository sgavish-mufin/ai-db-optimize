import os
from typing import Optional
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

def get_optimization_report(prompt: str) -> Optional[str]:
    """
    Send the optimization prompt to OpenAI/OpenRouter and return the response.
    Returns None if API key is not configured or if an error occurs.
    """
    try:
        import requests
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("[ERROR] OPENAI_API_KEY not found in .env file")
            return None
        
        # Support both OpenAI and OpenRouter
        base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        
        url = f"{base_url}/chat/completions"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        data = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=60)
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            print(f"[ERROR] API returned status {response.status_code}")
            print(f"Response: {response.text}")
            return None
    
    except Exception as e:
        print(f"[ERROR] API error: {e}")
        return None
