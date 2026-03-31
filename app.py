import os
import google.generativeai as genai

PROMPT_TEMPLATE = """
You are a customer support assistant.
Write a polite, professional, and concise email reply to the customer message below.

Customer message:
{customer_message}
"""

def generate_reply(customer_message: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY environment variable.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = PROMPT_TEMPLATE.format(customer_message=customer_message)
    response = model.generate_content(prompt)

    return response.text.strip()

if __name__ == "__main__":
    user_input = input("Enter customer message:\n")
    reply = generate_reply(user_input)

    print("\n=== Generated Reply ===\n")
    print(reply)