# test-lnar-llm-api-key

Lnar のテスト用リポジトリです。OpenAI / Anthropic / Gemini の各 API キーを使って LLM を実行するサンプルコードを管理します。

## ファイル構成

| ファイル | 説明 |
|---|---|
| `openai_llm.py` | OpenAI API (gpt-4o) を使って LLM を実行するサンプル |
| `anthropic_llm.py` | Anthropic API (claude-sonnet-4-6) を使って LLM を実行するサンプル |
| `gemini_llm.py` | Gemini API (gemini-2.0-flash) を使って LLM を実行するサンプル |

## セットアップ

```bash
python3 -m venv .venv
.venv/bin/pip install openai anthropic google-genai python-dotenv
```

`.env` ファイルを作成し、各 API キーを設定してください。

```
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
GEMINI_API_KEY=your-gemini-api-key
```

## 実行

```bash
.venv/bin/python3 openai_llm.py
.venv/bin/python3 anthropic_llm.py
.venv/bin/python3 gemini_llm.py
```
