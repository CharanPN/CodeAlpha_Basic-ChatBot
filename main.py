from datetime import datetime
import random

def replies(msg):
    if msg in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]:
        return f"{msg.title()}!"
    
    elif msg == "how are you":
        return "I'm fine, thanks!"
    
    elif any(word in msg for word in ["fun", "funny", "joke", "comedy"]):
        jokes = ["Why do Java developers wear glasses? Because they don’t see sharp.", "Why do programmers prefer dark mode? Because light attracts bugs.", "Why did the student eat his homework? Because the teacher said it was a piece of cake.", "Why did the math book look sad? Because it had too many problems.", "What did the ocean say to the beach? Nothing, it just waved."]
        return random.choice(jokes)
    
    elif any(word in msg for word in ["time", "date", "day", "today"]):
        now = datetime.now()
        return now.strftime('Today is %A, %d-%m-%Y and current time is %H:%M')

    elif msg == "bye":
        return "Goodbye!"
    
    elif msg == "help":
        return "You can ask me:\n- hello\n- joke\n- time/date\n- bye"
    
    else:
        return "I don't understand that. Try asking jokes."
    

def main():    
    while True:
        msg = input("\nYou : ").lower().strip()
        reply = replies(msg)
        print(f"Bot : {reply}")
        if msg == "bye":
            break
        


if __name__ == "__main__":
    print("Bot : Welcome to Simple Chatbot!")
    print("Bot : Type 'bye' to exit.")
    main()