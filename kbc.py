l = [
    [
        "what is the capital of India?",
        "Mumbai",
        "Chennai",
        "Delhi",
        "Banglore",
        3
    ],
    [
        "which is the programming language created by gudio van russom?",
        "C",
        "Java",
        "Swift",
        "Python",
        4,
    ],
    [
        "who is the former president of India?",
        "Draupati Murmu",
        "Ramnath Kovinth",
        "Pranab Mukharjee",
        "Dr APJ Abdul Kalam",
        2,
    ],
    [
        "which is the programming language created by gudio van russom?",
        "C",
        "Java",
        "Swift",
        "Python",
        4,
    ],
    [
        "who is the former president of India?",
        "Draupati Murmu",
        "Ramnath Kovinth",
        "Pranab Mukharjee",
        "Dr APJ Abdul Kalam",
        2,
    ],
]

money = 0

levels = [10000, 20000, 100000, 500000, 1000000]

for i in range(len(l)):
    question = l[i]
    print(f"question for Rs.{levels[i]}")
    print(question[0])
    print(f"A.{question[1]}             B.{question[2]}")
    print(f"C.{question[3]}             D.{question[4]}")

    answer = eval(input("enter your answer (1-4):"))

    if answer == question[5]:
        print(f"correct answer!! you won {levels[i]}")
        money = levels[i]

    else:
        print('ohh too bad wrong answer\nbetter luck next time')
        break

print(f"the amount you won is {money}!!")
print("thanks for playing")