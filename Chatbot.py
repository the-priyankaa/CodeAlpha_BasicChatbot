# Variables

user_name = ""
user_input = ""
user_cc = ""
ni = ""

print(" ")
print("ChatBot: Hello! Type 'bye' to exit.")
print(" ")
print(" ")

user_name = input("What is your name? : ")

print(f"ChatBot: How can I help you, {user_name}?")

# Main chatbot loop

while True:

    print(" ")
    print("Help")
    print("Contact Us")
    print("Connect with Executive")
    print(" ")

    # Take user input

    user_input = input("You: ").lower().strip()

     # Check if the user wants to exit

    if user_input != "bye":

         # Convert input to lowercase and remove extra spaces

        user_input = user_input.lower().strip()

        # Greeting Section

        if user_input in {"hello", "hi", "hey", "sup"}:

            print(f"ChatBot: Hello!! {user_name}")

         # Help Section
        elif user_input in {"help"}:

            print("ChatBot: Hello, I am Ziggy the bot. How can I help you?")
            print(" ")
            print("1 Product Related")
            print("2 Refund Related")
            print("3 Service Related")
            print("4 Complaint")
            print("5 Go Back")
            print("Enter the option number")
            print(" ")

            # Help menu loop

            while True:
                print("ChatBot: Enter your choice")
                ni = input("You: ")

                # Product issue

                if ni == "1":
                    print("ChatBot: Tell me what happened to your product.")
                    user_cc = input("You: ")
                    print(" ")
                    print("ChatBot: Your response was recorded. We will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break
                
                # Refund issue

                elif ni == "2":
                    print("ChatBot: Tell me what problem you are facing during the refund process.")
                    user_cc = input("You: ")
                    print(" ")
                    print("ChatBot: Your response was recorded. We will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break
                
                # Service request

                elif ni == "3":
                    print("ChatBot: Tell me what service you want.")
                    user_cc = input("You: ")
                    print(" ")
                    print("ChatBot: Your response was recorded. We will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break
                
                # Complaint section

                elif ni == "4":
                    print("ChatBot: You can submit your complaint here.")
                    user_cc = input("You: ")
                    print(" ")
                    print("ChatBot: Your response was recorded. We will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break
                
                # Go back to main menu

                elif ni == "5":
                    print(" ")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break
                
                # Invalid option

                else:
                    print("Choose one of the options.")

        # Contact Us Section

        elif user_input in {"contact us", "contact"}:

            print("ChatBot: Hello, I am Ziggy the bot. You can contact us using the options below.")
            print(" ")
            print("1 Contact us on Instagram")
            print("2 Contact us on Facebook")
            print("3 Contact us via Email")
            print("4 Contact us on X")
            print("5 Go Back")
            print("Enter the option number")
            print(" ")

            # Contact menu loop

            while True:
                print("ChatBot: Enter your choice")
                ni = input("You: ")

                if ni == "1":
                    print("ChatBot: You can connect with us on our Instagram page @xyz_support")
                    print(" ")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                elif ni == "2":
                    print("ChatBot: You can connect with us on our Facebook page @xyz_support")
                    print(" ")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                elif ni == "3":
                    print("ChatBot: You can contact us via email: xyz_support00@gmail.com")
                    print(" ")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                elif ni == "4":
                    print("ChatBot: You can connect with us on our X page @xyz_support")
                    print(" ")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                elif ni == "5":
                    print(" ")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                else:
                    print("Choose one of the options.")

        # Connect with Executive Section

        elif user_input in {"connect with executive", "executive", "connect executive"}:

            print("ChatBot: Hello, I am Ziggy the bot.")
            print(" ")
            print("1 Call Support")
            print("2 Visit Support")
            print("3 Chat Support")
            print("4 Go Back")
            print("Enter the option number")
            print(" ")

            # Executive support menu

            while True:
                print("ChatBot: Enter your choice")
                ni = input("You: ")

                # Call Support

                if ni == "1":
                    print(" ")
                    print("ChatBot: Your response was recorded. Our executive will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break
                
                # Visit Support

                elif ni == "2":
                    print("ChatBot: Your response was recorded. Our executive will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                # Chat Support
                 
                elif ni == "3":
                    print(" ")
                    print("ChatBot: Your response was recorded. Our executive will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break
                
                # Go back
                elif ni == "4":
                    print(" ")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                # Invalid option
                
                else:
                    print("Choose one of the options.")

        else:

            print("ChatBot: I don't understand that. Please choose one of the options!")

    else:
        print("ChatBot: Thank you for your response ")

        break