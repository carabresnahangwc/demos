 #Dictionaries
'''
dictionary = {"key1":"value1",
              "key2":"value2",
              "key3":"value3"}

print(dictionary)
value = dictionary[key]
'''
'''
english_to_spanish = {'hello':'hola',
                      'goodbye':'adios',
                      'table':'mesa',
                      'bread':'pan',
                      'milk':'leche'}

print(english_to_spanish['hello']) #prints hola



# Name and Age dictionary
# Name is the key and Age is the value
name_age = {"Cara":21,
            "Aidan":20,
            "Patty":57,
            "Patrick":58}
print(name_age)
'''

#Cara's method
#make a list of questions
questions = ["What is your name", "How old are you?"]
#make a list of keys the same length as questions
key = ["name","age"]

#empty dictionary {shortenedquestion:answer}
responses = {}
#list of all responses
all_responses = []
notdone = True

while notdone == True:
    people = input("Keep going?")

    if people == 'no':
        notdone = False
    else:
        for index in range(len(questions)):
            response = input(questions[index]+"  ")
            responses[key[index]] = response
        all_responses.append(responses) # add dictionary response to list of all

print(all_responses)



'''


#no answers yet
answers = []
for x in questions:
    # getting answer to question x
    response = input(x)

    # add response into list of answers
    answer.append(response)



# put our key and value into our dictionary
# shortened question and answer to our question into our dictionary of reponses
for i in range(len(questions)):
    responses[key[i]] = answers[i]





reponse = {} #dictionary of answers
#use a for loop for each question
for i in range(len(questions)):
    #ask the question, save the answer input()
    answer = input(questions[i])
    #save key, answer into reponse
    reponse[key[i]] = answer

'''
