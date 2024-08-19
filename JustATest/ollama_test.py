#import requests
import ollama

# Your Ollama Server URL
SERVER_URL = "http://localhost:11434" # Replace with your actual server address

if __name__ == "__main__":
    response = ollama.chat(model='gemma2:2b', messages=[
        {
            'role': 'user',
            'content': 'Is the earth flat?',
        }
    ])
    
    print(response['message']['content'])
    