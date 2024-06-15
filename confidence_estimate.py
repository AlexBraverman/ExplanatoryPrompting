import openai
import json
from dotenv import find_dotenv, load_dotenv
import os

# Read the JSON file
with open('../../Downloads/graph_connectivity.json', 'r') as json_file:
    data = json.load(json_file)
# Initialize OpenAI API with your key
API_KEY = '' #insert API key here
messages = []
system_message = "answer questions"
load_dotenv(find_dotenv(), override=True)
openai.api_key = API_KEY
engine = "gpt-4"

def chain_of_thought_prompting(initial_prompt, iterations=5):
    current_prompt = initial_prompt + ", think step-by-step"
    messages = [
        {"role": "system", "content":"you answer like a scientist in a brief and precise manner"},
        {"role": "user", "content": current_prompt}
    ]
    response = openai.ChatCompletion.create(
        model=engine,
        messages=messages,
        max_tokens=150,
        n=iterations,
    )
    return(response)
messages.clear()
tracker = 0
for i in data:
    if tracker == 20:
        break
    messages.clear() 
    file_namer = "../llm-project/Hallucination-Metrics/Step-By-Step/self-consist-confidence-" + str(tracker) + ".txt"
    with open(file_namer, 'w') as output_file:
        # Redirect print statements to the file
        print(chain_of_thought_prompting(i)   , file=output_file)
    tracker += 1
    print("Question number -" , tracker)
