import openai

openai.api_key = "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"
#The above API Key will not work as it does not allow me to share it on GitHub
#You will have to generate a new key and paste it instead of the above

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")