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

while True:
    print(" ")
    print("Help")
    print("Contact Us")
    print("Connect with Executive")
    print(" ")

    user_input = input("You: ").lower().strip()

    if user_input != "bye":

        user_input = user_input.lower().strip()

        if user_input in {"hello", "hi", "hey", "sup"}:

            print(f"ChatBot: Hello!! {user_name}")

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

            while True:
                print("ChatBot: Enter your choice")
                ni = input("You: ")

                if ni == "1":
                    print("ChatBot: Tell me what happened to your product.")
                    user_cc = input("You: ")
                    print(" ")
                    print("ChatBot: Your response was recorded. We will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                elif ni == "2":
                    print("ChatBot: Tell me what problem you are facing during the refund process.")
                    user_cc = input("You: ")
                    print(" ")
                    print("ChatBot: Your response was recorded. We will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                elif ni == "3":
                    print("ChatBot: Tell me what service you want.")
                    user_cc = input("You: ")
                    print(" ")
                    print("ChatBot: Your response was recorded. We will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                elif ni == "4":
                    print("ChatBot: You can submit your complaint here.")
                    user_cc = input("You: ")
                    print(" ")
                    print("ChatBot: Your response was recorded. We will contact you as soon as possible.")
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

        elif user_input in {"connect with executive", "executive", "connect executive"}:

            print("ChatBot: Hello, I am Ziggy the bot.")
            print(" ")
            print("1 Call Support")
            print("2 Visit Support")
            print("3 Chat Support")
            print("4 Go Back")
            print("Enter the option number")
            print(" ")

            while True:
                print("ChatBot: Enter your choice")
                ni = input("You: ")

                if ni == "1":
                    print(" ")
                    print("ChatBot: Your response was recorded. Our executive will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                elif ni == "2":
                    print("ChatBot: Your response was recorded. Our executive will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                elif ni == "3":
                    print(" ")
                    print("ChatBot: Your response was recorded. Our executive will contact you as soon as possible.")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                elif ni == "4":
                    print(" ")
                    input("Press 'Enter' to continue")
                    print(" ")
                    print("Anything else you want?")
                    break

                else:
                    print("Choose one of the options.")

        else:

            print("ChatBot: I don't understand that. Please choose one of the options!")

    else:
        print("ChatBot: Thank you for your response ")
        
        break