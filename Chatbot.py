def chatbot():

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

                print("ChatBot: I'm fine, whtat about you?")
            elif user_input in {"fine", "i am fine", "good"}:

                print("ChatBot: nice, How can i help you")

            elif user_input in {"bye", "goodbye", "see you", "see ya"}:

                print("ChatBot: Goodbye!")
                
            elif user_input in {"thanks", "thank you", "ty"}:

                print("ChatBot: You're welcome!")
                
            else:

                print("ChatBot: I don't understand that.")
        
        else:
            print("ChatBot: Good bye ")

            break

chatbot()