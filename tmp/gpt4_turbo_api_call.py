import openai

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

# Make a request to the GPT-4 Turbo model
response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]
)

# Print the response
print(response.choices[0].message['content'])