import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Check if OPENAI_API_KEY is set
if not os.getenv('OPENAI_API_KEY'):
    print("Error: OPENAI_API_KEY environment variable is not set")
    sys.exit(1)

# Add the src directory to Python path
src_path = str(Path(__file__).parent / "src")
sys.path.insert(0, src_path)

from chat.tools.chat_cli import main

if __name__ == "__main__":
    main() 