import openai

# Set up OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

# Main chat loop
while True:
    # Get user input
    user_input = input("User: ")

    # Check if user wants to exit
    if user_input.lower() == "exit":
        break

    # Send user input to OpenAI API for chat-based completion
    response = openai.Completion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': user_input}
        ]
    )

    # Get the generated chatbot response
    chatbot_response = response.choices[0].message.content

    # Print the chatbot response
    print("ChatGPT: " + chatbot_response)
