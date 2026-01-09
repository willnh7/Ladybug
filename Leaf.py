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


def main():
    run()


    
    


def run():
    while True:
        user_question = input("Ask a question for the Lady: ")
        print(user_question  + "\n")
        # So now would be using chatgpt for the response?

        print("Do you have a question for the lady(answer no if done)?")
        if (user_question == "no"):
            break







if __name__ == '__main__':
    main()











