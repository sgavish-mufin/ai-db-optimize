# AI DB Optimize

AI DB Optimize is a simple yet powerful CLI tool that uses Artificial Intelligence to analyze and optimize your SQL queries. It identifies performance anti-patterns and suggests optimized rewrites and indexing strategies tailored to your specific database dialect.

## Features

- **SQL Query Optimization**: Analyzes raw SQL queries for performance bottlenecks.
- **Dialect Support**: Supports multiple databases including PostgreSQL, MySQL, SQLite, and more.
- **AI-Powered Analysis**: Uses OpenAI/OpenRouter to provide detailed optimization reports.
- **Actionable Recommendations**: Provides optimized SQL rewrites and `CREATE INDEX` statements.

## Project Structure

```text
ai-db-optimize/
├── ai_db_optimize/      # Core package
│   ├── __init__.py
│   ├── __main__.py      # Package entry point
│   ├── main.py          # CLI definitions
│   ├── llm_client.py    # AI API integration
│   └── prompt_gen.py    # AI prompt logic
├── .env.example         # Template for environment variables
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
└── README.md            # You are here!
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sgavish-mufin/ai-db-optimize.git
   cd ai-db-optimize
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the environment**:
   Copy `.env.example` to `.env` and add your API key:
   ```bash
   cp .env.example .env
   ```
   Edit `.env`:
   ```env
   OPENAI_API_KEY=your_api_key_here
   OPENAI_BASE_URL=https://api.openai.com/v1
   OPENAI_MODEL=gpt-4
   ```

## Usage

Run the tool using the following command:

```bash
python ai_db_optimize --db <database_type> --query "<your_sql_query>"
```

### Example

```bash
python ai_db_optimize --db postgres --query "SELECT * FROM orders WHERE status = 'pending'"
```

## Technologies Used

- **Python**: Core application logic.
- **Typer**: CLI framework.
- **OpenAI/OpenRouter**: AI analysis engine.
- **Dotenv**: Environment variable management.
