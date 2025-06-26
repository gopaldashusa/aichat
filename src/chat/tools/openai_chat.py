from typing import Optional, Dict, Any, Callable
import openai
from openai import OpenAIError, AuthenticationError, BadRequestError

class Tool:
    def __init__(self, name: str, description: str, func: Callable):
        self.name = name
        self.description = description
        self.func = func

class OpenAIChatTool:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        """
        Initialize the OpenAI Chat Tool.
        
        Args:
            api_key (str): OpenAI API key
            model (str): Model to use for chat (default: gpt-4o-mini)
        """
        self.api_key = api_key
        self.model = model
        self.client = openai.OpenAI(api_key=api_key)

    def create_chat_tool(self) -> Tool:
        """
        Create a Tool for OpenAI chat interactions.
        
        Returns:
            Tool: A Tool instance for chat interactions
        """
        return Tool(
            name="OpenAI Chat",
            description="A tool for interacting with OpenAI's chat model to discuss and refine content.",
            func=self._chat_with_openai
        )

    def _chat_with_openai(
        self,
        message: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> Dict[str, Any]:
        """
        Send a message to OpenAI's chat model and get a response.
        
        Args:
            message (str): The user's message
            system_prompt (Optional[str]): System prompt to guide the model's behavior
            temperature (float): Controls randomness (0.0 to 1.0)
            max_tokens (int): Maximum number of tokens in the response
            
        Returns:
            Dict[str, Any]: The model's response
        """
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": message})

            # Map the model name to the correct API model name
            api_model = self._get_api_model_name(self.model)

            response = self.client.chat.completions.create(
                model=api_model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )

            return {
                "response": response.choices[0].message.content,
                "usage": response.usage,
                "model": response.model
            }
        except AuthenticationError:
            return {
                "error": "Authentication failed. Please check your API key.",
                "response": None,
                "usage": None,
                "model": self.model
            }
        except BadRequestError as e:
            return {
                "error": f"Invalid request: {str(e)}",
                "response": None,
                "usage": None,
                "model": self.model
            }
        except OpenAIError as e:
            return {
                "error": f"OpenAI API error: {str(e)}",
                "response": None,
                "usage": None,
                "model": self.model
            }
        except Exception as e:
            return {
                "error": f"An unexpected error occurred: {str(e)}",
                "response": None,
                "usage": None,
                "model": self.model
            }

    def _get_api_model_name(self, model: str) -> str:
        """
        Map the model name to the correct API model name.
        
        Args:
            model (str): The model name to map
            
        Returns:
            str: The correct API model name
        """
        model_mapping = {
            "gpt-4o-mini": "gpt-4",  # Map to standard GPT-4 if mini is not available
            "gpt-4": "gpt-4",
            "gpt-3.5-turbo": "gpt-3.5-turbo"
        }
        return model_mapping.get(model, "gpt-4")  # Default to gpt-4 if model not found

# Example usage:
"""
from chat.tools.openai_chat import OpenAIChatTool

# Initialize the tool
chat_tool = OpenAIChatTool(api_key="your-api-key")

# Create the Tool
tool = chat_tool.create_chat_tool()

# Use the tool
response = tool.func(
    message="Help me write a user story for a login feature",
    system_prompt="You are an expert in writing user stories and acceptance criteria."
)
""" 