import random

questions = []
answers = []
correct = 0
counter = 0

print("Welcome to the quiz game!")
while True:
    question = str(input("Input a name/topic: "))
    answer = str(input("Enter the answer to that specfic name/topic: "))
    questions.append(question)
    answers.append(answer)
    
    stop = str(input("Would you like to continue (y/n)? "))
    if stop.lower().strip() == "n":
        break 

print("------------------------------------")
print()
print("------------------------------------")
print()
print("------------------------------------")
print()
print("------------------------------------")
print()
print("------------------------------------")
print()
print("------------------------------------")
print()
print("------------------------------------")
print()
print("------------------------------------")
print()

running = True
while running:
    print("Time to test your skills")
    current = random.randint(0,len(questions)-1)
    print(questions[current])
    user_answer = str(input("Type in your answer "))
    if user_answer == answers[current]:
        correct += 1
        counter += 1
    
    stop = str(input("Would you like to continue (y/n)? "))
    if stop.lower().strip() == "n":
        running = False

print(f"Average : {correct/counter:2f}")
print(f"Correct answers : {correct}")