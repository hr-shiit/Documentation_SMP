#!/Users/hrst/documentation/.venv/bin/python
import os
import sys
import anthropic
from dotenv import load_dotenv

load_dotenv()

def main():
    if len(sys.argv) < 2:
        print("Usage: claude <prompt>")
        sys.exit(1)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        print("Please set your Anthropic API key: export ANTHROPIC_API_KEY='your-key-here'")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    prompt = " ".join(sys.argv[1:])

    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        print(response.content[0].text)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 