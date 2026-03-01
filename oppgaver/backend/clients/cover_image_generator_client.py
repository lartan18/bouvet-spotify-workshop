import openai
from openai import AzureOpenAI
import os
import requests
import json

class CoverImageGeneratorClient:
    def __init__(self):
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        base_url = os.getenv("AZURE_OPENAI_BASE_URL")
        image_endpoint = os.getenv("AZURE_OPENAI_IMAGE_ENDPOINT")
        self.endpoint = f"{base_url}{image_endpoint}"

    def generate_image(self, prompt: str) -> str:
        try:            
            # Use Azure AI Foundry REST API
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            # TODO: 2.1 Fullfør payload med nødvendige parametere: "model": "gpt-image-1" og "prompt": med prompt-parameteren
            payload = {
                "prompt": prompt,# Placeholder, skal erstattes med prompt-parameteren
                "size": "1024x1024",
                "quality": "medium",
                "output_compression": 100,
                "output_format": "png",
                "n": 1,
                "model": "gpt-image-1"
            }
            
            # TODO: 2.1 Fullfør API-kallet: send til self.endpoint med payload i json-body           
            response = requests.post(
                self.endpoint, #Hvor skal vi sende requesten? Hint: kanskje i self?
                headers=headers,
                json=payload, #Hva skal vi sende i body? Hint: kanskje noe vi allerede har laget?
                timeout=60
            )
            result = response.json()
            
            # Azure AI Foundry returns base64 encoded image data
            b64_json = result.get("data", [{}])[0].get("b64_json")
            
            if b64_json:
                # Convert base64 to data URL for frontend display
                image_url = f"data:image/png;base64,{b64_json}"
                print(f"Successfully generated image (base64 data, length: {len(image_url)} chars)")
                return image_url
            else:
                print("ERROR: No b64_json in response")
                return None

        except requests.exceptions.RequestException as e:
            print(f"ERROR: Request failed: {type(e).__name__}: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"ERROR Response: {e.response.text}")
            return None
        except Exception as e:
            print(f"ERROR: Unexpected exception occurred: {type(e).__name__}: {str(e)}")
            return None
