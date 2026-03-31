# Evaluation Set

## Case 1: Normal Case
**Input:**  
Hello, I received the wrong item in my order. I ordered a blue notebook, but I got a black one. Can you help me exchange it?

**What a good output should do:**  
The reply should apologize, acknowledge the mistake, explain the exchange process clearly, and keep a polite and professional tone.

---

## Case 2: Normal Case
**Input:**  
Hi, my package has not arrived yet, and the tracking page has not updated in three days. Could you check on this for me?

**What a good output should do:**  
The reply should show empathy, explain that the delay will be checked, and give the customer a clear next step.

---

## Case 3: Edge Case
**Input:**  
I want a refund.

**What a good output should do:**  
The reply should remain polite even though the message is very short. It should ask for the needed order details and explain the next step clearly.

---

## Case 4: Human Review / High-Risk Case
**Input:**  
Your product caused a serious allergic reaction and I may take legal action if this is not resolved immediately.

**What a good output should do:**  
The reply should stay calm and professional, avoid admitting legal responsibility, show concern, and recommend escalation to a human support specialist.

---

## Case 5: Likely Failure / Vague Case
**Input:**  
I am unhappy with what happened last time and I want this fixed now.

**What a good output should do:**  
The reply should acknowledge the frustration, avoid making assumptions, and ask for more details before offering a solution.