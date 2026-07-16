import ollama

print("=" * 50)
print("Powered by Ollama - Llama 3.2")
print("Type 'exit' to stop the program")
print("=" * 50)

while True:
    input_user = input("\nYour input: ")

    if input_user.lower() == "exit":
        print("\nThanks for using the chatbot!")
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": input_user
            }
        ]
    )

    print("\nAI:", response["message"]["content"])