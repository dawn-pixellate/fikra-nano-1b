"""
Fikra Nano - Batch Processing
=============================
Process multiple questions efficiently.

Run: python examples/05_batch_processing.py
"""

from fikra import Fikra
import time

def main():
    print("🧠 Fikra Nano - Batch Processing\n")
    
    brain = Fikra()
    
    # Large batch of questions
    questions = [
        "What is 7 × 8?",
        "What is the capital of France?",
        "How many days are in a year?",
        "What is 100 - 37?",
        "Who invented the telephone?",
        "What is 5² (5 squared)?",
        "What is the boiling point of water?",
        "How many continents are there?",
        "What is 15% of 200?",
        "What is the speed of light?",
    ]
    
    print(f"Processing {len(questions)} questions...\n")
    
    start_time = time.time()
    results = []
    
    for i, question in enumerate(questions, 1):
        answer = brain.reason(question)
        results.append((question, answer))
        print(f"[{i}/{len(questions)}] {question}")
        print(f"    → {answer}\n")
    
    elapsed = time.time() - start_time
    avg_time = elapsed / len(questions)
    
    print("=" * 50)
    print(f"✅ Completed {len(questions)} questions in {elapsed:.2f}s")
    print(f"⚡ Average: {avg_time:.3f}s per question")
    print(f"🚀 Rate: {len(questions)/elapsed:.1f} questions/second")

if __name__ == "__main__":
    main()
