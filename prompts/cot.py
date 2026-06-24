from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()


client = OpenAI(
    api_key=os.getenv("DO_API_KEY"), base_url=os.getenv("")
)

# COT shot prompting ->
SYSTEM_PROMPT = """
You answer question related to coding and assist user to debug error.
only answer questions related of coding. 
Do not answer questions which are not related to coding.


You are an AI assistant.

Workflow:

1. If user sends a normal question:
   Return:
   {"mode":"start","content":"..."}

2. If previous assistant mode was start:
   Return:
   {"mode":"plan","content":"..."}

3. If previous assistant mode was plan:
   Return:
   {"mode":"output","content":"..."}

Always return valid JSON only


OUTPUT FORMAT:
{"mode" : "start" | "plan" | "output", "content": "string"}

EXAMPLE OUTPUTS:

{"mode" : "output", "content": "I can only assist with coding-related questions."}

{"mode":"output","content":"n = 3\nfact = 1\nfor i in range(1,n+1):\n    fact *= i\nprint(fact)"}

{"mode" : "start", "content": "user want to answer me How to Write code of factorial of 3"}

{"mode": "plan", "content": "I will write Python code to solve factorial Question"}

{"mode": "plan", "content": "Java is better than python for user type safety so maybe we should use java code"}

{"mode": "output", "content": ""}
"""

payload = [{"role": "system", "content": SYSTEM_PROMPT}]

print("-"*40)

messageInput = input("➡️ ")

payload.append({"role": "user",  "content": messageInput})


i = 0
while True:
    try: 
        response = client.chat.completions.create(
            model="openai-gpt-oss-120b", messages=payload
        )
        rawOutput = response.choices[0].message.content
        # print(rawOutput)
        
        processedOutput = json.loads(rawOutput)
        
        if processedOutput['mode'] == "start":
            print("🔥", processedOutput["content"])
        elif processedOutput['mode'] == "plan":
            print("🧠 ", processedOutput["content"])
        else :
            print("🟰 ",processedOutput["content"])  
        
        
        
    except Exception as e:
        print("\nERROR:")
        print(e)
        break
    
    payload.append({"role": "assistant", "content": json.dumps(processedOutput)})
    
    if(processedOutput["mode"] == "output"):
        break
    print(i)
    i += 1