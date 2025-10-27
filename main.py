

from agents import Agent , Runner, OpenAIChatCompletionsModel, AsyncOpenAI , set_tracing_disabled , RunContextWrapper, function_tool
from dataclasses import dataclass
import asyncio
import os
from rich import print
from dotenv import load_dotenv

from pydantic import BaseModel

load_dotenv()






set_tracing_disabled(True)


key = os.getenv("GEMINI_API_KEY")
url = os.getenv("BASE_URL")


Gemini_client =AsyncOpenAI(api_key=key , base_url =url)
llm_model = OpenAIChatCompletionsModel(model = "gemini-2.5-flash", openai_client=Gemini_client)
  



# Define a simple context using a dataclass

class UserInfo(BaseModel):
     
    name: str
    age : int
    uid: int

# A tool function that accesses local context via the wrapper
@function_tool
def fetch_user_age_name ( wrapper:RunContextWrapper[UserInfo]):
    """instruction = name,age ,uid function tool"""
    return f" {wrapper.context.name,wrapper.context.age,wrapper.context.uid} "

 

user_info = UserInfo(name="John", age = 47, uid =123 )  

    # Define an agent that will use the tool above
coach= Agent[UserInfo](  
        name="Assistant",
        instructions="you are a helpful assistant.",
        model=llm_model,
        tools=[fetch_user_age_name],)

    # Run the agent, passing in the local context
res =Runner.run_sync(coach,input="what is age and name ,uid  ",context=user_info,
    )
print(res.final_output)  # Expected output: The user John is 47 years old.

# if __name__ == "__main__":
#     (main())


