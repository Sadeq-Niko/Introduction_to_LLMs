# Make sure ollama in installed in pip
import ollama
model = "gemma3-4b"

prompt = "Explain agentic AI in one sentence."

response = ollama.chat(
    model=model,
    messages = [
        {"role":"user", "content": prompt}
    ]
)

print(response["message"]["content"])