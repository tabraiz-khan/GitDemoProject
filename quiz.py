import random

score = 0
operations = ["*", "+", "-"]
print("Start the quiz --> start")
print("End the quiz --> close")

select = input("Enter the options: ").lower()

if select == "close":
    print("Quiz Closed")
elif select == "start":
    while True:
        a = random.randrange(1, 10)
        b = random.randrange(1, 10)
        op = random.choice(operations)

        # Calculate the real answer
        if op == "+":
            correct_ans = a + b
        elif op == "-":
            correct_ans = a - b
        else:
            correct_ans = a * b

        # Ask the user (using f-string for easy formatting)
        user_input = input(f"{a} {op} {b} ---> ")

        # Check if user wants to quit inside the loop
        if user_input.lower() == "close":
            print(f"Quiz Ended. Final Score: {score}")
            break

        # Convert input to int and compare
        if int(user_input) == correct_ans:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer was {correct_ans}")
            print(f"Final Score: {score}")
            break
