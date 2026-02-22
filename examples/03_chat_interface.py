"""
Fikra Nano - Chat Interface
===========================
A simple terminal-based chatbot using Fikra.

Run: python examples/03_chat_interface.py
"""

from fikra import Fikra

def main():
    print("🧠 Fikra Nano - Chat Interface")
    print("=" * 50)
    print("Type 'exit' or 'quit' to end the conversation\n")
    
    brain = Fikra()
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for exit
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\nFikra: Goodbye! 👋")
            break
        
        # Skip empty input
        if not user_input:
            continue
        
        # Get Fikra's response
        try:
            response = brain.reason(user_input)
            print(f"Fikra: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
