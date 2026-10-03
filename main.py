import os
from groq import Groq

# -----------------------------------
# 1. Connect to Groq
# -----------------------------------

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)


# -----------------------------------
# 2. Get input from user
# -----------------------------------

a = input("Enter the first number: ")
b = input("Enter the second number: ")


# -----------------------------------
# 3. Create prompt for the LLM
# -----------------------------------

prompt = f"""
The user entered two numbers.

First number: {a}
Second number: {b}

Understand the numbers even if they are written
as words or numbers.

Write a short 3-line story based on the given numbers.

Example:
If the user enters 5 and 2,
the story could say Rahul woke up at 5 o'clock
and completed homework for 2 subjects.
"""


# -----------------------------------
# 4. Send prompt to Groq
# -----------------------------------

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)


# -----------------------------------
# 5. Get AI response
# -----------------------------------

answer = response.choices[0].message.content


# -----------------------------------
# 6. Display result
# -----------------------------------

print("\n--- AI Generated Story ---")
print(answer)