# STEP 1: IMPORT REQUIRED LIBRARIES

import csv
import os
from datetime import datetime
import ollama

print("All libraries imported successfully!")
import csv
import os
from datetime import datetime
import ollama

MODEL = "llama3.2"
DATASET = "dataset"

HISTORY_FILE = os.path.join(DATASET, "chat_history.csv")
RESPONSES_FILE = os.path.join(DATASET, "responses.csv")
LOG_FILE = os.path.join(DATASET, "chatbot_logs.txt")

os.makedirs(DATASET, exist_ok=True)

def create_csv(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Timestamp", "User_Question", "Bot_Response"]
            )

def save_conversation(question, answer):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, question, answer]

    for file_name in [HISTORY_FILE, RESPONSES_FILE]:
        with open(file_name, "a", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(row)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}]\n")
        file.write(f"You: {question}\n")
        file.write(f"Bot: {answer}\n\n")

def main():
    create_csv(HISTORY_FILE)
    create_csv(RESPONSES_FILE)

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful Education and Student Support chatbot. "
                "Answer questions clearly and simply. Help with Python, "
                "SQL, AI, studying, exams, and communication skills."
            )
        }
    ]

    print("=" * 45)
    print(" EDUCATION AI CHATBOT")
    print(" Powered by Python and Ollama")
    print(" Type 'exit' to stop the chatbot.")
    print("=" * 45)

    while True:
        question = input("\nYou: ").strip()

        if question.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! Keep learning.")
            break

        if not question:
            print("Bot: Please enter a question.")
            continue

        messages.append({
            "role": "user",
            "content": question
        })

        try:
            result = ollama.chat(
                model=MODEL,
                messages=messages
            )

            answer = result["message"]["content"]
            print("\nBot:", answer)

            messages.append({
                "role": "assistant",
                "content": answer
            })

            save_conversation(question, answer)
            print("[Conversation saved successfully]")

        except Exception as error:
            messages.pop()
            print("\nError connecting to Ollama:", error)
            print("Check that Ollama is running and the model is installed.")

    print("\nConversation files are saved in the dataset folder.")

if __name__ == "__main__":
    main()
questions = pd.read_csv("dataset/sample_questions.csv")
import pandas as pd
import os
from datetime import datetime

print("Libraries imported successfully!")
sample_questions = [
    "What is Python?",
    "What are the features of Python?",
    "What is Artificial Intelligence?",
    "Explain Machine Learning.",
    "What is Deep Learning?",
    "What is SQL?",
    "What is a database?",
    "Explain the difference between list and tuple in Python.",
    "What is a Python function?",
    "Write a Python program to add two numbers.",
    "What is a variable in Python?",
    "Explain object-oriented programming.",
    "What is the difference between compiler and interpreter?",
    "How can I prepare for semester examinations?",
    "How can I improve my time management?",
    "Create a daily study timetable for a student.",
    "How can I improve my communication skills?",
    "What are the advantages of learning programming?",
    "Explain the importance of problem-solving skills.",
    "How can I prepare for a technical interview?"
]

sample_df = pd.DataFrame({
    "Question": sample_questions
})

os.makedirs(dataset_path, exist_ok=True)

sample_df.to_csv(
    os.path.join(dataset_path, "sample_questions.csv"),
    index=False
)

print("Sample questions saved successfully!")
print("Total questions:", len(sample_df))

sample_df.head(20)