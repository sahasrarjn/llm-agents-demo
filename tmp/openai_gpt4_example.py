import openai

# Set your API key
openai.api_key = 'your-api-key-here'

# Define the request parameters
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you explain the theory of relativity?"}
    ]
)

# Print the response
print(response.choices[0].message['content'])