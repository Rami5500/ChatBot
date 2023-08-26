import openai

openai.api_key = "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"

conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke."},
]

while True:
    user_input = input("You: ")  # Get user input
    conversation.append({"role": "user", "content": user_input})  # Add user input to conversation

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    assistant_reply = response.choices[0].message.content
    print("Assistant:", assistant_reply)

    conversation.append({"role": "assistant", "content": assistant_reply})  # Add assistant reply to conversation

    if user_input.lower() in ["exit", "bye"]:
        print("Goodbye!")
        break  # Exit the loop when the user says "exit" or "bye"

