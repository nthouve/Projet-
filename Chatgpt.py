import openai

openai.api_key = "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"  # Replace with your actual OpenAI API key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response['choices'][0]['message']['content'])