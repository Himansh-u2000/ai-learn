from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()


client = OpenAI(
    api_key=os.getenv("DO_API_KEY"),
    base_url="https://inference.do-ai.run/v1"  
)

# FEW shot prompting -> Direct prompt and few example how llm should answer user quesries
SYSTEM_PROMPT = '''
You are a expert  Coding with 20 years of experience and answer all the question is easy understandable manner. 
You does not answer any question other than Coding related questions and answer. 
simply tell user that You cannot answer this Question

examples: 
Q: Can You answer about AI in Moderen World
Ans. Sorry, I cannot anser that!

Q: Write a code to print hello world in pythonx 
Ans. print("hellp world")

# Q: How to solve Maths problem using python ? 
# Ans. Sorry, I cannot answr that!
'''


response = client.chat.completions.create(
    model = "openai-gpt-oss-120b",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "How to solve Maths problem using python ? "}
    ]
)

print(response.choices[0].message.content)