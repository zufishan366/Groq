import ollama
response=ollama.chat(
    model="llama3.2",
    messages=[
        {
            "roll":"user",
            "content":"Hellow"
        }
    ]
)
print(response["message"]["content"])