"""
This is meant to help users study by converting latex documents into 
slow questionaires where the user must answer before displaying an 
answer. We do this to allow the user to study with themselves.

Latex Format. ONLY HAVE ONE itemize section in latex. Each item 
will be considered the question line. Each line afterwards will 
be considered the answer lines until we reach a question line again.
"""
import random

"""
Handles a singular instance of a question.
"""
class question:
    def __init__(self, question, answer):
        self.q = question 
        self.a = answer

"""
Master of questions.
"""
class questionWrapper:
    def __init__(self, fName):
        file = open(fName, "r")
        lines = file.readlines()
        tmp = ""
        q = ""
        a = ""
        self.questions = []

        while len(lines) != 0:
            tmp = lines[0]
            lines[0].pop(0)
            if tmp == "\begin{itemize}":
                break

        while len(lines) != 0:
            tmp = lines[0]
            if "\item" in tmp:
                self.questions.append(question(q, a))
                q = tmp
                a = ""
            elif "\end{itemize}" in tmp:
                break
            else:
                a += tmp
            lines.pop(0)
        
        def pickRandom(self):
            return random.choice(self.questions)

            
        pass

def main():
    file = input("Please insert a file pathway. \n")
    quizData = questionWrapper(file)

"""
Handles hiding and displaying questions.
"""
def quiz(quizData):
    inp = ""
    q = None
    print("Enter q to quit. Enter anything else for to reveal answer.")
    while inp != "q":
        q = quizData.pickRandom()
        print("Question\n")
        print(q.q)
        inp = input()
        print(q.a)

if __name__ == "__main__":
    main()