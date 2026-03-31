# Report

## Overview

This project builds a simple AI tool that generates customer support email replies using a large language model (Gemini).

The goal is to help customer support staff respond to customer messages faster and more consistently. The system takes a customer message as input and generates a polite and professional reply.

---

## Approach

I used a prompt-based approach to guide the model. The program is written in Python and calls the Gemini API.

The workflow is simple:
- The user enters a customer message
- The system sends the message with a prompt to the model
- The model generates an email reply
- The reply is printed in the terminal

This design is easy to use and shows how AI can support everyday business writing tasks.

---

## Prompt Iteration

I started with a simple prompt:

"Write a polite and professional email reply."

However, this version often produced replies that were too general and not very helpful.

In Revision 1, I added instructions to clearly acknowledge the customer's issue and explain the next step. This made the replies more structured and useful.

In Revision 2, I added instructions to avoid making promises that cannot be verified. I also added a rule for high-risk cases, such as legal or safety issues, where the system should suggest escalation to a human agent.

These changes improved both the clarity and safety of the responses.

---

## Evaluation

I tested the system using several cases, including normal customer questions, short inputs, vague messages, and high-risk situations.

### What worked well

The system can generate polite and professional responses. It works well for common cases like refunds, delays, and product questions.

The improved prompts made the replies more clear and more helpful. The model was better at explaining next steps after prompt revisions.

### Limitations

Some responses are still generic. The system may not fully understand vague messages without more context.

High-risk cases are still difficult. The model can give a reasonable answer, but human review is still necessary.

---

## Challenges

One major challenge was working with the Gemini API.

At first, I used a newer model (gemini-2.0-flash), but I often received errors related to quota limits. The system returned messages like "RESOURCE_EXHAUSTED" or "quota exceeded."

I tried different solutions:
- Waiting a few minutes before running the program again
- Switching to a lighter model such as gemini-1.5-flash or gemini-1.5-flash-8b
- Reducing the number of test runs

These steps helped reduce the problem, but the free API still has limits. This showed that even simple applications need to consider API constraints.

---

## Reflection

One thing I learned from this assignment is that prompt design is very important. Small changes in wording can significantly change the output.

I liked how quickly the model can generate useful responses. It can save time for repetitive tasks.

However, I also found it surprising that the system is not fully reliable. It still needs human review, especially for unclear or sensitive cases.

Overall, this tool is useful for drafting responses, but it should be used as a support tool rather than a replacement for human judgment.