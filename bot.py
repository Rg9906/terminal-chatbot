import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


SYSTEM_PROMPT = """
You are a blunt but supportive college senior.
You speak casually, without emojis.
You explain things clearly and honestly.
You don’t sugarcoat, but you care.
"""

print("AI Chatbot started. Type 'exit' to quit.")

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Alright. I’m out.")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content
    print("Bot:", reply)

    messages.append({"role": "assistant", "content": reply})
