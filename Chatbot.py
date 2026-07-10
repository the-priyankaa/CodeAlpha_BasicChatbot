import random

quotes = ["Whatever our souls are made of, his and mine are the same. — Emily Brontë","The best thing to hold onto in life is each other. — Audrey Hepburn","I sustain myself with the love of family. — Maya Angelou","We love because it's the only true adventure. — Nikki Giovanni","To love and be loved is to feel the sun from both sides. — David Viscot"]

user_name = ""
user_input = ""

print("ChatBot: Hello! Type 'bye' to exit.")

user_name = input("What is your name?:")

print(f"ChatBot: Hello!! {user_name}")

while True:
    user_input = input("You: ").lower().strip()
    
    if user_input != "bye":
                    
        user_input = user_input.lower().strip()

        if user_input in {"hello", "hi", "hey", "sup"}:

            print(f"ChatBot: Hello!! {user_name}")
                
        elif user_input in {"how are you", "how's it going", "how are you doing"}:

            print("ChatBot: I'm fine, what about you?")

        elif user_input in {"fine", "i am fine", "good"}:

            print("ChatBot: nice, How can I help you ?")

        elif user_input in {"quote plz", "give me a quote", "quote of the day", "quote"}:

            print(random.choice(quotes))
                
        elif user_input in {"thanks", "thank you", "ty"}:

            print("Your welcome")
                
        else:

            print("ChatBot: I don't understand that.")
        
    else:
        print("ChatBot: Good bye ")

        break