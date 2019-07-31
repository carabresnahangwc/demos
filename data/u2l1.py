import json

q1 = "What is your name?"
q2 = "What is your date of birth? (MM/DD/YYYY)"
q3 = "What is your age?"
q4 = "Where do you call home? (City, State, Country)"
q5 = "How many people live in your home more than 50% of the time?"
q6 = "How many hours per week do you spend on the phone?"
q7 = "Name the app, program, or website that you use most frequently."
q8 = "Favorite song right now?"
q9 = "Last binged tv show?"
q10 = "If you could meet anyone, who would it be?"

#questions = {"name":q1, "DOB":q2, "age":q3,"home":q4,"numinhouse":q5,
    #         "hoursonphone"}

questions = [q1,q2]#,q3,q4,q5,q6,q7,q8,q9,q10]
keys = ["name", "DOB", "age", "home", "numinhouse", "hours on phone", "app", "song", "tv", "person"]
all_responses = []

def survey1():

    responses = {}
    for x in range(len(questions)):
        answer = input(questions[x]+" ")
        responses[keys[x]] = answer

    print(responses)

def survey2():

    while True:
        keepgoing = input("Do you want to take a survey?")

        if keepgoing == 'y':

            responses = {}
            for x in range(len(questions)):
                answer = input(questions[x]+" ")
                responses[keys[x]] = answer
            all_responses.append(responses)
        else:
            break

    #open and load old data to new file
    #f = open("allanswers.json", "r")

    #olddata = json.load(f)
    #all_responses.extend(olddata)
    #f.close()

    # Reopen the file in write mode and write each entry in json format.
    f = open("allanswers.json", "w")
    f.write('[\n')
    index = 0
    for t in all_responses:
        if (index < len(all_responses)-1):
            json.dump(t, f)
            f.write(',\n')
        else:
            json.dump(t, f)
            f.write('\n')
        index += 1

    f.write(']')
    f.close()

    print(all_responses)

def get_names(all_responses):
    names = []
    for s in range(len(all_responses)):
        names.append(all_responses[s]["name"])
    print(names)

def savedata():
    #open and load old data to new file
    f = open("allanswers.json", "r")
    olddata = json.load(f)
    all_responses.extend(olddata)
    f.close()

    # Reopen the file in write mode and write each entry in json format.
    f = open("allanswers.json", "w")
    f.write('[\n')
    index = 0
    for t in all_responses:
        if (index < len(all_responses)-1):
            json.dump(t, f)
            f.write(',\n')
        else:
            json.dump(t, f)
            f.write('\n')
        index += 1

    f.write(']')
    f.close()

survey1()
