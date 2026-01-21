# Workshop 1: Social Media Automation Pipeline

This project automates social media posting by connecting **Notion → OpenRouter → Mastodon**. It fetches content from a Notion page, uses an LLM to generate structured post ideas (caption, image prompt, hashtags), and posts to Mastodon.

---

## Features

1. **Fetch Notion Content**  
   - Pulls text from a Notion page using the Notion API.

2. **Generate Social Media Posts**  
   - Uses OpenRouter LLM to summarize Notion content and generate structured posts.
   - Output format:
   ```json
   {
     "caption": "Engaging caption here",
     "image_prompt": "Description for image generation",
     "hashtags": "#food #coffee #daily"
   }
   ```

3. **Post to Mastodon**
   - Posts generated content to a Mastodon account.
   - Ensures character limits are respected (500 chars max).

---

## Project Structure

```
workshop1/
├── main.py                # Entry point: runs the full pipeline
├── config.py              # Loads .env API keys and configuration
├── notion.py              # Fetches Notion page content
├── openrouter.py          # Summarizes and generates structured social media posts
├── mastodon_posting.py    # Posts to Mastodon
├── test_*.py              # Optional test scripts
├── .gitignore             # Ignores cache, .env, virtual environments
├── .env.example           # Template for API keys
├── pyproject.toml         # Project and dependency configuration
├── uv.lock                # Locked dependency versions
└── README.md              # This file
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/workshop-1-social-automation.git
cd workshop-1-social-automation/workshop1
```

### 2. Install dependencies

```bash
uv install
```

### 3. Configure environment variables

- Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

- Fill in your API keys for:
  - **OpenRouter** (OPENROUTER_API_KEY)
  - **Mastodon** (MASTODON_BASE_URL, MASTODON_ACCESS_TOKEN)
  - **Notion** (NOTION_API_KEY, NOTION_PAGE_ID)

**Important**: `.env` is ignored by Git to keep your keys safe.

---

## Usage

### Run the full pipeline

```bash
uv run python main.py
```

This will:
1. Pull content from your Notion page
2. Generate a structured post via OpenRouter
3. Print the generated post (dry-run mode by default)
4. Post to Mastodon (set `dry_run=False` in `main.py` to actually post)

### Run tests

```bash
uv run python test_notion.py
uv run python test_openrouter.py
uv run python test_mastodon.py
```

---

## Configuration

### Key Settings

- **OPENROUTER_MODEL**: Default is `openai/gpt-4o-mini` (set in config.py)
- **Max caption length**: 500 characters (enforced in openrouter.py)
- **Max Notion input**: 2000 characters (~500 tokens) to avoid token limits
- **Dry-run mode**: Set to `True` by default for safe testing

---

## Notes

- Notion page content is automatically truncated to avoid LLM token limits
- All posts are limited to 500 characters to meet Mastodon constraints
- The pipeline generates both a caption and an image prompt (image generation not implemented)
- Use `dry_run=True` for testing before posting live

---

## Troubleshooting

### Token limit errors
- Reduce `MAX_INPUT_CHARS` in `openrouter.py` (currently 2000)
- Or use a model with larger context window via `OPENROUTER_MODEL`

### Function name errors
- Ensure you're using `get_page_content()` from `notion.py`
- Not `fetch_notion_page()` (old name)

### Mastodon posting fails
- Verify your `MASTODON_ACCESS_TOKEN` and `MASTODON_BASE_URL` in `.env`
- Check that your token has write permissions

---

## License

MIT License - feel free to use and modify as needed!
