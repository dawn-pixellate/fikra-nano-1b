"""
Fikra Nano - Code Helper
========================
Examples of using Fikra to help with coding tasks.

Run: python examples/04_code_helper.py
"""

from fikra import Fikra

def main():
    print("🧠 Fikra Nano - Code Helper\n")
    
    brain = Fikra()
    
    # Code-related questions
    tasks = [
        "Write a Python function to reverse a string",
        "How do I sort a list in Python?",
        "Write a function to check if a number is even",
        "Explain what a for loop does",
        "Write a Python function to calculate factorial",
    ]
    
    print("Coding assistance examples:\n")
    
    for i, task in enumerate(tasks, 1):
        print(f"Task {i}: {task}")
        print("-" * 50)
        response = brain.reason(task, max_tokens=256)
        print(response)
        print("\n")

if __name__ == "__main__":
    main()
