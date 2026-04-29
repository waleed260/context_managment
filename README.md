🧠 RunContextWrapper Example (Agents + Gemini API)

This project demonstrates how to use RunContextWrapper from the agents framework to pass structured context (like user information) into an AI agent.
The agent uses a Gemini model (gemini-2.5-flash) and a function tool that accesses contextual data (name, age, UID) provided at runtime.

🚀 Features

Uses Gemini API through the AsyncOpenAI client.

Demonstrates context injection with RunContextWrapper.

Shows how to create tools that can access runtime context data.

Fully synchronous run example using Runner.run_sync.

Clean and modular structure using pydantic and dotenv.

📂 Project Structure
RunContextWrapper/
│
├── main.py              # Main program file (agent + context logic)
├── .env                 # Environment file (contains API key and base URL)
└── README.md            # Documentation

⚙️ Requirements

Make sure you have Python 3.10+ installed.
Then install the dependencies:

pip install rich python-dotenv pydantic


If you’re using a custom agents framework, ensure it includes:

Agent

Runner

RunContextWrapper

function_tool

OpenAIChatCompletionsModel

AsyncOpenAI

🔑 Environment Variables

Create a .env file in the project root and add:

GEMINI_API_KEY=your_api_key_here
BASE_URL=https://your_gemini_base_url_here

🧩 Code Overview
1. Define Context Model
class UserInfo(BaseModel):
    name: str
    age: int
    uid: int


Defines structured user information that the agent can access at runtime.

2. Create a Function Tool
@function_tool
def fetch_user_age_name(wrapper: RunContextWrapper[UserInfo]):
    """Fetch name, age, and UID from the context."""
    return f"{wrapper.context.name, wrapper.context.age, wrapper.context.uid}"


This function tool retrieves data from the runtime context passed via RunContextWrapper.

3. Build and Run the Agent
user_info = UserInfo(name="John", age=47, uid=123)

coach = Agent[UserInfo](
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=llm_model,
    tools=[fetch_user_age_name],
)

res = Runner.run_sync(
    coach,
    input="What is the age, name, and UID?",
    context=user_info,
)
print(res.final_output)
✅ Expected Output

('John', 47, 123)

💡 How It Works

The UserInfo object acts as the context.

RunContextWrapper gives the tool access to this context inside the function.

The Agent uses the provided tool and context to generate responses dynamically.

The Runner executes the agent synchronously and prints the final output.

🧠 Example Use Case

You can extend this concept to:

Pass user preferences or chat session state dynamically.

Build personalized assistants that remember user profiles.

Integrate context-aware function calls in multi-agent systems.

🧾 License

This project is for educational and demonstration purposes only.
Use responsibly and ensure your API keys remain private.

