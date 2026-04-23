import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello! Please introduce yourself briefly."},
    ],
)

print(message.content[0].text)
print(f"\n[tokens] input: {message.usage.input_tokens}, output: {message.usage.output_tokens}, total: {message.usage.input_tokens + message.usage.output_tokens}")
