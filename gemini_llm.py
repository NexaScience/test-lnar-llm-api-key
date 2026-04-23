import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello! Please introduce yourself briefly.",
)

print(response.text)
u = response.usage_metadata
print(f"\n[tokens] input: {u.prompt_token_count}, output: {u.candidates_token_count}, total: {u.total_token_count}")
