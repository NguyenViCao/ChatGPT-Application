import openai
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

def generateChatResponse(prompt):
    messages = []
    messages.append({"role": "system", "content": "Your name is Chat GPT bot. You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    
    try:
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except:
        answer = 'The AI is not available to answer your question at the moment. Please try another question.'

    return answer
