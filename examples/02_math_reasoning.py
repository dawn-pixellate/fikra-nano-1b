"""
Fikra Nano - Math Reasoning Examples
====================================
Demonstrates Fikra's mathematical reasoning capabilities.
Note: Fikra's math capabilities may be limited due to model size.

Run: python examples/02_math_reasoning.py
"""

from fikra import Fikra

def main():
    print("🧠 Fikra Nano - Math Reasoning\n")
    
    brain = Fikra()
    
    # Collection of math problems
    problems = [
        "What is 15 × 23?",
        "If a train travels 120 km in 2 hours, what is its speed in km/h?",
        "A rectangle has length 8 cm and width 5 cm. What is its area?",
        "If I have $50 and spend $18.50, how much do I have left?",
        "What is 25% of 80?",
        "If 3 apples cost $2.40, how much does 1 apple cost?",
    ]
    
    print("Solving math problems...\n")
    
    for i, problem in enumerate(problems, 1):
        print(f"Problem {i}: {problem}")
        answer = brain.reason(problem)
        print(f"Answer: {answer}\n")

if __name__ == "__main__":
    main()
