import os
import vertexai

PROJECT_ID = "refined-analogy-435508-n3"  
LOCATION = "us-central1" 

vertexai.init(project=PROJECT_ID, location=LOCATION)

def create_session():
    chat_model = vertexai.language_models.ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat()
    return chat

def response(chat, message):
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    result = chat.send_message(message, **parameters)
    return result.text

def run_chat():
    chat_model = create_session()
    print(f"Chat Session created")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        content = response(chat_model, user_input)
        print(f"AI: {content}")

if __name__ == '__main__':
    run_chat()






















     business_idea_prompt =  f"""
    
    Business Idea: Generate a unique business concept based on the following input: {message}.\n"
    Market Analysis: Identify potential market share and percentage, detailing local and international competitors input {message}\n
    Investment Requirements: Outline the financial investment needed, including a breakdown of costs in bullet points. {message}\n
    Actionable Steps: Provide a clear and structured plan for implementation, with specific actions to take at each stage. {message}\n
    Risks and Challenges: Highlight potential risks and challenges associated with the business idea, along with strategies to mitigate them. {message}\n
    and , provide insights, advice, and actionable recommendations as if you were an integral part of my company.
    
    """
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 356,
        "top_p": 0.8,
        "top_k": 40
    }
    # Send the modified prompt to generate business ideas
    result = chat.send_message(business_idea_prompt, **parameters)  # <-- Updated this line
    return result.text