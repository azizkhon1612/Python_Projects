import requests

question_data = [
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linus Torvalds created Linux and Git.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The programming language 'Python' is based off a modified version of 'JavaScript'.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The logo for Snapchat is a Bell.", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "'HTML' stands for Hypertext Markup Language.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Windows 7 operating system has six main editions.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Windows ME operating system was released in the year 2000.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Linux was first created as an alternative to Windows XP.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Python programming language gets its name from the British comedy group 'Monty Python.'",
     "correct_answer": "True", "incorrect_answers": ["False"]}

]


# def get_data(api):
#     response = requests.get(f"{api}")
#     if response.status_code == 200:
#         print("sucessfully fetched the data")
#         print(response.json())
#     else:
#         print(f"Hello person, there's a {response.status_code} error with your request")
#
# get_data(api = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
