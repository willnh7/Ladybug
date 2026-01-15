## The Leaf python file will be mainly about somehow integrating 
# the chatgpt ai api into an essentially console terminal prompting.


##Pseudocode {
#    Output a prompt for the user to input a question 
#    Read in string from console for the prompt 
#    output response from ai to console,
#    ask again
#    do {
#        output to console for the user to ask a question
#        read in user input as string  then plug into chatgpt 
#        output the response from ai 
#    } while(user wants another response)
#} 


import os
# Quota reached with openai, Switching to gemini.
# from openai import OpenAI

def run():  
    while True:
        # So now would be using chatgpt for the response?
        user_question = input("Do you have a question for the lady(answer no if done)?").lower()

        if (user_question == "no"):
            break
        print(user_question  + "\n")

        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # Or another model like "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_question}
            ],
            max_tokens=150 # Limits the length of the response
        )
        response_content = response.choices[0].message.content
        print(response_content)

def main():
    run()

if __name__ == '__main__':
    main()











