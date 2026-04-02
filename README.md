# HW2 - Tieyuan Qian

## Description

This project builds a simple AI tool that generates customer support email replies using the Gemini API.

The goal is to help customer support staff respond to messages more efficiently and consistently.

---

## Workflow Description

- **User:** Customer support staff  
- **Input:** A customer message or complaint  
- **Output:** A polite and professional email reply  
- **Why it matters:** This task is repetitive and time-consuming, and AI can help improve efficiency and consistency  

---

## How It Works

- The user enters a customer message  
- The system sends the message with a prompt to the Gemini model  
- The model generates a reply  
- The reply is printed in the terminal  

---

## Files

- `app.py`: Python script that calls the Gemini API  
- `prompt.md`: prompt versions and improvements  
- `eval_set.md`: test cases for evaluation  
- `report.md`: explanation of approach and results  

---

## Commit Summary

- initial repository setup  
- add evaluation set  
- add llm api prototype  
- fix api and use new gemini sdk  
- add prompt iterations  
- add detailed report  

---

## How to Run

To run this project, you need a Gemini API key.

1. Get your API key from Google AI Studio.

2. Set the environment variable in your terminal:

For Windows (PowerShell):
$env:GEMINI_API_KEY="your_api_key_here"

3. Run the app:
python app.py


Note: The API key is not included in this repository for security reasons.

---

## Video

https://youtu.be/yYrwy9cDiQY