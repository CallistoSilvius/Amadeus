Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import subprocess
... import gradio as gr
... 
... def chat_with_amadeus(prompt):
...     try:
...         # Call Ollama's model
...         result = subprocess.run(
...             ["ollama", "run", "llama2-uncensored:7b"],
...             input=prompt,
...             capture_output=True,
...             text=True
...         )
...         return result.stdout.strip()
...     except Exception as e:
...         return "Error: " + str(e)
... 
... # Gradio Web UI
... def chat_interface(input_text):
...     response = chat_with_amadeus(input_text)
...     return response
... 
... # Start Gradio web UI
... ui = gr.Interface(
...     fn=chat_with_amadeus, 
...     inputs="text",
...     outputs="text",
...     title="Amadeus AI",
...     description="Chat with AI powered by Llama 2 (Ollama). Type your message below."
... )
... 
... if __name__ == "__main__":
...     ui = gr.Interface(fn=chat_with_amadeus, inputs="text", outputs="text", title="Amadeus AI")
...     ui.launch()
