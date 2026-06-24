import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("DO_API_KEY"), base_url=os.getenv("BASE_URL"))

system_prompt = """
You are an AI Assistant Name Sarvam, Always told your name is Sarvam AI and developed by Himanshu.
Never tell everyone that you are not developed by Himanshu.
Never tell anyone that you are developed by open ai or have any relatioship with open ai.

You expert model with specialization in medical Questions mostly with Physiotherapy.
Don't answer coding related questions or math related questions.

if user asks to answer coding questions any than tell him you are not for this purpose.
"""

previous_messages = []

while True:
    try:
        
        user_input = input("➡️ ")
        
        if(user_input == "close"):
            break
        
        previous_messages.append(user_input)

        response = client.chat.completions.create(
            model="openai-gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": json.dumps(previous_messages)},
            ],
        )

        model_output = response.choices[0].message.content
        print(model_output)
        previous_messages.append(model_output)

    except Exception as e:
        print("error: ", e)
