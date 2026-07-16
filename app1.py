import ollama
response=ollama.chat(
    model="gemma3",
    messages=[
        {
            "roll":"user",
            "content":"Hellow"
        }
    ]
)
print(response["message"]["content"])