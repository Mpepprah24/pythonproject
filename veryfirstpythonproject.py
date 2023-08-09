print("This is your very first project!")

username = input("Create your username: ")
password = input("Create your password: ")

_private_password = password

print(f"Congrats on making your account! Welcome, {username}!")

print("As someone learning how to program, write an adjective to describe how excited you are below:")
adj = input("Enter an adjective: ")

print(f"I am {adj} about learning how to program!!")


def login():
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    if entered_username == username and entered_password == _private_password:
        print(f"Welcome back, {username}!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False


def main_menu():
    while True:
        print("1. Basics Concepts")
        print("2. If Else Statements")
        print("3. For and While Loops")
        print("4. Functions")
        print("5. Lists and Tuples")
        print("6. Dictionaries")
        print("7. Classes")
        print("8. Take Quiz")
        print("9. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            basics_concepts()
        elif choice == 2:
            if_else_statements()
        elif choice == 3:
            for_and_while_loops()
        elif choice == 4:
            functions()
        elif choice == 5:
            lists_and_tuples()
        elif choice == 6:
            dictionaries()
        elif choice == 7:
            classes()
        elif choice == 8:
            quiz_menu()
        elif choice == 9:
            print(f"I hope you return, {username}! Have a great day!")
            break
        else:
            print("Invalid choice, please try again.")


def basics_concepts():
    print("Below are some basic concepts in Python you should know:")
    print("Variables - They are containers that store data")
    print("Data Types - There are several data types in Python, including integers, floats, strings, and Booleans")
    print("Operators - Python has several operators that allow you to perform operations on variables, such as +, -, *, and /")


def if_else_statements():
    print("Below describes what if else statements are:")
    print("An if-else statement is used to execute a block of code conditionally.")
    print("It consists of a boolean expression followed by one or more statements that are executed if the boolean expression is True")
    print("An optional else clause followed by one or more statements that are executed if the boolean expression is False.")


def for_and_while_loops():
    print("Below describes what for and while loops are:")
    print("A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable object and execute a block of code for each item in the sequence.")
    print("A while loop, on the other hand, is used to execute a block of code repeatedly as long as a certain condition is true.")
    print("It's important to include a way to update the condition being tested in the while loop, or the loop will run indefinitely (known as an infinite loop). In the example above, the count variable is decremented by 1 on each iteration, eventually reaching 0 and causing the loop to exit.")


def functions():
    print("Below describes what functions are:")
    print("A function is a reusable block of code that performs a specific task.")
    print("The code block within every function starts with a colon : and is indented.")
    print("To call a function, use the function name followed by a set of parentheses () containing any necessary arguments")


def lists_and_tuples():
    print("A list is a collection of items that are ordered and changeable.")
    print("To create a list, use square brackets [] and separate the items with commas.")
    print("To access an item in a list, use its index in square brackets [].")
    print("To change an item in a list, use its index in square brackets [] followed by the assignment operator =. To add an item to the end of a list, use the append() method. To add an item at a specific index in a list, use the insert() method. To remove an item from a list, use the remove() or pop() method.")


def dictionaries():
    print("A dictionary is a collection of items that are unordered, changeable, and indexed.")
    print("To create a dictionary, use curly braces {} and specify key-value pairs as key: value.")
    print("To access an item in a dictionary, use its key in square brackets [].")
    print("To change an item in a dictionary, use its key in square brackets [] followed by the assignment operator =. To add an item to a dictionary, use the update() method. To remove an item from a dictionary, use the pop() method.")


def classes():
    print("A class is a template for creating objects")
    print("It defines the characteristics and behaviors of the objects that will be created from the class.")
    print("To create a class, use the class keyword followed by the class name and a colon :.")
    print("An attribute is a characteristic or property of an object, while a method is a function that belongs to an object. To create an object from a class, use the class name followed by a set of parentheses ().")


def quiz_menu():
    print(f"Now that you have learned the basics of Python, {username}, here's a quiz to test your knowledge:")
    answer = input("Would you like to take the quiz? (y=yes, n=no): ")
    if answer.lower() == 'y':
        run_quiz()
    else:
        print("If you want to take the quiz, just log back in. Bye!")


def run_quiz():
    print("Answer the following questions:")
    score = 0
    for question in questions:
        user_answer = input(question.prompt)
        if user_answer.lower() == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "1. What is a variable?\n(a) A container for storing data\n(b) A data type\n(c) An operator\n",
    "2. What is a data type in Python?\n(a) A container for storing data\n(b) A specific kind of data with a certain behavior\n(c) An operator\n",
    "3. What are some examples of data types in Python?\n(a) Integers, floats, and strings\n(b) Booleans, lists, and dictionaries\n(c) Functions, modules, and classes\n",
    "4. What is an if-else statement used for in Python?\n(a) To execute a block of code conditionally\n(b) To iterate over a sequence\n(c) To create a function\n",
    "5. What is an else clause in an if-else statement used for in Python?\n(a) To execute a block of code if the boolean expression is True\n(b) To execute a block of code if the boolean expression is False\n(c) To create a function\n",
    "6. What is a for loop used for in Python?\n(a) To execute a block of code repeatedly as long as a certain condition is true\n(b) To iterate over a sequence\n(c) To create a function\n",
    "7. What is the correct syntax for a for loop in Python?\n(a) for i in range:\n(b) for i in range():\n(c) for (i in range):\n",
    "8. What is the correct syntax for a while loop in Python?\n(a) while {condition}:\n(b) while (condition):\n(c) while condition\n(d) while condition:\n",
    "9. What is the correct syntax for defining a function in Python?\n(a) def function_name():\n(b) def name():\n(c) function(name):\n(d) def(name):\n",
    "10. What is the correct syntax for creating a list in Python?\n(a) list = [1, 2, 3]\n(b) [1, 2, 3]\n(c) (1, 2, 3)\n(d) {1, 2, 3}\n",
    "11. How do you access a value in a dictionary using its key?\n(a) dict[key]\n(b) dict{key}\n(c) dict(\"key\")\n(d) dict 'key'\n",
    "12. How do you create an object of a class in Python?\n(a) object = MyClass()\n(b) object(MyClass)\n(c) new MyClass()\n(d) create MyClass()\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "d"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "a"),
    Question(question_prompts[11], "a")
]


main_menu()





