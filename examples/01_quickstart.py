"""
Fikra Nano - Quickstart Example
================================
The simplest way to use Fikra for reasoning tasks.

Run: python examples/01_quickstart.py
"""

from fikra import Fikra

def main():
    print("🧠 Fikra Nano - Quickstart Example\n")
    
    # Initialize (downloads model on first run - ~700MB)
    print("Initializing Fikra...")
    brain = Fikra()
    print("✅ Ready!\n")
    
    # Example 1: Math reasoning
    print("--- Example 1: Math Reasoning ---")
    question = "If I have 15 apples and give 7 to my friend, how many do I have left?"
    print(f"Q: {question}")
    answer = brain.reason(question)
    print(f"A: {answer}\n")
    
    # Example 2: General knowledge
    print("--- Example 2: General Knowledge ---")
    question = "What is photosynthesis?"
    print(f"Q: {question}")
    answer = brain.reason(question)
    print(f"A: {answer}\n")
    
    # Example 3: Code generation
    print("--- Example 3: Code Helper ---")
    question = "Write a Python function to check if a number is prime"
    print(f"Q: {question}")
    answer = brain.reason(question)
    print(f"A: {answer}\n")

if __name__ == "__main__":
    main()
