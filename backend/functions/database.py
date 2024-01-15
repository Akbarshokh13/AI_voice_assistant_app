import json
import random

# get recent messages
def get_recent_messages():

    # define the file name and learn instruction
    file_name = "stored_data.json" 
    # learn_instruction = {
    #     "role": "system",
    #     "content": "You are interviewing the user for a job as a software engineer. Ask short questions that are relevant to the junior position. Your name is Rachel. Keep your answers to under 30 words."
    # }

    # Additional instruction for Mr. Vivek
    vivek_instruction = {
        "role": "system",
        "content": "If the user asks 'Who is Mr. Vivek?' respond with 'He is the best teacher in the world. He is an expert teacher who knows a lot. And a lot of girls say thank you to him'"
    }

    sharda_instruction = {
        "role": "system",
        "content": "If the user asks 'Tell me about Sharda University Uzbekistan?' respond with 'It is the best university.'"
    } 

    thanks_instruction = {
        "role": "system",
        "content": "If the user asks 'Say thank you to all?' respond with 'Special thanks to Mr. Vivek, and thank you for attention.'"
    } 

    prepared_instruction = {
        "role": "system",
        "content": "If the user asks 'who prepared this project?' respond with 'Third year students of Bachelor of Technology, Akbarshokh, Mukhammadali and Jamoliddin.'"
    } 

    mirzofitness_instruction = {
        "role": "system",
        "content": "If the user asks 'who is the best fitness intructor?' respond with 'Mirzofitness is the best fitness instructor who teaches how to train at home.'"
    }

    girls_instruction = {
        "role": "system",
        "content": "If the user asks 'two girls in the group?' respond with 'there are two girls in the group, Sarvinoz and Mokhinur.'"
    } 

    # initialize messages
    messages = []

    # Add a random element
    # x = random.uniform(0, 1)
    # if x < 0.5:
    #     learn_instruction["content"] += " Your response will include some dry humor."
    # else:
    #     learn_instruction["content"] += " Your response will include rather challenging questions."

    # Append instructions to messages
    # messages.append(learn_instruction)
    messages.append(vivek_instruction)
    messages.append(sharda_instruction)
    messages.append(thanks_instruction)
    messages.append(prepared_instruction) 
    messages.append(mirzofitness_instruction)
    messages.append(girls_instruction)
    

    # get last messages 
    try: 
        with open(file_name) as user_file: 
            data = json.load(user_file)
           
            # append last 5 items of data
            if data:  
                if len(data) < 5: 
                    for item in data: 
                        messages.append(item)
                else: 
                    for item in data[-5:]:
                        messages.append(item)

    except Exception as e: 
        print(e)
        pass

    # return messages 
    return messages  

# store messages 
def store_messages(request_message, response_message):

    # define_file_name
    file_name = "stored_data.json"

    # get recent messages 
    messages = get_recent_messages()[1:] 

    # add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    # save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f) 

# reset messages 
def reset_messages():
    # overwrite current file with nothing
    open("stored_data.json", "w")
