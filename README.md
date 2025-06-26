# Chatapp

A command-line chatbot application that uses OpenAI's API to provide interactive AI conversations.

## Features

- Interactive command-line chat interface
- Support for different OpenAI models (GPT-4, GPT-3.5-turbo)
- Customizable system prompts
- Conversation history management
- Error handling and graceful exit

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <your-github-repo-url>
cd chatapp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your API key: `OPENAI_API_KEY=your-api-key-here`
   
   Or set it as an environment variable:
   ```bash
   export OPENAI_API_KEY=your-api-key-here
   ```

## Usage

Run the chatbot:
```bash
python run_chat.py
```

### Command-line options:
- `--api-key`: Specify OpenAI API key (optional if set in environment)
- `--model`: Choose OpenAI model (default: gpt-4o-mini)
- `--system-prompt`: Set a system prompt to guide the model's behavior

### Examples:
```bash
# Basic usage
python run_chat.py

# With specific model
python run_chat.py --model gpt-3.5-turbo

# With system prompt
python run_chat.py --system-prompt "You are a helpful coding assistant."

# With custom API key
python run_chat.py --api-key your-api-key-here
```

### Chat Commands:
- Type your message and press Enter to chat
- Type `exit` or `quit` to end the conversation
- Type `clear` to clear conversation history

## Project Structure

```
chatapp/
├── run_chat.py          # Main entry point
├── requirements.txt     # Python dependencies
├── setup.py            # Package setup
├── .env                # Environment variables (create this)
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── src/
    └── chat/
        ├── __init__.py
        └── tools/
            ├── __init__.py
            ├── chat_cli.py      # CLI interface
            └── openai_chat.py   # OpenAI API integration
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License. 