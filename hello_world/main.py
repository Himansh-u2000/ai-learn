from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DO_API_KEY"),
    base_url="https://inference.do-ai.run/v1"  
)

response = client.chat.completions.create(
    model = "openai-gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a expert  Physiotherapist with 20 years of experience and answer all the question is easy understandable manner. You does not answer any question other than Physiotherapist related questions and answer. Even user asks about health disease related questions which are not related to physiotherapy then don't answer them. simple tell user that You cannot answer this Question"},
        {"role": "user", "content": "What should we do if i get fracture in leg"}
    ]
)

print(response.choices[0].message.content)