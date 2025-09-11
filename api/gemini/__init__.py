from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.environ.get("GOOGLE_API_KEY"),
)

# response = client.models.generate_content(
#    model="gemini-2.5-flash",
#    contents="Explain how AI works in a few words",
#    config=types.GenerateContentConfig(
#        thinking_config=types.ThinkingConfig(thinking_budget=0)  # Disables thinking
#    ),
# )
# print(response.text)


def get_response(prompt):
    prompt = (
        "Assume you are a mental health expert and are helping struggling and stressed campus students, so reply to the following question in the language of the folowing prompt, and act as if it is a conversation and preferably keep answers short and friendly: \n"
        + prompt
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_budget=-1
            )  # Disables thinking
        ),
    )
    return response.text
