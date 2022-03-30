#! /usr/bin/python

#chmod +x SCRIPTNAME.py
#./SCRIPTNAME.py

quiz1 = [5,5,15,15,15,15,20]
quiz2 = [10,10,10,15,10,10,10,15]

def gen_marks(questions):
    results = []
    for question, points in enumerate(questions):
        results.append(int(input(f"Question {question + 1}, {points}:")))
    print(f"Marks: {sum(results)}/{sum(questions)}, {sum(results)/sum(questions)*100:.2f}%")

while True:
    gen_marks(quiz2)
    print("\n")
