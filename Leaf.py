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
from google import genai

def run():  
    while True:
        # So now would be using chatgpt for the response?
        user_question = input("Do you have a question for the lady(answer no if done)?").lower()
        # This is the user question that should create a image of this for the ladybug to traverse/ fly across.
        if (user_question == "no"):
            break
        print(user_question  + "\n")

        # There is now a functional response to text by the gemini ai model(gemini-2.5-flash-lite) 
        print("Answer:")
        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=user_question + " Use 2 sentences at most.",
        )
        print(response.text)

        

def main():
    run()

if __name__ == '__main__':
    main()











