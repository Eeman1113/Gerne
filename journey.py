import openai

openai.api_key = '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'
def get_img(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512",


        )
        img_url = response.images[0].url
    except Exception as e:
        img_url = "https://imgur.com/AD3MbBi"
    return img_url

def chat(inp,message_history, role="user"):
    message_history.append({"role": role, "content": inp})
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message_history)
    
    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": reply_content})
    return reply_content,message_history

message_history = [{"role": "user", "content": """You are an interactive story game bot that proposes some hypothetical fantastical situation where the user needs to pick from 2-4 options that you provide. Once the user picks one of those options, you will then state what happens next and present new options, and this then repeats. If you understand, say, OK, and begin when I say "begin." When you present the story and options, present just the story and start immediately with the story, no further commentary, and then options like "Option 1:" "Option 2:" ...etc."""},{"role": "assistant", "content": f"""OK, I understand. Begin when you're ready."""}]

reply_content,message_history = chat("begin",message_history)

for _ in range(5):
    print(reply_content)
    next_inp = input("Enter your response: ")
    reply_content,message_history = chat(reply_content,message_history)
