import random
questions = [
    {
        "question": "What is the capital f nepal?",
        "options": ["A) baglung", "B) kathmandu", "C) birjung"],
        "answer": "B"
    },
    {
        "question": "what is the currency of nepal?",
        "options": ["A) IC", "B) USD", "C) rupee"],
        "answer": "C"
    },
    {
        "question": "Who is the prime minister of Nepal?",
        "options": ["A) ser bahadur", "B) prachanda", "C) kp oli"],
        "answer": "C"
    }
]
score = 0
def quiz(questions):
    random.shuffle(questions)
    for x in questions:
        print(x["question"])
        for y in x["options"]:
            print(y)
        answer=input("enter your answer:").strip().upper()
        if answer==x["answer"]:
            score += 1
            print("right")
        else:
            print('wrong')
quiz(questions)




