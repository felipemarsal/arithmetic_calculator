import random

math_symbols = ["+", "-", "*"]
correct_answer_txt = "Right!"
wrong_answer_txt = "Wrong!"
incorrect_format_txt = "Incorrect format."
correct_answers = 0


def integral_squares():
    global correct_answers
    op_to_answer = random.randint(11, 29)
    print(op_to_answer)

    while True:
        try:
            user_input = int(input())
        except:
            print("Incorrect format.")
            print(op_to_answer)
        else:
            if int(user_input) == op_to_answer ** 2:
                correct_answers += 1
                print(correct_answer_txt)
                break
            else:
                print(wrong_answer_txt)
                break


def simple_operation():
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    symbol = random.choice(math_symbols)
    variable_to_solve = str(x) + " " + symbol + " " + str(y)
    return variable_to_solve


def testing_user_answer_so():
    global correct_answers
    op_to_answer = simple_operation()
    print(op_to_answer)
    op_to_answer_eval = eval(op_to_answer)

    while True:
        try:
            user_input = int(input())
        except:
            print("Incorrect format.")
            print(op_to_answer)
        else:
            if int(user_input) == op_to_answer_eval:
                correct_answers += 1
                print(correct_answer_txt)
                break
            else:
                print(wrong_answer_txt)
                break


def saving_user():
    saved_mark = input(
        f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.\n").lower()

    if saved_mark == "yes" or saved_mark == "y":
        user_name = input("What is your name?\n")
        with open('results.txt', 'a') as file:
            if user_level == 1:
                file.write(f"{user_name}: {correct_answers}/5 in level 1 (simple operations with numbers 2-9)")
                print('The results are saved in "results.txt"')
            else:
                file.write(f"{user_name}: {correct_answers}/5 in level 2 (integral squares 11-29)")
                print('The results are saved in "results.txt"')

while True:
    try:
        user_level = int(input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9 \n"
                               "2 - integral squares of 11-29\n"))
    except:
        print("Incorrect format.")
    else:
        if int(user_level) == 1 or int(user_level) == 2:
            break
        else:
            print("Incorrect format.")

for question in range(5):
    if user_level == 1:
        testing_user_answer_so()
    elif user_level == 2:
        integral_squares()

saving_user()
