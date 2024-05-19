import app_st as st
import openai

# Set up OpenAI API key
openai.api_key = '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'

# Define chat function
def chat(inp, message_history, role="user"):
    message_history.append({"role": role, "content": inp})
    
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt='\n'.join([f"{i['role']}: {i['content']}" for i in message_history]),
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    reply_content = completion.choices[0].text.strip()
    message_history.append({"role": "assistant", "content": reply_content})
    return reply_content, message_history

# Define main function
def main():
    # Initialize message history
    message_history = []
    
    # Display introduction message and wait for user to start
    st.write("""Welcome to the interactive story game bot!""")
    st.write("""Please wait for the bot to initiate the conversation.""")
    while True:
        inp = st.text_input("You: ")
        if inp.lower() == "begin":
            reply_content, message_history = chat(inp, message_history, role="user")
            break
    st.write(f"Bot: {reply_content}")
    
    # Loop through conversation
    while True:
        inp = st.text_input("You: ")
        if inp:
            reply_content, message_history = chat(inp, message_history, role="user")
            st.write(f"Bot: {reply_content}")
        else:
            st.write("Please enter a response.")
    
# Run the app
if __name__ == "__main__":
    main()
