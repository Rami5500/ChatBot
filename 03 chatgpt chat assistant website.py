import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a financial expert that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Define your custom components for the UI
input_text = gradio.inputs.Textbox(lines=2, label="Enter your message:")
output_text = gradio.outputs.Textbox(label="Assistant's Reply:")

# Customize the UI using the components
demo = gradio.Interface(
    fn=CustomChatGPT,
    inputs=input_text,
    outputs=output_text,
    title="Real Estate Pro",
    description="Ask questions about real estate investment and negotiation.",
    article="https://example.com/article",
    examples=[
        ["Tell me about property valuation."],
        ["What are the best locations for real estate investment?"],
    ]
)

# Launch the customized UI
demo.launch(share=True)
