import os
import argparse
#from openai_chat import OpenAIChatTool
from chat.tools.openai_chat import OpenAIChatTool

def main():
    parser = argparse.ArgumentParser(description='OpenAI Chat CLI for Chatbot')
    parser.add_argument('--api-key', help='OpenAI API Key (or set OPENAI_API_KEY env variable)')
    parser.add_argument('--model', default='gpt-4o-mini', help='OpenAI model to use (default: gpt-4)')
    parser.add_argument('--system-prompt', help='System prompt to guide the model')
    args = parser.parse_args()

    # Get API key from args or environment variable
    api_key = args.api_key or os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OpenAI API key is required. Provide it via --api-key or OPENAI_API_KEY environment variable.")
        return

    # Initialize the chat tool
    chat_tool = OpenAIChatTool(api_key=api_key, model=args.model)
    tool = chat_tool.create_chat_tool()

    print("Welcome to the AI Chatbot!")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("Type 'clear' to clear the conversation history.")
    print("-" * 50)

    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("\nGoodbye!")
                break
            elif user_input.lower() == 'clear':
                print("\nConversation history cleared.")
                continue
            
            # Get response from OpenAI
            response = tool.func(
                message=user_input,
                system_prompt=args.system_prompt
            )
            
            if 'error' in response:
                print(f"\nError: {response['error']}")
            else:
                print(f"\nAssistant: {response['response']}")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main() 