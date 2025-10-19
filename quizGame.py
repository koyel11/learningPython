questions=("How many elements are in periodic table?",
           "How many bones a human have?",
           "What is the national Bird of India?",
           "What is the capital of Japan?")

options=(("A. 112","B. 123","C. 118","D. 120"),
         ("A. 200","B. 206","C. 210","D. 213"),
         ("A. Parrot","B. Pigeon","C. Sparrow","D. Peacock"),
         ("A. Tokyo","B. Shanghai","C. Seoul","D. Bangkok"))
answers=("C","B","D","A")
score=0
guesses=[]
question_num=0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option,end=" ")
        print()
    guess=input("Enter a your answer (A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!!")
        print(f"Correct answer is: {answers[question_num]}")
    question_num+=1

print("-----RESULT-----")

print("answers",end=" ")
for answer in answers:
    print(answer,end=" ")

print()

print("guesses",end=" ")
for guess in guesses:
    print(guess,end=" ")

print()

score=int(score/len(questions)*100)
print(f"Your Total Score is:{score}/100")