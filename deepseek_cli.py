#!/Users/hrst/documentation/.venv/bin/python
import os
import sys
from deepseek_ai import DeepSeekAI

def main():
    if len(sys.argv) < 2:
        print("Usage: deepseek <prompt>")
        sys.exit(1)

    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        print("Error: DEEPSEEK_API_KEY environment variable not set")
        print("Please set your DeepSeek API key: export DEEPSEEK_API_KEY='your-key-here'")
        sys.exit(1)

    client = DeepSeekAI(api_key=api_key)
    prompt = " ".join(sys.argv[1:])

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 