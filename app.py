import os
from google import genai

PROMPT_TEMPLATE = """
You are a customer support assistant.
Write a polite, professional, and concise email reply to the customer message below.
Clearly acknowledge the customer's issue, explain the next step, and avoid making promises you cannot verify.
If the issue involves legal, medical, or safety concerns, recommend escalation to a human support specialist.

Customer message:
{customer_message}
"""

def generate_reply(customer_message: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY environment variable.")

    client = genai.Client(api_key=api_key)

    prompt = PROMPT_TEMPLATE.format(customer_message=customer_message)

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
    )

    return response.text.strip()

if __name__ == "__main__":
    user_input = input("Enter customer message:\n")
    reply = generate_reply(user_input)

    print("\n=== Generated Reply ===\n")
    print(reply)