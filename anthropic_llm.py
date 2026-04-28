import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=[{
        "type": "text",
        "text": "You are a helpful assistant.",
        "cache_control": {"type": "ephemeral"},
    }],
    messages=[
        {"role": "user", "content": "Hello! Please introduce yourself briefly."},
    ],
)

print(response.content[0].text)
u = response.usage
print(f"\n[tokens] input: {u.input_tokens}, output: {u.output_tokens}, total: {u.input_tokens + u.output_tokens}")
print(f"[cache] created: {u.cache_creation_input_tokens}, read: {u.cache_read_input_tokens}")
