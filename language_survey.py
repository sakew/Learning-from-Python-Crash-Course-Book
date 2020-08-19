from Learning_from_python_crash_course_book.survey import AnonymousSurvey

#Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#Show the question and store the responses.

my_survey.show_question()
print("Enter 'q' if you want to quit.")
while True:
    response = input("Input language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Show the survey results.

print("\nThank you to everyone who participated to this survey!")
print(my_survey.responses)
my_survey.show_results()