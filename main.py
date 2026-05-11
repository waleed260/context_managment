

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
  




