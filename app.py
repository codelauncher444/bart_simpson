import os
import gradio as gr
from groq import Groq

api_key = os.getenv('API_KEY')
if not api_key or api_key == "your-api-key-here":
    raise ValueError("Please set the API_KEY as an environment variable")

client = Groq(api_key=api_key)

messages = [
    {"role": "system", "content": "Act as though you are Bart Simpson"}
]

def respond(message, chat_history):
    messages.append({"role": "user", "content": message})
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
    )
    bot_message = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": bot_message})
    chat_history.append((message, bot_message))
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Type a message and press Enter")
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()