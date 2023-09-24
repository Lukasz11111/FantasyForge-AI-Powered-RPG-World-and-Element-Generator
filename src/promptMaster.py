import os
import openai
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

openai.organization =os.getenv("OPENAI_API_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatCompletionCreate(prompt):
  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": f"{prompt}"}
  ]
  )
  return completion

