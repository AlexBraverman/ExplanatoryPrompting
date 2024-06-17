import openai
import json

# Read the Dataset JSON file
with open('graph_connectivity.json', 'r') as json_file:
    data = json.load(json_file)

API_KEY = '' # Enter API key

openai.api_key= API_KEY
messages = []
system_message = "answer questions"
messages.append({"role":"system","content":system_message})

tracker = 0
for i in data:
    message = "" + data[tracker] # Enter necessary prompt within quotes
    messages.append({"role":"user","content": message})
  
    response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )

    reply = response["choices"][0]["message"]["content"]
    file_namer = "Tests/result-" + str(tracker) + ".txt"
    with open(file_namer, 'w') as output_file:
        # Redirect print statements to the file
        print(reply, file=output_file)
    tracker += 1
