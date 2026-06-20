from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()


client = OpenAI(
    api_key=os.getenv("DO_API_KEY"), base_url="https://inference.do-ai.run/v1"
)

# COT shot prompting ->
SYSTEM_PROMPT = """
You answer question related to coding and assist user to debug error.
only answer questions related of coding. 
Do not answer questions which are not related to coding.

Answer all the questions in one of 3 phases. start or plan or output, always return in one of such phase.
if user is in no phase than answer in start phase and end. if user asks in start phase than answer in plan phase and write correct plan. if user asks in plan phase than answer in output phase


OUTPUT FORMAT:
{"mode" : "start" | "plan" | "output", "content": "string"}

EXAMPLE:
Q: How to Solve Quardatic Equation
Answer: 
{"output" : "output", "content": "I can only assist with coding-related questions."}

Q: How to Write code of factorial of 10
Answer: 
{"mode": "output", "content": "
n = 3
fact
for i in range(0, n+1):
    fact *= i
    
print(fact)
"}

EXAMPLE OUTPUTS:

{"mode" : "start", "content": "user want to answer me How to Write code of factorial of 3"}

{"mode": "plan", "content": "I will write Python code to solve factorial Question"}

{"mode": "output", "content": "print("Hello World!")"}
git 
"""

payload = [{"role": "system", "content": SYSTEM_PROMPT}]

print("-"*40)
messageInput = input("What can I help You with! ")

payload.append({"role": "user", "content": {"mode": "start", "content": messageInput}})

i = 0
while True:
    try: 
        response = client.chat.completions.create(
            model="openai-gpt-oss-120b", messages=payload
        )
        rawOutput = (response.choices[0].message.content)
        processedOutput = json.loads(rawOutput)
        # print(rawOutput)
        print(processedOutput)  
        
    except:
        print("model does not return json data")
        break
    
    payload.append({"role": "assistant", "content": processedOutput})
    
    if(processedOutput["mode"] == "output"):
        break
    print(i)
    i += 1