name_of_student = input("Name: ")
matric_number_of_student = input("Matriculation Number: ")
score_of_exam = 0

print("Answer the following Questions")
# Question 1
user_answer_question_1 = input("1. Who is the President of SQI, College of ICT? (include abbreviated title)\nYour Answer: ").upper()
keywords_for_question_1 = "DR. ADEYEMI ADERINTO"
answer_for_question_1 = keywords_for_question_1.split()

if answer_for_question_1[0] in user_answer_question_1 and answer_for_question_1[2] in user_answer_question_1 or answer_for_question_1[0] and answer_for_question_1[1] and answer_for_question_1[2] in user_answer_question_1:   
    print("Your Answer is correct")
    score_of_exam += 1
else:
    print("Your Answer is wrong\nThe correct answer is " + keywords_for_question_1 + " or DR. ADERINTO")

# Question 2
user_answer_question_2 = input("2. Mention any state in the South-Western Region of Nigeria\nYour answer: ").lower()
keywords_for_question_2 = "oyo lagos osun ondo ogun kwara ekiti"
answer_for_question_2 = keywords_for_question_2.split()

if answer_for_question_2[0] in user_answer_question_2 or answer_for_question_2[1] in user_answer_question_2 or answer_for_question_2[2] in user_answer_question_2 or answer_for_question_2[3] in user_answer_question_2 or answer_for_question_2[4] in user_answer_question_2 or answer_for_question_2[5] in user_answer_question_2 or answer_for_question_2[6] in user_answer_question_2:
    print("Your Answer is correct")
    score_of_exam += 1
else:
    print("Your Answer is wrong\nThe correct answer is " + keywords_for_question_2.upper())

# Question 3
user_answer_question_3 = input("3. List the colours on the Nigerian flag\nYour Answer: ").lower()
keywords_for_question_3 = "green white"
answer_for_question_3 = keywords_for_question_3.split()

if answer_for_question_3[0] in user_answer_question_3 and answer_for_question_3[1] in user_answer_question_3:
    print("Your Answer is correct")
    score_of_exam += 1
else:
    print("Your Answer is wrong\nThe correct answer is " + keywords_for_question_3.upper())

# Question 4
user_answer_question_4 = input("4. Type the first line of the second stanza of the Nigerian National Anthem\nYour Answer: ")
answer_for_question_4 = "Oh God of creation"

if user_answer_question_4 == answer_for_question_4:
    print("Your Answer is correct")
    score_of_exam += 1
else:
    print("Your Answer is wrong\nThe correct answer is " + answer_for_question_4)

# Question 5
user_answer_question_5 = input("5. Former President _________ served as Nigeria's President from 1999-2007\nYour Answer: ").upper()
keywords_for_question_5 = "OLUSEGUN OBASANJO"
answer_for_question_5 = keywords_for_question_5.split()
if answer_for_question_5[0] in user_answer_question_5 and answer_for_question_5[1] in user_answer_question_5:
    print("Your Answer is correct")
    score_of_exam += 1
else:
    print("Your Answer is wrong\nThe correct answer is "+ keywords_for_question_5)

percentage_of_score = float((score_of_exam/5)*100)
print(name_of_student +"(" + matric_number_of_student + ")" + ", you have completed the examination")
print("Your total score is " + str(percentage_of_score) + "%")


